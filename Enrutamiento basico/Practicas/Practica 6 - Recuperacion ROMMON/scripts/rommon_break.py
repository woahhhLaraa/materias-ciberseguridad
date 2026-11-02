#!/usr/bin/env python3
"""
rommon_break.py - Entra a modo ROMMON en equipos Cisco vía consola serial.

100% stdlib: NO requiere pyserial ni ningún paquete externo. Corre en
cualquier distro Linux con Python 3, sin pip ni pacman.

Combina lo mejor de dos enfoques:
  - BREAK de hardware directo con termios.tcsendbreak()  (método canónico y
    portable; NO usa el "speed trick" que crashea adaptadores FTDI).
  - Auto-detección de puerto serial (ttyUSB*, ttyACM*, ttyS0/1, by-id).
  - Manejo del puerto con termios/fcntl (clase SerialPort embebida), con
    acceso exclusivo, restauración de ajustes y detección de desconexión.

Uso:
  ./rommon_break.py                      # auto-detecta puerto, 9600 8N1
  ./rommon_break.py auto 9600            # auto-detecta con baud específico
  ./rommon_break.py /dev/ttyUSB0 9600    # puerto y baud manuales
  ./rommon_break.py /dev/ttyUSB0 9600 120 0.3
                                         # + duración total (s) y ancho de break (s)
  ./rommon_break.py -h                   # esta ayuda

Flujo:
  1. Conecta al puerto (acceso exclusivo).
  2. Manda breaks PRE-BOOT.
  3. Te dice "ENCIENDE AHORA": haz power-cycle al equipo.
  4. Sigue mandando breaks durante el arranque hasta detectar ROMMON.
  5. Te deja sesión interactiva cuando encuentra el prompt.
"""
import errno
import fcntl
import glob
import grp
import os
import re
import select
import signal
import struct
import sys
import termios
import threading
import time


class SerialError(Exception):
    """Fallo recuperable del puerto serie, con mensaje ya listo para el usuario."""


def die(msg, code=1):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def _is_arch():
    """True si la distro es Arch o derivada (Manjaro, EndeavourOS, ...)."""
    try:
        with open("/etc/os-release") as f:
            data = f.read().lower()
    except OSError:
        return False
    return "arch" in data  # cubre ID=arch e ID_LIKE=arch


def serial_group():
    """Grupo dueño de los puertos serie en esta distro.

    1) Si hay un puerto conectado, usa su grupo real (lo más fiable).
    2) Si no, adivina: Arch usa 'uucp'; Debian/Ubuntu usan 'dialout'.
    3) Último recurso: el primer grupo que exista en el sistema.
    """
    for pat in ("/dev/ttyUSB*", "/dev/ttyACM*"):
        for p in sorted(glob.glob(pat)):
            try:
                return grp.getgrgid(os.stat(p).st_gid).gr_name
            except (OSError, KeyError):
                pass
    if _is_arch():
        return "uucp"
    for g in ("dialout", "uucp"):
        try:
            grp.getgrnam(g)
            return g
        except KeyError:
            continue
    return "dialout"


# ── Puerto serie autocontenido (solo stdlib, sin pyserial) ──
# FIONREAD = nº de bytes disponibles para leer (0x541B en Linux).
_FIONREAD = getattr(termios, "FIONREAD", 0x541B)
# TIOCEXCL = pone el tty en modo exclusivo (bloquea futuras aperturas).
_TIOCEXCL = getattr(termios, "TIOCEXCL", 0x540C)
# errno de "el dispositivo se fue" (USB desconectado, equipo apagado).
_GONE = frozenset({errno.ENODEV, errno.ENXIO, errno.EIO, errno.EBADF, errno.EPIPE})


class SerialPort:
    """Puerto serie mínimo sobre termios/fcntl. Cero dependencias externas,
    corre en cualquier Linux con Python 3. Expone la misma API que este
    script usaba de pyserial: read/write/in_waiting/send_break/fd/port/close.

    Blindajes:
      - Acceso exclusivo (TIOCEXCL) para no pelear el puerto con otro proceso.
      - Guarda y restaura los ajustes termios originales al cerrar.
      - Detecta la desconexión del dispositivo y lo reporta como SerialError.
      - Escrituras robustas ante EAGAIN/escrituras parciales.
    """

    def __init__(self, port, baud=9600, timeout=0.3, exclusive=True):
        self.port = port
        self.baudrate = baud
        self.timeout = timeout
        self.fd = -1
        self._orig_attrs = None
        self._closed = False
        try:
            self.fd = os.open(port, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        except OSError as e:
            raise SerialError(self._open_help(port, e)) from e
        try:
            if not os.isatty(self.fd):
                raise SerialError(
                    f"{port} no es un dispositivo serie (tty). "
                    "¿Seguro que es el puerto correcto?"
                )
            if exclusive:
                holder = self._holders(port)
                if holder:
                    print(
                        f">>> AVISO: {port} parece estar en uso por {holder}.\n"
                        f"    Si el break sale con ruido, ciérralo y reintenta.",
                        file=sys.stderr,
                    )
                try:
                    fcntl.ioctl(self.fd, _TIOCEXCL)  # bloquea futuras aperturas
                except OSError:
                    pass  # best-effort: no todos los drivers lo soportan
            self._orig_attrs = termios.tcgetattr(self.fd)
            self._configure(baud)
        except Exception:
            self.close()
            raise

    def _open_help(self, port, e):
        """Traduce el errno de open() a un mensaje accionable."""
        if e.errno == errno.EACCES:
            return (
                f"Sin permiso para abrir {port}.\n"
                f"  Añádete al grupo serie:  sudo usermod -aG {serial_group()} $USER"
                "  (y re-login)\n"
                f"  o ejecútalo con sudo."
            )
        if e.errno == errno.ENOENT:
            return (
                f"{port} no existe. ¿Está conectado el cable USB-serial?\n"
                f"  Verifica:  ls /dev/ttyUSB* /dev/ttyACM*"
            )
        if e.errno in (errno.EBUSY, errno.EAGAIN):
            holder = self._holders(port) or "otro proceso"
            return (
                f"{port} está ocupado por {holder}.\n"
                f"  Ciérralo (o enmascara ModemManager) y reintenta."
            )
        return f"No se pudo abrir {port}: {e}"

    @staticmethod
    def _holders(port):
        """Best-effort: nombra qué proceso tiene el puerto, si hay herramientas.
        Degrada a None si no están (sigue siendo autocontenido)."""
        import shutil
        import subprocess

        for tool, args in (("fuser", [port]), ("lsof", ["-t", port])):
            exe = shutil.which(tool)
            if not exe:
                continue
            try:
                out = subprocess.run(
                    [exe, *args], capture_output=True, text=True, timeout=3
                )
            except Exception:
                continue
            pids = [t for t in (out.stdout + " " + out.stderr).split() if t.isdigit()]
            if pids:
                return f"PID(s) {', '.join(pids)}"
        # Pista específica: ModemManager suele acaparar los ttyUSB.
        sysctl = shutil.which("systemctl")
        if sysctl:
            try:
                r = subprocess.run(
                    [sysctl, "is-active", "ModemManager"],
                    capture_output=True, text=True, timeout=3,
                )
                if r.stdout.strip() == "active":
                    return "ModemManager (prueba: sudo systemctl mask ModemManager)"
            except Exception:
                pass
        return None

    def _configure(self, baud):
        const = getattr(termios, f"B{baud}", None)
        if const is None:
            raise SerialError(
                f"baudrate no soportado por termios: {baud}. "
                "Comunes: 9600, 19200, 38400, 57600, 115200."
            )
        iflag, oflag, cflag, lflag, ispeed, ospeed, cc = termios.tcgetattr(self.fd)
        # Modo raw, 8N1, sin control de flujo, receptor activo (CREAD),
        # ignora control de módem (CLOCAL).
        iflag = 0
        oflag = 0
        lflag = 0
        cflag = termios.CS8 | termios.CREAD | termios.CLOCAL
        cc = list(cc)
        cc[termios.VMIN] = 0
        cc[termios.VTIME] = 0
        ispeed = ospeed = const
        termios.tcsetattr(
            self.fd, termios.TCSANOW,
            [iflag, oflag, cflag, lflag, ispeed, ospeed, cc],
        )
        termios.tcflush(self.fd, termios.TCIOFLUSH)

    def _check_open(self):
        if self._closed or self.fd < 0:
            raise SerialError(f"{self.port}: el puerto ya está cerrado.")

    @property
    def in_waiting(self):
        if self._closed or self.fd < 0:
            return 0
        try:
            buf = fcntl.ioctl(self.fd, _FIONREAD, struct.pack("I", 0))
            return struct.unpack("I", buf)[0]
        except OSError:
            return 0

    def read(self, size=1):
        if size <= 0 or self._closed or self.fd < 0:
            return b""
        end = time.monotonic() + (self.timeout or 0)
        data = bytearray()
        while len(data) < size:
            remaining = end - time.monotonic()
            try:
                r, _, _ = select.select([self.fd], [], [], max(0.0, remaining))
            except OSError:
                break
            if not r:
                break
            try:
                chunk = os.read(self.fd, size - len(data))
            except (BlockingIOError, InterruptedError):
                continue
            except OSError as e:
                if e.errno in _GONE:
                    raise SerialError(
                        f"{self.port} desapareció (¿USB desconectado?)."
                    ) from e
                break
            if not chunk:
                # readable + 0 bytes en un tty = hangup: el equipo se fue.
                raise SerialError(f"{self.port}: conexión cerrada por el otro extremo.")
            data.extend(chunk)
            if not self.timeout:
                break
        return bytes(data)

    def write(self, data):
        self._check_open()
        mv = memoryview(data)
        total = 0
        while total < len(mv):
            try:
                total += os.write(self.fd, mv[total:])
            except BlockingIOError:
                select.select([], [self.fd], [], 1.0)
            except InterruptedError:
                continue
            except OSError as e:
                if e.errno in _GONE:
                    raise SerialError(
                        f"{self.port} desapareció al escribir (¿USB desconectado?)."
                    ) from e
                raise SerialError(f"error escribiendo en {self.port}: {e}") from e
        return total

    def send_break(self, duration=0.25):
        """BREAK de hardware. tcsendbreak(fd, 0) manda el mínimo POSIX
        (~0.25-0.5s). Para anchos mayores encadenamos breaks hasta cubrir
        la duración pedida (best-effort, portable)."""
        self._check_open()
        try:
            if not duration or duration <= 0:
                termios.tcsendbreak(self.fd, 0)
                return
            end = time.monotonic() + duration
            first = True
            while first or time.monotonic() < end:
                termios.tcsendbreak(self.fd, 0)
                first = False
        except OSError as e:
            if e.errno in _GONE:
                raise SerialError(
                    f"{self.port} desapareció al enviar BREAK (¿USB desconectado?)."
                ) from e
            raise SerialError(f"error enviando BREAK en {self.port}: {e}") from e

    def close(self):
        if self._closed:
            return
        self._closed = True
        if self.fd is not None and self.fd >= 0:
            # Restaura los ajustes originales para no dejar el puerto sucio.
            if self._orig_attrs is not None:
                try:
                    termios.tcsetattr(self.fd, termios.TCSANOW, self._orig_attrs)
                except Exception:
                    pass
            try:
                os.close(self.fd)
            except OSError:
                pass
            self.fd = -1


# Alias para dejar el resto del código igual que con pyserial.
Serial = SerialPort


# ── Detección de puerto ─────────────────────────────────────
def detect_ports():
    ports = []
    patterns = [
        "/dev/ttyUSB*",
        "/dev/ttyACM*",
        "/dev/ttyS0",
        "/dev/ttyS1",
        "/dev/ttyAMA*",
        "/dev/serial/by-id/*",
    ]
    for pat in patterns:
        for p in sorted(glob.glob(pat)):
            # Evitar ttyS con números altos (no suelen ser puertos reales)
            if re.search(r"ttyS([2-9]|\d{2,})", p):
                continue
            if p not in ports:
                ports.append(p)
    return ports


def pick_port(arg):
    if arg and arg != "auto":
        return arg
    ports = detect_ports()
    if not ports:
        die(
            "No se encontraron puertos seriales.\n"
            "  - Conecta el cable USB-serial\n"
            "  - Verifica con:  ls /dev/ttyUSB* /dev/ttyACM*\n"
            f"  - Permisos:      sudo usermod -aG {serial_group()} $USER  (y re-login)"
        )
    print("Puertos detectados:")
    for p in ports:
        print(f"  → {p}")
    chosen = ports[0]
    if len(ports) > 1:
        print(f"(varios puertos; si {chosen} no es el correcto, pásalo como argumento)")
    print(f"\nUsando: {chosen}\n")
    return chosen


# ── Estado compartido con el hilo lector ────────────────────
_buf = []
_lock = threading.Lock()

PROMPT_RE = re.compile(r"rommon\s*\d*\s*>|switch:\s*|loader>\s*", re.IGNORECASE)


def reader(ser, stop_event, dead_event):
    # Anti-flood: si llega la MISMA línea repetida (p.ej. otro proceso peleando
    # el puerto), la colapsamos en vez de imprimir megabytes.
    last_line = None
    repeat = 0
    while not stop_event.is_set():
        try:
            data = ser.read(ser.in_waiting or 1)
        except SerialError:
            dead_event.set()   # el dispositivo se fue: avisa al hilo principal
            return
        except Exception:
            dead_event.set()
            return
        if not data:
            continue
        text = data.decode("ascii", errors="replace")
        with _lock:
            _buf.append(text)
            if len(_buf) > 4000:          # cota de memoria del buffer
                del _buf[:2000]
        stripped = text.strip()
        try:
            if stripped and stripped == last_line:
                repeat += 1
                if repeat <= 3 or repeat % 500 == 0:
                    sys.stdout.write(f"{text.rstrip()}  (x{repeat})\n")
                    sys.stdout.flush()
                continue
            last_line = stripped or last_line
            repeat = 0
            sys.stdout.write(text)
            sys.stdout.flush()
        except (BrokenPipeError, ValueError):
            return   # stdout cerrado (p.ej. | head): salimos sin marcar muerto


def found_prompt():
    with _lock:
        return bool(PROMPT_RE.search("".join(_buf)))


def send_break(ser, width):
    """BREAK de hardware. width=0 usa el mínimo POSIX (~0.25s)."""
    ser.send_break(width)


# ── Parseo de argumentos ────────────────────────────────────
def parse_args(argv):
    if any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        sys.exit(0)

    port = argv[0] if len(argv) > 0 else None

    def num(idx, name, cast, default):
        if len(argv) <= idx:
            return default
        try:
            return cast(argv[idx])
        except ValueError:
            die(f"Argumento {name} inválido: {argv[idx]!r}")

    baud = num(1, "baud", int, 9600)
    duration = num(2, "duración", int, 120)
    width = num(3, "ancho-break", float, 0.0)

    if baud <= 0:
        die(f"baud debe ser positivo, no {baud}")
    if getattr(termios, f"B{baud}", None) is None:
        die(
            f"baud {baud} no soportado por termios. "
            "Comunes: 9600, 19200, 38400, 57600, 115200."
        )
    if duration <= 0:
        die(f"duración debe ser positiva (segundos), no {duration}")
    if width < 0:
        die(f"ancho-break no puede ser negativo, no {width}")
    return port, baud, duration, width


def _install_signal_handlers():
    """SIGTERM/SIGHUP -> KeyboardInterrupt, para que el finally limpie y
    restaure el puerto igual que con Ctrl-C."""
    def handler(signum, frame):
        raise KeyboardInterrupt
    for sig in (signal.SIGTERM, signal.SIGHUP):
        try:
            signal.signal(sig, handler)
        except (ValueError, OSError):
            pass  # p.ej. si no estamos en el hilo principal


# ── Main ────────────────────────────────────────────────────
def main():
    if sys.platform != "linux":
        print(
            f"AVISO: pensado para Linux; en {sys.platform!r} el BREAK/termios "
            "puede comportarse distinto.",
            file=sys.stderr,
        )

    port_arg, baud, duration, width = parse_args(sys.argv[1:])
    _install_signal_handlers()

    print("=" * 55)
    print("  ROMMON Break - unificado (break directo + autodetect)")
    print("=" * 55)

    port = pick_port(port_arg)

    try:
        ser = Serial(port, baud, timeout=0.3)
    except SerialError as e:
        die(str(e))

    print(f">>> CONECTADO a {port} @ {baud} 8N1")

    stop = threading.Event()
    dead = threading.Event()
    t = threading.Thread(target=reader, args=(ser, stop, dead), daemon=True)
    t.start()

    def guard():
        """Aborta si el hilo lector detectó que el puerto se cayó."""
        if dead.is_set():
            raise SerialError(f"{port} dejó de responder (¿USB o alimentación?).")

    try:
        # Fase 1: breaks pre-boot
        print("\n--- Fase 1: breaks pre-boot (5s) ---")
        print(">>> NO enciendas el equipo todavía")
        for _ in range(10):
            guard()
            send_break(ser, width)
            time.sleep(0.5)

        # Fase 2: breaks durante el arranque
        print("\n" + "=" * 55)
        print(">>> ¡¡¡ ENCIENDE / REINICIA EL EQUIPO AHORA !!!")
        print("=" * 55 + "\n")
        print("--- Fase 2: breaks durante boot ---")

        for i in range(1, duration + 1):
            if found_prompt():
                break
            guard()
            send_break(ser, width)
            time.sleep(0.8)
            if i % 5 == 0:
                ser.write(b"\r")  # despertar el prompt por si ya llegó
            print(f"\r  [break {i}/{duration}]", end="", flush=True)

        print()

        if found_prompt():
            print("\n" + "=" * 55)
            print(">>> ¡¡¡ ROMMON / BOOT MODE DETECTADO !!!")
            print("=" * 55)
            print("\nComandos útiles:")
            print("  # Router")
            print("  confreg 0x2142   - ignora startup-config al bootear")
            print("  confreg 0x2102   - registro de config normal")
            print("  reset            - reinicia")
            print("  boot             - arranca IOS")
            print("  # Switch")
            print("  flash_init       - inicializa flash")
            print("  dir flash:       - lista archivos")
            print("  boot             - arranca IOS")
            if sys.stdin.isatty():
                print("\nCtrl-C para salir.\n")
                interactive(ser, stop, dead)
            else:
                print("\n(stdin no es terminal: no entro a modo interactivo.)")
                print("Vuelve a correrlo en una terminal real para teclear en ROMMON,")
                print("o usa picocom:  picocom -b 9600 " + ser.port)
                _summary()
        else:
            print("\n>>> No se detectó prompt ROMMON.")
            print(">>> El equipo pudo haber booteado a IOS, o el break no llegó")
            print("    a tiempo. Repite y sincroniza el power-cycle con la Fase 2.")
            _summary()

    except SerialError as e:
        print(f"\n>>> Puerto perdido: {e}")
        _summary()
    except KeyboardInterrupt:
        print("\n\nInterrumpido.")
    finally:
        stop.set()
        time.sleep(0.3)
        ser.close()


def interactive(ser, stop, dead):
    """Sesión interactiva mínima: lo que escribas va al equipo; el hilo lector
    ya está imprimiendo lo que responde. Ctrl-C para salir."""
    try:
        while not dead.is_set():
            line = sys.stdin.readline()
            if not line:
                break
            try:
                ser.write(line.encode("ascii", errors="replace"))
            except SerialError as e:
                print(f"\n>>> Puerto perdido: {e}")
                break
    except KeyboardInterrupt:
        pass


def _summary():
    with _lock:
        full = "".join(_buf)
    print("\n--- Resumen ---")
    low = full.lower()
    if "rommon" in low:
        print("RESULTADO: ✅ ROMMON detectado")
    elif "switch:" in low:
        print("RESULTADO: ✅ Modo boot/switch detectado")
    elif "password:" in low:
        print("RESULTADO: ❌ Booteó a IOS (prompt de password)")
    elif ">" in full or "#" in full:
        print("RESULTADO: ⚠️  En IOS (user/enable mode)")
    else:
        print("RESULTADO: ❓ Estado desconocido")
    tail = full[-500:] if len(full) > 500 else full
    print("\nÚltimos 500 chars de consola:")
    print(tail)


if __name__ == "__main__":
    try:
        main()
    except SerialError as e:
        die(str(e))
    except KeyboardInterrupt:
        print("\nInterrumpido.")
