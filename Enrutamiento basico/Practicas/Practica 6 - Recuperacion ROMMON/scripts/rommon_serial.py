#!/usr/bin/env python3
"""
ROMMON break - método limpio.
Envía break continuamente con tcsendbreak() directo.
NO usa speed trick (crashea adaptadores FTDI).
"""
import serial
import sys
import time
import threading
import termios

PORT = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyUSB0"
BAUD = int(sys.argv[2]) if len(sys.argv) > 2 else 9600
DURATION = int(sys.argv[3]) if len(sys.argv) > 3 else 120

output_lines = []
lock = threading.Lock()

def reader(ser, stop_event):
    while not stop_event.is_set():
        try:
            data = ser.read(ser.in_waiting or 1)
            if data:
                text = data.decode("ascii", errors="replace")
                sys.stdout.write(text)
                sys.stdout.flush()
                with lock:
                    output_lines.append(text)
        except Exception:
            break

def check_rommon():
    with lock:
        full = "".join(output_lines).lower()
    return "rommon" in full or "switch:" in full or "loader>" in full

print("=" * 55)
print("  ROMMON Break - Método Limpio")
print(f"  Puerto: {PORT}  Baud: {BAUD}")
print("=" * 55)

try:
    ser = serial.Serial(PORT, BAUD, timeout=0.3)
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)

print(f"\n>>> CONECTADO a {PORT}")
print(">>> ¡¡¡ NO ENCIENDAS EL ROUTER TODAVÍA !!!")
print(">>> Enviando breaks pre-boot...")
print(">>> Enciende el router cuando veas 'ENCIENDE AHORA'\n")

stop = threading.Event()
t = threading.Thread(target=reader, args=(ser, stop), daemon=True)
t.start()

# Fase 1: Enviar breaks PRE-BOOT (5 segundos antes de encender)
print("--- Fase 1: Breaks pre-boot (5s) ---")
for i in range(10):
    try:
        # tcsendbreak directo - duración 0 = ~0.25s según POSIX
        termios.tcsendbreak(ser.fd, 0)
    except Exception:
        ser.send_break(duration=0.25)
    time.sleep(0.5)

print("\n" + "=" * 55)
print(">>> ¡¡¡ ENCIENDE EL ROUTER AHORA !!!")
print("=" * 55 + "\n")

# Fase 2: Breaks continuos durante boot (120 segundos)
print("--- Fase 2: Breaks durante boot ---")
for i in range(1, DURATION + 1):
    if check_rommon():
        print(f"\n\n{'=' * 55}")
        print(">>> ¡¡¡ ROMMON DETECTADO !!!")
        print(f"{'=' * 55}\n")
        break

    try:
        termios.tcsendbreak(ser.fd, 0)
    except Exception as e:
        print(f"\n>>> Error enviando break: {e}")
        break

    time.sleep(0.8)
    
    # Enviar Enter cada 5 intentos por si hay prompt
    if i % 5 == 0:
        ser.write(b"\r")

    print(f"\r  [Break {i}/{DURATION}]", end="", flush=True)

print("\n")

# Fase 3: Ver qué hay en la consola
print("--- Estado final ---")
ser.write(b"\r\n")
time.sleep(2)
ser.write(b"\r\n")
time.sleep(2)

with lock:
    full = "".join(output_lines)

# Buscar información relevante
print("\n--- Resumen ---")
if "rommon" in full.lower():
    print("RESULTADO: ✅ ROMMON detectado")
elif "switch:" in full.lower():
    print("RESULTADO: ✅ Modo Boot/Switch detectado")
elif "Password:" in full:
    print("RESULTADO: ❌ Router booteó a IOS - prompt de password")
elif ">" in full or "#" in full:
    print("RESULTADO: ⚠️  Router en IOS (user/enable mode)")
else:
    print("RESULTADO: ❓ Estado desconocido")

print(f"\nÚltimos 500 chars de la consola:")
print(full[-500:] if len(full) > 500 else full)

stop.set()
time.sleep(0.5)
ser.close()
