---
materia: Sistemas Operativos
semestre: 3
tipo: temario
fecha-examen: 2026-10-19
tags: [examen, parcial, sistemas-operativos]
---

# Temario — primer parcial de Sistemas Operativos

**Examen: lunes 19 de octubre de 2026.**

Abarca **solo lo visto en clase** hasta el 1 de octubre, la última clase con apuntes. Está armado con [[Sistemas Operativos/Notas en curso|Notas en curso]], las notas de concepto, los apuntes de agosto (`Sistemas Operativos Parcial 1.odt`) y la Práctica 1.1. Los libros (Tanenbaum y Silberschatz) y la investigación de [[Concurrencia y paralelismo]] se usan solo como referencia, para verificar datos o rellenar un hueco. Cuando algo sale de un libro, se cita con su página.

Preguntas para ponerte a prueba: [[Banco de preguntas - parcial 1]].

## Lo que entra

Numeración y nombres del programa oficial ![[PE Sistemas Operativos 2022.pdf]], que tiene 13 temas. En clase se ha llegado hasta el 10.

| # | Tema del programa | Clase | Estado |
|---|---|---|---|
| 1 | Introducción a los SO | 17 ago | Completo |
| 2 | Historia | 17 ago | Completo; ⭐ multiprogramación y spooling |
| 3 | Tipos de SO | 20 ago | Completo; los mainframes se rellenan desde el libro; ⚠️ simétrico/asimétrico corregido |
| 4 | Capas o subsistemas | — | Completo, con lo básico de procesos y memoria |
| 5 | Consideraciones para la instalación | Práctica 1.1, entrega 3 sep | ⚠️ Teoría no capturada; va lo de la práctica |
| 6 | Dispositivos de E/S | — | Completo |
| 7 | Concurrencia y paralelismo | — | Versión compacta; ⚠️ vídeo de clase sin revisar |
| 8 | Interfaces de usuario | — | Completo; la parte de GUI es escueta |
| 9 | Manejo de usuarios | 10, 14 y 17 sep | Completo; ⚠️ falta la 3.ª forma de iniciar sesión |
| 10 | Sistema de archivos | 28 sep y 1 oct | Lo visto en clase |

**No entra:** el resto del programa, que no se ha visto. Son los temas 11 (procesos a fondo), 12 (comunicación entre procesos) y 13 (memoria y almacenamiento), y los subtemas del 10 que no salieron en clase (rutas, operaciones con archivos y directorios, gestión de espacio, protección).

«—»: la nota no tiene fecha de clase.


## 1. Introducción a los sistemas operativos

Ver [[Definicion y funciones del sistema operativo]].

| Fuente           | Definición                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Tanenbaum**    | Software que actúa como intermediario entre el usuario y el hardware, *gestionando los recursos de los equipos*           |
| **Silberschatz** | Programa que administra los recursos y *proporciona servicios para facilitar la ejecución de los programas de aplicación* |
| **El profesor**  | Programa que administra la ejecución de otros programas y gestiona los recursos del dispositivo                           |

Las tres coinciden en el núcleo: **administrar recursos**. Difieren en el énfasis — Tanenbaum en la intermediación, Silberschatz en el servicio a las aplicaciones.

- **Funciones esenciales:** administrar CPU, gestionar memoria, gestionar archivos, gestionar dispositivos, gestionar procesos, proporcionar interfaz de usuario, **proteger recursos** (de usuarios y de otros programas).
- **Características:** facilidad de uso (las GUI son las más sencillas), gestión de recursos, multitarea, seguridad, estabilidad, eficiencia, capacidad de evolución, **portabilidad** (adaptarse a distinto hardware).
- **Componentes:** **kernel** (el más importante, capa más interna, en contacto directo con el hardware), **capa de usuario** (interfaz GUI o CLI, aplicaciones, librerías) y **hardware**. Dicho con el otro esquema visto en clase: **shell** (interfaz de usuario) — **kernel** (comunicación hardware/software) — **hardware**.

## 2. Historia: generaciones de sistemas operativos

Ver [[Generaciones de sistemas operativos]].

Clasificación de cinco generaciones según **Tanenbaum y Herbert Bos**; fechas referenciales.

| Generación | Años | Hardware | Hitos del SO |
|---|---|---|---|
| 1ª | 1945–1955 | Tubos de vacío | No había sistema operativo; todo en lenguaje máquina, directo sobre el hardware |
| 2ª | 1955–1965 | Transistor (sustituye al tubo de vacío); mainframes | **Sistemas por lotes** — antecesor del SO actual; código en FORTRAN/ensamblador en tarjetas perforadas |
| 3ª | 1965–1980 | Circuitos integrados | ⭐ **Multiprogramación**, ⭐ **spooling**, tiempo compartido; interfaces CLI; el SO ya administra recursos de forma compleja |
| 4ª | 1980–1990 | Circuitos más pequeños; primer microprocesador Intel 8080 (1974) | Computadoras personales; primeros SO de PC (DOS, MS-DOS, Windows, Linux, UNIX, BSD); nacen las **interfaces gráficas** *user friendly*; las PC empiezan a conectarse en red |
| 5ª | 1990–actualidad | — | Dispositivos móviles, comunicación inalámbrica; nacen **Android**, **iOS** y **HarmonyOS** |

- ⭐ **Multiprogramación:** técnica que permite tener varios trabajos cargados en **memoria** a la vez; evolución del procesamiento por lotes.
- ⭐ **Spooling:** técnica que permite leer y almacenar los trabajos de las tarjetas directamente en el **disco**, en lugar de cargarlos en memoria principal.
- **Tiempo compartido:** variante de la multiprogramación para que varios usuarios usen la computadora de forma interactiva, compartiendo recursos por turnos.

> Diferencia clave entre los dos temas de examen: **multiprogramación** carga varios trabajos en *memoria*; **spooling** los almacena en *disco*.

> ⚠️ **No mezclar con Organización de computadoras.** La numeración de generaciones de SO no coincide con la numeración de generaciones de hardware: la 3ª generación de SO (1965–1980, circuitos integrados / multiprogramación / spooling) cae dentro de lo que la cronología de hardware cuenta como parte de su **4ª** generación. Son dos líneas de tiempo distintas con criterios distintos — no usar los números de una para la otra en el examen.

## 3. Tipos de sistemas operativos

Ver [[Tipos de sistemas operativos]].

Tres criterios de clasificación: **1)** según el tipo de sistema informático, **2)** según servicios y capacidades, **3)** según su estructura interna.

### 1. Según el tipo de sistema informático

- **Mainframes** ⚠️ (hueco de la nota de clase, rellenado desde el libro): son las computadoras de gran tamaño de los centros de datos corporativos; su diferencia frente a una PC está en la capacidad de E/S (una mainframe con miles de discos no es inusual). Ofrecen típicamente tres servicios: **procesamiento por lotes**, **procesamiento de transacciones** (grandes volúmenes de peticiones pequeñas, p. ej. cheques bancarios) y **tiempo compartido**. Hoy se reemplazan gradualmente por variantes de UNIX como Linux (Tanenbaum, p. 64).
- **SO de servidor:** dan servicio a otras computadoras por red; multiusuario, multitarea, escalables, orientados a red; para cargas intensas; diseñados para **nunca apagarse**; muy robustos en seguridad.
- **SO de escritorio:** Windows, distribuciones Linux, BSD, sistemas Apple; uso personal, interfaces *user friendly*, con tiendas de aplicaciones.
- **SO móviles:** smartphones y tabletas; movilidad y conectividad inalámbrica, pantallas táctiles, aprovechan GPS/cámara/acelerómetro; limitación característica: la **batería**.

| SO móvil | Kernel | Uso |
|---|---|---|
| Android | Linux | Smartphones, tabletas |
| iOS | Darwin (UNIX) | Dispositivos Apple |
| HarmonyOS | Microkernel HongMeng | Huawei |
| Tizen OS | Linux | Smart TV |
| Xiaomi HyperOS | — | Smart bands |
| Roku | Linux | Smart TV |
| Android Automotive OS | Linux | Automóviles |

- **SO embebidos:** para hardware especializado (microondas, refrigeradores, sistemas médicos), corren en microcontroladores más que en procesadores; poco almacenamiento, un solo uso, no suelen cambiar de SO. **Embedded Linux** (cámaras, routers, smart TVs, ~2 MB de instalación típica), **OpenWRT** (routers/redes), **TinyOS** (sensores IoT).

### 2. Según servicios y capacidades

- **Tiempo real:** respuesta predecible en tiempo y forma. **Duro:** respuesta obligatoria en una ventana mínima (fallo = riesgo de vidas o pérdidas millonarias). **Blando:** admite un pequeño retraso; suele convivir con otro sistema dentro del mismo dispositivo (ej.: en un auto, bolsas de aire/frenos = tiempo real duro; infoentretenimiento = sistema aparte).
- **Por número de usuarios:** **monousuario** (un usuario a la vez, sin importar núcleos o tareas — ojo: monousuario *comercial* no implica kernel incapaz de ser multiusuario, p. ej. Windows Server) / **multiusuario** (atiende peticiones de varios usuarios a la vez, cada uno con su shell, procesos, permisos y memoria propios, de forma concurrente).
- **Por número de tareas:** **monotarea** (una sola tarea acapara el procesador) / **multitarea** (varias tareas "al mismo tiempo", según el manejo de la [[Concurrencia y paralelismo|concurrencia]]).
- **Por número de procesadores:** **monoprocesador** / **multiprocesador**, este último con dos técnicas: **asimétrica** (un procesador "maestro" dirige a los demás, "esclavos") y **simétrica** (el SO dirige a todos los procesadores por igual, sin maestro ni esclavos).

  > ⚠️ **Corregido.** El apunte tiene los nombres al revés: llama *simétrica* a la de maestro-esclavo y *asimétrica* a la de todos iguales. En Tanenbaum el modelo maestro-esclavo es el asimétrico, y el SMP (*multiprocesador simétrico*) «elimina esta asimetría»: cualquier CPU puede ejecutar el SO, sin maestro (Tanenbaum, p. 566). Si el profesor lo dictó así, confírmalo con él antes del examen.

### 3. Según su estructura interna

| | Qué incluye en el kernel | Dónde vive el resto | Compromiso |
|---|---|---|---|
| **Monolítico** | Planificador, gestión de memoria, sistema de archivos, drivers, pila de red, IPC, interrupciones, system calls — todo dentro | — | Rápido y eficaz, pero si algo falla, falla todo el kernel. Así funciona Linux |
| **Microkernel** | Solo lo mínimo: IPC, planificación básica de CPU, gestión mínima de memoria, manejo básico de interrupciones/HAL | Sistema de archivos, drivers, pila de red, gestión de procesos de alto nivel, autenticación — cada uno como proceso de usuario | Más estable (un fallo no tira todo el kernel), pero con más overhead de comunicación |
| **Híbrido** | Lo crítico para rendimiento | Lo no esencial (controladores, sistemas de archivos) en espacio de usuario | Combina el alto rendimiento del monolítico con la modularidad del microkernel. Kernel de Windows XP/7/10/11 y servidores; XNU (macOS, iOS); ReactOS, BeOS |

## 4. Capas o subsistemas de un sistema operativo

Ver [[Capas de un sistema operativo]], [[Gestion de procesos]] y [[Gestion de memoria]].

Un SO se reduce en clase a **ocho subsistemas**:

| Subsistema                    | Función esencial                                                                                                                                                                  |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kernel o núcleo**           | El corazón del sistema; el resto de capas se construye sobre él o dentro de él según sea monolítico/microkernel                                                                   |
| **Entrada y salida**          | Periféricos, tarjetas gráficas/de red, almacenamiento secundario (no el CPU ni la memoria principal) — ver [[Dispositivos de entrada y salida]]                                   |
| **Gestión de procesos**       | Inicializa/pausa/reanuda/cierra procesos; comunicación y sincronización (pipelines, mensajes, memoria compartida, sockets); gestiona deadlock; asigna ráfaga de CPU; planificador |
| **Gestión de memoria**        | Asignar y limpiar espacios de memoria; memoria virtual; saber quién usa qué; proteger de accesos no autorizados; su componente de hardware es la **MMU**                          |
| **Almacenamiento secundario** | Quién/cuándo/cómo accede a memoria persistente; espacio libre/ocupado; planificación de disco                                                                                     |
| **Sistema de archivos**       | Crear/eliminar/leer/modificar archivos; administrar directorios; búsqueda; protección de archivos críticos                                                                        |
| **Redes y comunicaciones**    | TCP/IP, enviar/recibir paquetes, administrar la tarjeta de red, gestionar conexiones; protección en las comunicaciones                                                            |
| **Interfaz de usuario**       | Puente GUI/CLI entre SO y usuario: recibe input, da output, gestiona ventanas, notificaciones y errores                                                                           |

### De la capa de procesos: proceso, ráfaga, quantum, cambio de contexto

Ver [[Gestion de procesos]].

- **Proceso:** programa en ejecución.
- La **multiprogramación** permitió que un CPU ejecutara varias tareas de forma simultánea mediante **cambio de contexto**, repartiendo el procesador por **quantums** de tiempo.
- **Quantum:** cantidad de milisegundos que el CPU puede dar a una tarea.
- **Cambio de contexto:** el momento en que se cambia de una tarea a otra durante la multiprogramación; al volver a una tarea, la reanuda **desde donde se quedó**.
- Ver también la tabla concurrencia/paralelismo en la sección 7.

### De la capa de memoria: memoria virtual, paginación, MMU

Ver [[Gestion de memoria]].

- **Memoria virtual:** no es una cosa física, sino un **concepto**/ilusión que crea el SO para que los programas no "se pisen" al escribir en memoria; si la memoria real se agota, el SO puede asignar espacio de memoria secundaria.
- **Paginación:** la **técnica** con la que se logra la memoria virtual — el SO da a cada proceso un "mapa de apodos" (mapa virtual) propio, haciéndole creer que tiene toda la memoria para él solo y de forma secuencial. El proceso usa esos apodos sin saber la dirección física real.
- **MMU** (unidad de gestión de memoria): componente de **hardware dentro de la CPU** que traduce esos apodos a direcciones físicas reales; existe para **bajar la carga lógica del CPU** (evitarle millones de traducciones manuales).

## 5. Consideraciones para la instalación de un sistema operativo

Ver [[Reporte de instalacion de un sistema linux maquina virtual]] y ![[1.1 Instalacion de un sistema operativo - instrucciones.pdf]].

> ⚠️ La teoría de este tema no se capturó: los apuntes se cortan en el encabezado «Consideraciones para instalación», tanto en [[Sistemas Operativos/Notas en curso|Notas en curso]] como en el `.odt` de agosto. Aquí va lo trabajado en la **Práctica 1.1** (Debian 13 en máquina virtual, entrega 3 sep). Conviene pedir los apuntes o las diapositivas de esa clase.

- **Requisitos del enunciado:** 30–50 GB de disco, procesador de 4 núcleos, 1–2 GB de RAM, 1 adaptador de red, **soporte de virtualización** activo, ISO completa de Debian 13.6.0, internet opcional.
- **Hipervisor:** el enunciado pide uno de **tipo 2**, preferentemente VirtualBox. Tú usaste **QEMU/KVM con virt-manager**, que ya venía en tu Debian *bare metal*.

| | Tipo 1 | Tipo 2 |
|---|---|---|
| Dónde corre | Directo sobre el hardware; en la práctica es el propio SO, el único programa en modo kernel | Como programa de usuario sobre un SO anfitrión |
| Ejemplo | KVM (integrado en el kernel Linux) | VirtualBox |

> Tanenbaum, p. 600. En tu reporte justificas que KVM actúa como tipo 1, aunque en el uso diario se siente igual que uno de tipo 2.

- **Máquina virtual creada:** instalación manual → Debian 13 → 2048 MiB de RAM y 2 vCPU (el enunciado pedía 4 núcleos) → disco de 50 GiB `qcow2` → red NAT.
- **Instalación de Debian:** idioma español, teclado latinoamericano, contraseña de **root** y usuario normal, zona horaria, red.
- **Particionado manual, esquema MBR:**

| Punto de montaje | Tamaño | Sistema de archivos | Tipo de partición |
|---|---|---|---|
| `/` | 25 GB | ext4 | Primaria |
| `/home` | 21 GB | ext4 | Lógica |
| `swap` | 7.7 GB | — | Lógica |

- **Selección de software:** sin entorno gráfico, solo utilidades estándar del sistema y **SSH**. **GRUB** instalado en el disco principal.
- **Post-instalación (las 7 tareas del reporte):** actualizar (`apt update && apt full-upgrade`), configurar `sudo`, instalar `qemu-guest-agent`, verificar controladores virtio, verificar la red, endurecimiento básico (sin login de root por SSH, firewall, `unattended-upgrades`) y hacer un snapshot.

## 6. Dispositivos de entrada y salida

Ver [[Dispositivos de entrada y salida]].

- Dispositivos capaces de recibir input del usuario para el SO, o de dar output hacia el usuario: mouse, teclado, almacenamiento secundario, bocinas, pantalla, tarjeta gráfica, tarjeta de red.
- Cada dispositivo tiene **componente físico** (lo tocable) y **componente lógico** (chip/tarjeta con su propia lógica, controlador y a veces memoria/búferes).

| Clasificación | Tipo | Ejemplos |
|---|---|---|
| Por forma de transferencia (legacy) | **De bloque** (datos en tamaño fijo) | Almacenamiento |
| | **De carácter** (byte por byte) | Teclado, mouse |
| Por función (actual) | **De entrada** | Teclado, mando, mouse |
| | **De salida** | Pantallas, bocinas |
| | **De entrada/salida** | Tarjetas gráficas, discos |

- Comunicación con el SO mediante **drivers (controladores)**, dentro del componente lógico.
- **Registros E/S:** de **control** (el CPU escribe/lee comandos), de **datos** (donde se lee/escribe la información) y de **estado** (suspendido, ocupado, encendido, listo, error).
- **Puertos/direcciones E/S:** puente entre el dispositivo y el SO; dan a cada registro una dirección única para que el SO sepa con quién habla.

## 7. Concurrencia y paralelismo

Ver [[Gestion de procesos]] y [[Capas de un sistema operativo]].

> ⚠️ Este tema quedó marcado en clase como "buscar". Se da aquí la definición precisa de concurrencia y paralelismo desde Tanenbaum, y se mantienen solo los conceptos extra que aparecen explícitamente en las notas de clase (multiprogramación, quantum, cambio de contexto). No se incluyen deadlock, semáforos ni los problemas clásicos de sincronización porque no aparecen en los apuntes de clase — sí están investigados en [[Concurrencia y paralelismo]], pero esa nota es una investigación externa del alumno, no apunte de clase.

| | Qué ocurre | Qué hace falta |
|---|---|---|
| **Paralelismo** | Dos o más procesos se ejecutan **exactamente al mismo tiempo** | Varios procesadores, o varios núcleos de un procesador |
| **Concurrencia** | Dos o más procesos se ejecutan uno por uno, con un cambio de contexto tan rápido que da la **ilusión** de paralelismo | Un solo núcleo basta |

- **Definición precisa de concurrencia** (Tanenbaum, p. 113): los procesos son una de las abstracciones más importantes de un SO porque dan la capacidad de operar (pseudo)concurrentemente aun con una sola CPU disponible — convierten una CPU en varias CPU virtuales.
- **Definición precisa de paralelismo** (Tanenbaum, p. 114): en cualquier sistema de multiprogramación, la CPU en sentido estricto ejecuta solo un proceso a la vez, conmutando con rapidez entre varios y dando la apariencia de un paralelismo (**pseudoparalelismo**), que se distingue del **paralelismo real de hardware** de los sistemas multiprocesador con dos o más CPUs que comparten la misma memoria física.
- **Multiprogramación:** ver sección 2 (⭐ tema de examen) — varios trabajos cargados en memoria a la vez.
- **Quantum y cambio de contexto:** ver sección 4 — el quantum es el tiempo de CPU asignado por turno; el cambio de contexto es la conmutación entre tareas. Definición de refuerzo (Tanenbaum, p. 57): en un sistema de multiprogramación, cambiar de un programa a otro (cambio de contexto o *context switch*) puede exigir vaciar bloques modificados de la caché y actualizar los registros de la MMU — operación costosa que los programadores procuran evitar.

> ⚠️ Existe un vídeo de clase, `Concurrencia y paralelismo.mp4`, que no fue revisado para armar esta sección. Puede contener contenido dado en clase que no quedó capturado en las notas escritas — revisar antes del examen si el tiempo lo permite.

## 8. Interfaces de usuario

Ver [[CLIs y shells]] e [[Interfaces graficas]].

- **GUI** (*Graphic User Interface*): interfaz visual, con botones, que elimina la necesidad de comandos — la más común para usuarios finales.
- **NUI** (*Natural User Interface*): elimina el uso de periféricos, se apoya en movimientos naturales (manos, brazos, dedos, voz).
- **Terminal (consola):** originalmente un dispositivo físico de teclado y pantalla/papel que solo envía y recibe texto sin interpretarlo; en Linux, las consolas virtuales (tty1, tty2…) que da el kernel.
- **Emulador de terminal:** programa que emula una terminal física dentro de un entorno gráfico; dibuja el texto y captura el teclado, se comunica con la shell por una pseudoterminal (pty); **no ejecuta comandos por sí mismo**.
- **Shell (intérprete de comandos):** toma la cadena de texto, la divide, expande variables/comodines/redirecciones/pipes, revisa si es alias/función/builtin y si no, busca el programa en el `PATH` y lo ejecuta. En uso coloquial, "shell" se usa de forma general para casi cualquier CLI o terminal, aunque no sea del todo correcto.
- **POSIX:** estándar/convención al que se llegó para que los distintos shells manejen la misma terminología y comandos, dando una experiencia similar al usuario final entre shells distintos.

| Shell | Cercanía a POSIX | Rasgo principal |
|---|---|---|
| **BASH** (Bourne Again Shell) | Implementa el estándar POSIX | El más usado en Linux; fuerte en scripting; muy documentado y retroactivo desde los 80 — "si no está roto, no lo reemplaces" |
| **ZSH** | De la familia POSIX, con diferencias que lo alejan un poco | Muy personalizable; estándar en macOS y en Kali |
| **FISH** | Se aleja del estándar POSIX | Interactivo y cómodo desde el primer uso, poca configuración; no recomendado para scripting de sistema |
| **KSH** (Korn Shell) | Pionero en POSIX | Código antiguo, liberado en 2000 tras salir de AT&T; uso relegado a sistemas heredados |
| **TCSH** | Se aleja de POSIX (scripting al estilo C) | Uso relegado a sistemas/código heredado |

> ⚠️ `Interfaces graficas.md` es casi un esqueleto en las notas de clase (solo define GUI y NUI); no se infla aquí con contenido que no se vio.

## 9. Manejo de usuarios

Ver [[Sistemas Operativos/Notas en curso|Notas en curso]], [[Usuarios y gestion de usuarios]] y [[Usuarios y su gestion]].

### 10 de septiembre — definición y funciones

- **Usuario:** entidad (persona, proceso o dispositivo) que interactúa con la computadora y posee una **identidad digital** propia; esa identidad determina permisos, privilegios y nivel de acceso.
- Se identifica con **nombre de usuario** (+ contraseña en la mayoría de los casos) y, internamente, con un **número único** (UID de usuario, y GID de grupo).
- **Autenticación**, según tres principios (visto también en Introducción a la ciberseguridad):
  - Algo que **sabe** (contraseña, PIN).
  - Algo que **es** (biometría).
  - Algo que **tiene** (token, tarjeta).
  > Tanenbaum llama a esto los "tres principios generales" para autenticar usuarios (Tanenbaum, p. 672).
- **Por qué importa:** una mala gestión de usuarios es un agujero de seguridad que permite accesos no autorizados o compromete recursos del sistema.
- **Funciones del SO frente a los usuarios:**
  - **Control de acceso y autenticación:** validar quién entra (contraseñas).
  - **Asignación de propiedad:** marcar qué archivos/carpetas/configuraciones pertenecen a cada perfil para que nadie más los modifique sin permiso.
  - **Aislamiento de procesos:** los programas de un usuario no interfieren ni espían los de otro usuario en el mismo equipo.
  - **Auditoría y registro:** guardar en el historial qué acciones hizo cada entidad.
  - Administrar servicios de red.
- Cada usuario autorizado recibe un **UID** asignado por el administrador; los procesos heredan el UID de quien los lanzó (Tanenbaum, p. 69). El **superusuario** (UID 0 en Linux) tiene poder especial y puede saltarse casi todas las reglas de protección (Tanenbaum, pp. 69 y 834).

### 14 de septiembre — tipos de usuario, servicios, archivos de configuración, comandos

- **Tipos de usuario en Linux** (niveles distintos de acceso, permisos y privilegios):

| Tipo | Rasgos |
|---|---|
| **Administrador / superusuario (root)** | Privilegios más altos: instalar programas, modificar configuración, crear/eliminar usuarios, administrar permisos. Solo él instala actualizaciones/paquetes o borra ciertos directorios y archivos. Prompt `#` |
| **Estándar / normal** | El que inicia sesión normalmente; usa apps y sus archivos, restringido en el resto. Lo crea el superusuario sin problema. Usuario + contraseña. Prompt `$`. Tiene workspace propio `/home/usuario` y un **UID** |
| **Invitado** | Un estándar con permisos aún más limitados, para accesos temporales |
| **De sistema / especial** | Usuarios "lógicos" (sin login, sin contraseña), muy ligados a los **daemons**; UID típicamente entre 1 y 100 |

- **Usuarios de servicio:** al inicializar un servicio se crea un usuario especial para él. Ejemplos de la clase:
  - **Apache** (web, puerto 80).
  - **MySQL** (base de datos, puerto 3306).
  - Así, si el servicio se vulnera, el atacante solo puede hacer lo que ese usuario de servicio puede hacer (aislamiento de permisos).
- **Grupo:** expresión lógica para reunir usuarios con características en común.
- **Archivos de configuración de usuarios/grupos/contraseñas:**

| Archivo | Contenido |
|---|---|
| `/etc/passwd` | Información básica y **pública** de las cuentas |
| `/etc/shadow` | Contraseñas cifradas (hash), de forma segura |
| `/etc/group` | Define los grupos del sistema, para compartir permisos de archivos/directorios |

- **Tabla de comandos de usuarios y grupos:**

| Comando | Qué hace |
|---|---|
| `useradd` | Agrega usuario; de **bajo nivel**, no interactivo |
| `adduser` | Agrega usuario; script de **alto nivel**, interactivo |
| `passwd usuario` | Agrega/cambia la contraseña (el usuario ya debe existir). Root puede cambiar la de cualquiera; un usuario normal, solo la suya |
| `usermod` | Cambia grupo, comentarios, directorio de trabajo, nombre de login o shell por defecto |
| `userdel usuario` | Borra la cuenta de `passwd`/`shadow`, **conserva** su directorio de trabajo |
| `userdel -r usuario` | Elimina **todo**: cuenta y directorio/archivos |
| `userdel -f usuario` | Fuerza el borrado aunque el usuario esté trabajando en el sistema; radical, puede causar inestabilidad |
| `groupadd nombre` | Crea un grupo |
| `groupdel nombre` | Elimina un grupo |
| `groupmod -n nuevoNombre antiguoNombre` | Renombra un grupo |
| `usermod -aG grupo usuario` | Añade (`-a`, *append*) el usuario a un grupo adicional sin quitarlo de los demás |
| `gpasswd -d usuario grupo` | Saca al usuario de ese grupo |

### 17 de septiembre — permisos

- Los **permisos** son un mecanismo de seguridad que controla qué acciones puede realizar un usuario, proceso o programa sobre un recurso.
- Tres pilares para evaluarlos: **sujeto** (quién quiere hacer algo), **objeto** (el recurso) y **acción** (cómo).
- Los tres permisos básicos en Linux: **r**ead, **w**rite, e**x**ecute (Tanenbaum, p. 74, los llama "bits rwx").
- Se aplican a tres categorías: **propietario** del archivo, **grupo** (usuarios con rol similar) y **otros** (cualquier otra cuenta del sistema).
- `ls -l` muestra atributos, permisos y propietario de un archivo o directorio. Captura de la clase:

  ![[Pasted image 20260917092250.png]]
- **Octal:** cada permiso rwx vale `r=4, w=2, x=1`; se suman por categoría. Tres cifras: propietario, grupo, otros (Tanenbaum confirma el mismo esquema de 9 bits en grupos de 3, p. 833).
- `chmod` agrega o quita permisos:
  - Octal: `chmod 755 archivo` deja `rwxr-xr-x` (Tanenbaum, p. 835).
  - Simbólico: `u/g/o/a` (usuario/grupo/otros/todos) + `+`/`-` + `r/w/x` + archivo. Ej.: `chmod g+w archivo`, `chmod o-r archivo`.
- **Permisos de grupo**, procedimiento de la clase:
  1. Crear el grupo: `sudo groupadd licic`.
  2. Vincular el archivo/carpeta al grupo (cambia el propietario de grupo): `sudo chown :licic /ruta/elemento`.
  3. Asignar los permisos al directorio (con `chmod`).

### Inicio de sesión

> El apunte dice "existen 3 formas de iniciar sesión" pero solo lista dos: de forma gráfica y a través de CLI.

- ⚠️ No se encontró en Tanenbaum ni Silberschatz una lista explícita y cerrada de "3 formas de iniciar sesión en un SO" que resuelva cuál es la tercera — solo aparecen menciones sueltas (p. ej. "inicio de sesión remoto" como uno de los seis tipos de servicio de red, Tanenbaum p. 618). **Preguntar al profesor cuál es la tercera forma**; no se inventa aquí. Candidata razonable sin confirmar: acceso remoto (SSH/red).

## 10. Sistema de archivos

Ver [[Sistemas Operativos/Notas en curso|Notas en curso]].

### 28 de septiembre — definición, funciones, metadatos, tipos y capas

- **Qué es:** uno de los subsistemas del SO (no confundir con la gestión de almacenamiento secundario); conjunto de estructuras, métodos y mecanismos que el SO usa para organizar, almacenar, gestionar, leer, modificar y recuperar información de forma lógica y estructurada en un dispositivo de almacenamiento (disco, SSD, USB). Permite organizar los datos en archivos, carpetas y directorios para localizarlos y acceder a ellos.
- **Funciones:**
  - Organizar archivos.
  - Permitir copiar, pegar, eliminar archivos.
  - Mostrar las rutas de los archivos.
  - Controlar el acceso a los archivos.
  - Gestionar el espacio de almacenamiento (asignar y liberar según necesidad).
  - Permitir el uso compartido de archivos entre usuarios y procesos autorizados.
- **Metadatos que mantiene por archivo:** dónde está almacenado, cuánto espacio ocupa, tamaño/tipo, si está en uso (tabla de archivos), fecha de creación/modificación, permisos de acceso, identificadores de acceso.
- **Tabla comparativa de sistemas de archivos vistos en clase:**

| Sistema | Para / origen | Tamaño máx. de archivo | Tamaño máx. de partición | Journaling | Rasgo distintivo |
|---|---|---|---|---|---|
| **FAT32** | Microsoft, 1996 (sucesor de FAT16/FAT12); USB, SD, multimedia de auto/TV | 4 GB | Tanenbaum: hasta 2 TB en teoría (Tanenbaum, p. 936); el apunte añade que en la práctica el formateo de Windows limita a 32 GB | No | Ligero, compatibilidad casi universal, sin permisos ni cifrado nativos |
| **exFAT** | Microsoft, 2006, para Windows Embedded; ahora libre, Linux la soporta de forma nativa | ~16 EB teóricos | ~128 PB teóricos | No | Sucesora de FAT32 sin el límite de 4 GB; estructura simple, no desgasta memorias flash; sin permisos locales ni cifrado nativo como NTFS/ext4 |
| **NTFS** | Microsoft, 1993 (Windows NT 3.1); llega al usuario doméstico con Windows XP (2001) | 16 TB teóricos | 256 TB | Sí | Usa **MFT** (tabla maestra de archivos); permisos y cifrado nativo; compatibilidad limitada con macOS/Linux |
| **ext4** | Linux, 2008 (familia ext2→ext3→ext4) | 16 TB | 1 EB | Sí | Usa **inodos** y *extents* (reduce fragmentación); eficiente en CPU; sin soporte nativo en Windows/macOS |
| **APFS** | Apple, 2017 (macOS High Sierra) | — | — | No (usa *redirect-on-write*) | Pensado para SSD/flash; clonación instantánea y snapshots; solo ecosistema Apple, rinde peor en HDD |

  > El apunte dice que NTFS es «de Microsoft desde el 93 con Windows XP». Son dos fechas distintas: NTFS nace en 1993 con Windows NT 3.1, y Windows XP (2001) es el que lo lleva a los equipos domésticos.

  > El apunte original llama a exFAT **"EXTFAT32"**. Por el contexto (creado en 2006 para Windows Embedded, sucesor de FAT32, sin el límite de 4 GB, hasta 16 EB teóricos de archivo) es claramente **exFAT**, no un sistema llamado "EXTFAT32" (ese nombre no existe). Se corrige aquí dejando constancia; el resto del contenido del apunte sobre este sistema se conserva.

- **Estructura en capas de un sistema de archivos** (de alto a bajo nivel; separa funciones para reducir complejidad y facilitar mantenimiento):

| Capa | Función |
|---|---|
| **Aplicación de usuario** | Inicia la acción mediante llamadas al sistema (`open`, `read`, `write`, `close`); no es parte interna del sistema de archivos |
| **Archivo lógico** | Maneja la estructura conceptual: directorios, nombres, permisos de lectura/escritura, metadatos y bloques de control de archivo (FCB) |
| **Módulo de organización de archivos** | Puente entre lo lógico y lo físico: sabe cómo están asignados los archivos en el almacenamiento, rastrea espacio libre y decide dónde colocar datos nuevos |
| **Sistema de archivos básico** | Emite comandos genéricos al hardware para leer/escribir bloques físicos; administra buffers y caché en RAM |
| **Control de E/S** | Nivel más bajo del software: drivers y controladores de interrupciones; traduce comandos abstractos a instrucciones de hardware |
| **Hardware** | El componente físico donde residen los datos; traduce pulsos eléctricos a almacenamiento real |

- **Clasificación según dónde se almacenan los datos:**
  - **Locales (de disco):** interactúan directamente con el hardware físico (discos internos, almacenamiento mecánico).
  - **En red (distribuidos):** no controlan nada físicamente; usan un protocolo para que el SO "crea" que un directorio remoto está montado localmente (NFS, SMB/Samba, SSHFS — ver tabla abajo).
  - **Virtuales/especiales:** no se montan sobre un medio físico ni de red; existen solo en RAM o mientras corre un proceso (`/proc`, `/dev`, el registro de Windows).
- **Archivo:** conjunto de datos que representa algo (fotos, documentos, binarios); el medio se divide en bloques de longitud fija y el sistema de archivos asigna un número de bloques a cada archivo.
- **Directorio:** contenedor virtual para administrar archivos y subdirectorios (las "carpetas" de las GUI); organiza, localiza y da estructura de árbol a partir de un directorio raíz.

### 1 de octubre — sistemas de archivos de red

| | **SMB/Samba** | **NFS** | **SSHFS** |
|---|---|---|---|
| **Origen** | Samba: 1992, implementación libre del protocolo SMB de Microsoft para Unix/Linux | 1983, Sun Microsystems, nativo de Unix/Linux | Suite basada en SSH + SFTP |
| **Uso típico** | Redes domésticas y de oficina; forma nativa de Windows para compartir archivos/impresoras; puede actuar como controlador de dominio (Active Directory) | Centros de datos, clústeres, NAS corporativo, servidor-servidor Linux | Montar carpetas remotas (servidor web, Raspberry Pi) para edición en tiempo real o mantenimiento |
| **Modelo** | Dos demonios: **smbd** (transferencia, autenticación, permisos) y **nmbd** (resolución de nombres de red) | Cliente-servidor, usa RPC sobre un único puerto TCP; independiente del sistema de archivos subyacente | FUSE (captura la operación) → cliente SSHFS/SFTP (traduce a SFTP) → servidor SSH/SFTP remoto (ejecuta y responde) |
| **Seguridad/cifrado** | Compatibilidad universal, pero más sobrecarga de red que NFS | Manejo nativo de permisos Unix; integración con Windows compleja | Cifrado extremo a extremo (AES, ChaCha20…), hereda toda la seguridad de SSH; usa el puerto 22, atraviesa firewalls fácilmente |
| **Rendimiento** | Mayor sobrecarga de red | Muy rápido y eficiente, ideal para archivos grandes entre Linux | Más lento que NFS/Samba (cifra/descifra todo); sensible a la latencia |
| **Configuración** | Se ve directo en el explorador de archivos | — | Sin configuración en el servidor si ya acepta SSH; un solo paso en el cliente |

> Todos se ven en clase como ejemplos de sistemas de archivos **en red/distribuidos**, dentro de la clasificación de la sección anterior.

## ⭐ Marcado por el profesor como «tema de examen»

> Multiprogramación y spooling (3.ª generación).

- **Multiprogramación:** varios trabajos cargados en **memoria** a la vez; mientras uno espera E/S, la CPU atiende a otro.
- **Spooling:** los trabajos se leen de las tarjetas y se guardan en **disco**, para cargarlos después sin esperar al lector.
- Una frase: *la multiprogramación carga en memoria; el spooling almacena en disco.*

## Pendientes antes del examen

- [ ] **Preguntar al profesor** qué abarca el parcial: ¿hasta sistema de archivos? ¿Entra lo que se vea en las clases del 12 al 16 de octubre?
- [ ] **Preguntar al profesor:** ¿cuál es la 3.ª forma de iniciar sesión (tema 9)? ¿Simétrico/asimétrico como en el apunte o como en Tanenbaum (tema 3)?
- [ ] **Apuntes después del 1 de octubre:** si hubo clase el 5 o el 8 de octubre, capturarla en [[Sistemas Operativos/Notas en curso|Notas en curso]] y añadirla aquí.
- [ ] **Consideraciones para la instalación (tema 5):** la teoría no se capturó. Pedir los apuntes o las diapositivas de esa clase.
- [ ] Ver el vídeo `Concurrencia y paralelismo.mp4` (tema 7) y anotar lo que no esté en el tema.
- [ ] Ver `Arquitecturas de sistemas.mp4`: probablemente es el tema 3 (estructura interna) o el 4. Anotar lo que falte.
- [ ] Unificar [[Usuarios y gestion de usuarios]] y [[Usuarios y su gestion]], que están duplicadas (después del examen, si no hay tiempo).

## Roadmap de estudio

Ocho sesiones de 1–2 h y dos colchones, en orden: cada sesión usa lo de la anterior. Los subsistemas del tema 4 se apoyan en los tipos del tema 3, y los permisos del 9 vuelven en el sistema de archivos del 10. El método es el mismo que funcionó en Enrutamiento: **ponerte a prueba** en vez de releer, **volver a cada tema** a los 1–4 días y **mezclar** preguntas de temas distintos.

**Cómo va cada sesión:**
1. **Calentamiento (10–15 min, sin apuntes):** las preguntas de «Recuperar» de sesiones anteriores, sacadas del [[Banco de preguntas - parcial 1|banco]]. Lo que falles, al [[#Registro de fallos]].
2. **Tema nuevo:** primero intenta explicarlo sin mirar; después comprueba con la sección del temario. No empieces releyendo.
3. **Cierre:** la prueba «Listo si». Si no la pasas, se repite en el siguiente colchón.

| Fecha          | Tema nuevo                                         | Recuperar (calentamiento) |
| -------------- | -------------------------------------------------- | ------------------------- |
| Vie 9 oct      | Sesión 1: introducción e historia (temas 1 y 2)    | —                         |
| Sáb 10 oct     | Sesión 2: tipos de SO (tema 3)                     | Sesión 1                  |
| Dom 11 oct     | Sesión 3: subsistemas, procesos y memoria (tema 4) | Sesiones 1 y 2            |
| Lun 12 oct     | Sesión 4: instalación y E/S (temas 5 y 6)          | Sesiones 2 y 3            |
| Mar 13 oct     | Colchón A: serie mezclada 1–6                      | Registro de fallos        |
| Mié 14 oct     | Sesión 5: concurrencia e interfaces (temas 7 y 8)  | Sesiones 3 y 4            |
| Jue 15 oct     | Sesión 6: usuarios y permisos en la VM (tema 9)    | Sesiones 4 y 5            |
| Vie 16 oct     | Sesión 7: sistema de archivos (tema 10)            | Sesiones 5 y 6            |
| Sáb 17 oct     | Colchón B: pendientes + serie mezclada 1–10        | Registro de fallos        |
| Dom 18 oct     | Sesión 8: simulacro                                | —                         |
| **Lun 19 oct** | **Examen**                                         |                           |

Si te atrasas, usa los colchones para terminar la sesión pendiente, pero haz al menos la mitad de la serie mezclada. No recortes las sesiones 6 y 7 ni el simulacro: usuarios y sistema de archivos son lo más reciente y lo más práctico. Dormir 7–9 h **toda la semana** cuenta más que la noche anterior.

### Sesión 1 (vie 9 oct) — Introducción e historia (temas 1 y 2)
- [x] Explicar en voz alta, sin notas: las tres definiciones (Tanenbaum, Silberschatz, profesor), las 7 funciones y los componentes (kernel, capa de usuario, hardware). Comprobar con el tema 1.
- [x] Llenar en papel la tabla de las 5 generaciones: años, hardware e hito del SO.
- [x] La pregunta ⭐: multiprogramación vs spooling, en una frase cada uno.
- [x] Preguntas de los temas 1 y 2 del banco.
- **Listo si:** la tabla de generaciones sale completa sin mirar y explicas la diferencia ⭐ sin dudar.

### Sesión 2 (sáb 10 oct) — Tipos de SO (tema 3)
- [x] **Recuperar:** la pregunta ⭐; las 7 funciones del SO; ¿en qué generación nacen las GUI?
- [x] Escribir de memoria los 3 criterios de clasificación y, en cada uno, sus categorías. Comprobar con el tema 3.
- [x] Clasificar con los tres criterios: Android, Windows 11, Debian en un servidor, OpenWRT en un router y el SO de los frenos de un auto.
- [x] Monolítico, microkernel e híbrido: qué va dentro del kernel, ventaja, desventaja y un ejemplo de cada uno.
- [x] Simétrico vs asimétrico, **con la corrección** del tema 3.
- **Listo si:** clasificas cualquier SO con los tres criterios y explicas por qué un fallo tumba un kernel monolítico y no un microkernel.

### Sesión 3 (dom 11 oct) — Subsistemas, procesos y memoria (tema 4)
- [x] **Recuperar:** 2 preguntas del tema 1, 2 del tema 2 y 2 del tema 3; un SO móvil con su kernel.
- [x] Escribir los 8 subsistemas con dos funciones cada uno, sin mirar.
- [x] Explicar con un ejemplo propio: proceso, ráfaga, quantum y cambio de contexto.
- [x] Explicar con el «mapa de apodos»: memoria virtual (el concepto), paginación (la técnica) y MMU (el hardware que traduce).
- **Listo si:** los 8 subsistemas salen de memoria y distingues memoria virtual / paginación / MMU en tres frases.

### Sesión 4 (lun 12 oct) — Instalación y E/S (temas 5 y 6)
- [ ] **Recuperar:** los 8 subsistemas; quantum y cambio de contexto; monolítico vs microkernel.
- [ ] Contar en orden la Práctica 1.1: requisitos → hipervisor → máquina virtual → instalación → particiones → software → post-instalación. Comprobar con el tema 5.
- [ ] Hipervisor de tipo 1 vs tipo 2, con un ejemplo de cada uno.
- [ ] Clasificar 6 dispositivos (teclado, disco, bocinas, tarjeta de red, mouse, pantalla) en las dos clasificaciones del tema 6.
- [ ] Registros de control, datos y estado, y para qué sirven los puertos de E/S.
- **Listo si:** describes la instalación sin mirar, con las particiones, y clasificas cualquier dispositivo en ambas clasificaciones.

### Colchón A (mar 13 oct) — Serie mezclada de los temas 1–6
- [ ] Primero, lo pendiente: terminar una sesión atrasada o repetir un «Listo si» fallido.
- [ ] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [ ] Serie mezclada de 45 min, en orden aleatorio: 2 preguntas de cada tema 1–6 del banco, la tabla de generaciones, 1 SO para clasificar y la pregunta ⭐. Antes de contestar cada una, di de qué tema es.

### Sesión 5 (mié 14 oct) — Concurrencia e interfaces (temas 7 y 8)
- [ ] **Recuperar:** los 3 registros de E/S; tipo 1 vs tipo 2; memoria virtual vs paginación.
- [ ] Concurrencia vs paralelismo sin mirar: qué ocurre en cada uno, qué hardware hace falta y qué es el pseudoparalelismo. Relacionarlo con la multiprogramación y el cambio de contexto.
- [ ] Si da tiempo, ver el vídeo de clase `Concurrencia y paralelismo.mp4` y anotar lo nuevo (pendiente de arriba).
- [ ] Terminal vs emulador de terminal vs shell; qué hace la shell con un comando antes de ejecutarlo; POSIX.
- [ ] La tabla de shells de memoria: BASH, ZSH, FISH, KSH y TCSH, con su cercanía a POSIX y su uso.
- **Listo si:** explicas concurrencia y paralelismo con un ejemplo de un solo núcleo y otro de varios, y ubicas los cinco shells.

### Sesión 6 (jue 15 oct) — Usuarios y permisos en la VM (tema 9)
- [ ] **Recuperar:** concurrencia vs paralelismo; terminal / emulador / shell; los 8 subsistemas.
- [ ] Sin notas: tipos de usuario con su UID, para qué sirve un usuario de servicio y qué guardan `/etc/passwd`, `/etc/shadow` y `/etc/group`.
- [ ] En la VM Debian de la Práctica 1.1, los 10 comandos del banco. Después de cada uno, comprobar el efecto con `id`, `groups`, `ls -l` o `tail /etc/passwd`.
- [ ] 10 conversiones rwx ↔ octal en papel (755, 644, 700, 640, `rwxr-x---`, `rw-rw-r--`…).
- [ ] `useradd` vs `adduser` y `userdel` vs `userdel -r` vs `userdel -f`.
- **Listo si:** conviertes rwx ↔ octal sin pensarlo y das el comando correcto para crear, modificar o borrar un usuario o un grupo.

### Sesión 7 (vie 16 oct) — Sistema de archivos (tema 10)
- [ ] **Recuperar:** 3 conversiones octales; el comando para meter a un usuario en un grupo sin sacarlo de los demás; para qué es `/etc/shadow`.
- [ ] Las 6 capas del sistema de archivos, de memoria y en orden.
- [ ] La tabla FAT32 / exFAT / NTFS / ext4 / APFS: origen, límites, journaling y rasgo distintivo.
- [ ] Casos: USB para Windows, Mac y Linux con archivos de más de 4 GB; servidor Linux; red mixta Windows/Linux; editar código en un servidor por SSH.
- [ ] SMB/Samba vs NFS vs SSHFS en una frase cada uno. En la VM, `ls /proc` y `ls /dev` para ver los sistemas de archivos virtuales.
- **Listo si:** dibujas las 6 capas, eliges el sistema de archivos correcto para cada caso y explicas SMB, NFS y SSHFS en una frase.

### Colchón B (sáb 17 oct) — Pendientes + serie mezclada de los temas 1–10
- [ ] Primero, lo pendiente: terminar una sesión atrasada o repetir un «Listo si» fallido.
- [ ] Si el profesor confirmó que entra material de las clases del 12 al 16 de octubre, procesarlo hoy (30–45 min).
- [ ] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [ ] Serie mezclada de 45 min, en orden aleatorio:
  - 1 pregunta de cada tema 1–8.
  - 3 de usuarios y permisos, con 2 conversiones octales y 1 comando.
  - 3 de sistema de archivos, con 1 caso de elección.
  - La pregunta ⭐.

### Sesión 8 (dom 18 oct) — Simulacro
- [ ] Sin apuntes, 60 min, **mezclados, no por tema**:
  - **Un tercio de teoría base (temas 1–4):** generaciones con la ⭐, clasificar un SO, subsistemas y memoria virtual.
  - **Un tercio de los temas 5–8:** instalación, E/S, concurrencia vs paralelismo y shells.
  - **Un tercio práctico (temas 9 y 10):** comandos de usuarios y grupos, permisos en octal, capas y elección de sistema de archivos.
- [ ] Corregir con este temario y volver solo a lo que fallaste.
- [ ] Repaso final de 15 min: contestar otra vez sin mirar solo lo que fallaste hoy y lo que quede en el registro. Y a dormir temprano.

### Registro de fallos

Anota aquí cada pregunta o ejercicio que falles en un calentamiento, un «Listo si» o el simulacro. Los colchones empiezan rehaciéndolos; borra una línea cuando te salga bien en dos días distintos.

- 

> Índice de la materia: [[Sistemas Operativos (materia)]]
