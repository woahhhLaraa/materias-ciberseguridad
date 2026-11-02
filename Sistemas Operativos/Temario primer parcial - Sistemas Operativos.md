---
materia: Sistemas Operativos
semestre: 3
tipo: temario
fecha-examen: 2026-10-22
tags: [examen, parcial, sistemas-operativos]
---

# Temario — primer parcial de Sistemas Operativos

**Examen: jueves 22 de octubre de 2026.** Estaba el lunes 19 y se movió.

Abarca **solo lo visto en clase** hasta el 19 de octubre. Las clases son lunes y jueves, así que la del 19 es la última antes del examen y se da por hecho que entra (ver [[#Pendientes antes del examen]]). Está armado con [[Sistemas Operativos/Notas en curso|Notas en curso]], las notas de concepto, los apuntes de agosto (`Sistemas Operativos Parcial 1.odt`), la Práctica 1.1 y el programa en C de la clase del 12 de octubre (`Operaciones Archivos/`). Los libros (Tanenbaum y Silberschatz) y la investigación de [[Concurrencia y paralelismo]] se usan solo como referencia, para verificar datos o rellenar un hueco. Cuando algo sale de un libro, se cita con su página.

Preguntas para ponerte a prueba: [[Banco de preguntas - parcial 1]].

## Lo que entra

Numeración y nombres del programa oficial ![[PE Sistemas Operativos 2022.pdf]], que tiene 13 temas. En clase se ha llegado hasta el 10.

| #   | Tema del programa                   | Clase                       | Estado                                                                                 |
| --- | ----------------------------------- | --------------------------- | -------------------------------------------------------------------------------------- |
| 1   | Introducción a los SO               | 17 ago                      | Completo                                                                               |
| 2   | Historia                            | 17 ago                      | Completo; ⭐ multiprogramación y spooling                                               |
| 3   | Tipos de SO                         | 20 ago                      | Completo; los mainframes se rellenan desde el libro; ⚠️ simétrico/asimétrico corregido |
| 4   | Capas o subsistemas                 | —                           | Completo, con lo básico de procesos y memoria                                          |
| 5   | Consideraciones para la instalación | Práctica 1.1, entrega 3 sep | ⚠️ Teoría no capturada; va lo de la práctica                                           |
| 6   | Dispositivos de E/S                 | —                           | Completo                                                                               |
| 7   | Concurrencia y paralelismo          | —                           | Versión compacta; ⚠️ vídeo de clase sin revisar                                        |
| 8   | Interfaces de usuario               | —                           | Completo; la parte de GUI es escueta                                                   |
| 9   | Manejo de usuarios                  | 10, 14 y 17 sep             | Completo; ⚠️ falta la 3.ª forma de iniciar sesión                                      |
| 10  | Sistema de archivos                 | 28 sep, 1, 12 y 19 oct      | Lo visto en clase; ⚠️ del 12 oct solo está el programa en C; 🆕 19 oct: gestión de espacio y protección |

**No entra:** el resto del programa, que no se ha visto. Son los temas 11 (procesos a fondo), 12 (comunicación entre procesos) y 13 (memoria y almacenamiento), y los subtemas del 10 que no salieron en clase (rutas y operaciones con directorios). Las operaciones con archivos entran desde la clase del 12 de octubre, y la gestión de espacio y la protección, desde la del 19.

> 🆕 **Agregado el 19 de octubre** (el examen se movió al jueves 22): la clase de ese día, en [[#19 de octubre — gestión de espacio y almacenamiento]] y [[#19 de octubre — protección de archivos]]. Es lo único nuevo. El plan de estudio se rehízo para tres días: [[#Roadmap de estudio]].

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

| Archivo       | Contenido                                                                      |
| ------------- | ------------------------------------------------------------------------------ |
| `/etc/passwd` | Información básica y **pública** de las cuentas                                |
| `/etc/shadow` | Contraseñas cifradas (hash), de forma segura                                   |
| `/etc/group`  | Define los grupos del sistema, para compartir permisos de archivos/directorios |

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

### 12 de octubre — operaciones con archivos en C

> ⚠️ De esta clase solo hay un encabezado en [[Sistemas Operativos/Notas en curso|Notas en curso]] y el programa que se hizo: `Operaciones Archivos/operacionesArchivos.c`, más `archivoPrueba.txt` para probarlo. Lo que sigue sale del código. La lista de operaciones viene de Tanenbaum, porque la teoría de la clase no se capturó.

- **Qué hace el programa:** es un menú que lee o escribe un archivo de texto de tres maneras: por carácter, por palabra o por línea.

| | Leer (modo `"r"`) | Escribir (modo `"a"`) |
|---|---|---|
| **Por carácter** | `fgetc(archivo)` hasta `EOF` | `getchar()` del teclado → `fputc(c, archivo)`, hasta el Enter |
| **Por palabra** | `fscanf(archivo, "%29s", cadena)` mientras devuelva 1 | `scanf("%29s", palabra)` → `fprintf(archivo, "%s ", palabra)`, hasta escribir `fin` |
| **Por línea** | `fgets(linea, sizeof(linea), archivo)` hasta que devuelva `NULL` | `fgets(linea, sizeof(linea), stdin)` → `fprintf(archivo, "%s ", linea)` |

- **Todas las funciones siguen el mismo patrón:**
  1. `fopen(nombre, modo)`, que devuelve un `FILE *`.
  2. Comprobar que no sea `NULL`. Lo es si el archivo no existe o si no hay permiso, lo que conecta con los permisos del tema 9.
  3. Leer o escribir en un bucle hasta la marca de fin: `EOF` para `fgetc`, `NULL` para `fgets`, o que `fscanf` deje de devolver 1.
  4. Llamar a `fclose` **una sola vez**, después del bucle.
- **Modos de apertura usados:**
  - `"r"` abre para leer. El archivo tiene que existir.
  - `"a"` (*append*) abre para escribir **al final**, sin borrar lo que ya había. Si el archivo no existe, lo crea.
  - Complemento que no sale en el código: `"w"` también escribe, pero **vacía** el archivo antes.
- **Tamaños de búfer:** `char cadena[30]` guarda hasta 29 caracteres más el `'\0'` de fin de cadena. Por eso se usa `%29s`: evita escribir fuera del arreglo. Lo mismo pasa con `linea[255]`.
- **Relación con las capas del 28 de septiembre:** estas funciones viven en la **capa de aplicación de usuario**. `fopen`, `fgetc`, `fprintf` y `fclose` son de la biblioteca estándar de C (`stdio.h`). Por debajo hacen las llamadas al sistema `open`, `read`, `write` y `close`, que son las que reciben las capas internas del sistema de archivos.
- **Operaciones de archivos según Tanenbaum** (pp. 264–265). Son las llamadas al sistema más comunes:

| Operación | Qué hace |
|---|---|
| **Create / Delete** | Crea el archivo vacío y fija algunos atributos / lo elimina para liberar espacio en disco |
| **Open** | Lleva los atributos y la lista de direcciones de disco a memoria principal, para acceder rápido en las llamadas siguientes |
| **Close** | Libera espacio en la tabla interna y obliga a escribir el último bloque del archivo, aunque no esté lleno |
| **Read / Write** | Lee o escribe en la posición actual. Si se escribe a la mitad del archivo, se sobrescriben los datos |
| **Append** | Una forma restringida de write: solo agrega al final. Es lo que hace el modo `"a"` |
| **Seek** | Mueve el apuntador del archivo a una posición concreta (acceso aleatorio) |
| **Get / Set attributes** | Lee o cambia atributos, como el modo de protección |
| **Rename** | Cambia el nombre del archivo |

> ⚠️ **Error en `escribirArchivoPorPalabra`:** el `fclose(archivo)` está **dentro** del `while`. El archivo se cierra después de la primera palabra, y las siguientes se escriben en un archivo ya cerrado, lo que es comportamiento indefinido. Además, si la primera palabra es `fin`, el archivo nunca se cierra. El `fclose` debe ir una sola vez, después del bucle. Si en el examen te piden escribir código, es el error que hay que evitar.

### 19 de octubre — gestión de espacio y almacenamiento

> 🆕 Agregado el 19 de octubre. Sale de [[Sistemas Operativos/Notas en curso|Notas en curso]]. Los libros solo completan lo que el apunte deja a medias, y se citan con su página.

- **Qué es:** el conjunto de mecanismos y algoritmos para organizar y controlar el espacio de almacenamiento disponible y aprovecharlo eficientemente. Responde a dos preguntas: cómo gestiona el SO el espacio **libre** y cómo gestiona el espacio **ocupado**.
- **Tres tareas:** asignar espacio para guardar archivos, registrar qué espacio está ocupado y cuál libre, y liberar espacio en el disco.
- Va de la mano con el sistema de archivos, que es lo que usa el SO para localizar los datos. En las capas del 28 de septiembre, es trabajo del **módulo de organización de archivos**, el que «rastrea espacio libre y decide dónde colocar datos nuevos».
- **Conceptos fundamentales:** dispositivo de almacenamiento, sistema de archivos, bloque de asignación, espacio ocupado y espacio libre.

**Sectores y bloques**

| | Qué es | Tamaño |
|---|---|---|
| **Sector** | División física del disco, de tamaño fijo | 512 o 4096 bytes |
| **Bloque de asignación** | La unidad con la que el sistema de archivos asigna espacio a los archivos. Lo forman uno o varios sectores | Lo fija el sistema de archivos |

> El apunte dice «4097 bytes». Es una errata de 4096 (4 KiB), el tamaño de sector de los discos modernos. Los libros solo dan 512 (Tanenbaum, pp. 26 y 376).

- **El tamaño en disco no es el tamaño del archivo.** Un archivo ocupa bloques completos, así que en disco ocupa su tamaño más lo que sobra de su último bloque. Ejemplo: un archivo de 1 000 bytes con bloques de 4 096 ocupa un bloque, y se desperdician 3 096 bytes.
- **Fragmentación:**
  - **Interna:** se pierde **parte de un bloque**, el pedazo sin usar del último bloque de un archivo (Tanenbaum, p. 277).
  - **Externa:** se pierden **bloques completos**. El espacio libre queda repartido en huecos y ninguno basta para lo que hay que guardar junto (Silberschatz, p. 379). De aquí vienen la fragmentación y la desfragmentación del disco.
  - Para no confundirlas: la interna es **dentro** del bloque y la externa, **entre** bloques.

**Métodos de asignación** (cómo se lleva el registro del espacio ocupado)

| | Contigua | Enlazada | Indexada |
|---|---|---|---|
| **Cómo** | Los bloques del archivo van juntos, uno tras otro | Los bloques están repartidos por el disco y se enlazan con referencias: cada uno apunta al siguiente | Un **bloque índice** guarda las referencias a todos los bloques de datos del archivo |
| **Ventajas** | Es el más simple | No necesita espacio contiguo, el archivo crece con cualquier bloque libre y reduce la fragmentación externa | Acceso directo a cualquier bloque, sin posiciones consecutivas y sin la fragmentación externa de reservar bloques contiguos |
| **Desventajas** | Cuesta encontrar un hueco contiguo, y si el archivo crece hay que reubicarlo | Es lento recorrer todos los bloques, los punteros ocupan espacio y, si se daña un enlace, se dificulta llegar a los bloques que siguen | El índice ocupa espacio extra, los archivos pequeños lo desperdician y los grandes necesitan índices adicionales o estructuras más complejas |
| **¿Fragmentación externa?** | Sí (Silberschatz, p. 379) | No (Silberschatz, p. 381) | No (Silberschatz, p. 383) |

- La contigua, según el apunte, es «útil como modelo conceptual» y se relaciona con la asignación de regiones contiguas, como en ciertos formatos de archivo y sistemas de almacenamiento.
- Conexión con el 28 de septiembre: Tanenbaum llama **FAT** (*File Allocation Table*) a la enlazada con la tabla de enlaces en memoria (p. 278), y de ahí viene el nombre de FAT32. A la indexada la llama **nodo-i** (p. 279), que son los inodos de ext4.

**Métodos de asignación en los SO reales**

| SO (sistema de archivos) | Estructura |
|---|---|
| **Windows (NTFS)** | **MFT** (*master file table*): registros con la información de los archivos y sus ubicaciones |
| **Linux (ext4)** | **Inodos** para los metadatos y las referencias a los datos, y ***extents*** para grupos de bloques contiguos |
| **macOS (APFS)** | **Árboles B+** para organizar los metadatos y administrar la información del sistema de archivos |

> El apunte no dice de qué sistema es la fila de inodos y *extents*. Por la tabla del 28 de septiembre, es ext4.

**Gestión del espacio libre**

- **Mapa de bits:** una secuencia de bits, uno por bloque. En el apunte, **0 = libre y 1 = ocupado**.
  - **Cómo se usa:** el sistema consulta el mapa, busca los bits de bloques libres, elige los que necesita y los cambia a ocupado. Al borrar un archivo, sus bits vuelven a libre.
  - **Ventajas:** encuentra rápido los bloques libres y los consecutivos, y es sencillo de consultar y actualizar.
  - **Desventajas:** necesita memoria proporcional al número de bloques, así que en discos muy grandes ocupa bastante.

  > ⚠️ **Convención del bit.** Silberschatz la usa al revés: «Si el bloque está libre, el bit será igual a 1; si el bloque está asignado, el bit será 0» (p. 386). Tanenbaum usa 1 para libre «(o viceversa)» (p. 295), o sea que cualquiera de las dos vale si se dice cuál es. **En el examen usa la del profesor (0 = libre) y escríbela junto al mapa.**

- **Lista enlazada de bloques libres:** cada bloque libre guarda una referencia al siguiente bloque libre.
  - **Cómo se usa:** el sistema localiza el primer bloque de la lista. Cuando necesita espacio, saca uno o varios bloques de la lista y actualiza el puntero para que señale al siguiente libre.
  - **Ventajas:** no necesita un mapa de todo el disco y es sencilla de implementar.
  - **Desventajas:** puede ser lenta, y los enlaces ocupan espacio.
- **Agrupamiento y conteo:** evitan registrar cada bloque libre por separado. Es la misma idea de la asignación indexada, pero aplicada al espacio libre. Permiten consultar varias direcciones en una sola operación y reducen el espacio que ocupa el registro de bloques libres. El apunte no separa las dos técnicas; Silberschatz sí:
  - **Agrupamiento:** el primer bloque libre guarda las direcciones de *n* bloques libres. El último de esos *n* guarda las direcciones de otros *n*, y así sucesivamente (p. 387).
  - **Conteo** (Silberschatz lo llama «recuento»): como los bloques libres suelen venir seguidos, se guarda la dirección del primero y **cuántos** bloques libres contiguos le siguen. Cada entrada es una dirección más un contador (p. 388). Por eso el apunte dice que reduce los registros cuando hay secuencias de bloques consecutivos.

### 19 de octubre — protección de archivos

> 🆕 Agregado el 19 de octubre. Es el tema 9 (permisos del 17 de septiembre) visto en general: sujeto, objeto y acción.

- **Qué es:** los mecanismos que usa el SO para controlar **quién** puede acceder a los archivos y **qué operaciones** puede hacer con ellos.
- **Objetivos:**

| Objetivo | En el apunte |
|---|---|
| **Confidencialidad** | Solo la persona autorizada puede ver el archivo |
| **Integridad** | Los archivos no se cambian «porque sí» |
| **Disponibilidad** | Siempre están disponibles para la persona autorizada |
| **Control de acceso** | El apunte no lo define. Según la definición de arriba, es decidir quién accede y qué operaciones puede hacer |

**Modelos de control de acceso**

| Modelo | Quién decide los permisos | Ejemplo (no viene en el apunte) |
|---|---|---|
| **DAC** (discrecional) | El **propietario** del recurso concede o retira permisos | Los permisos rwx con `chmod` del tema 9: tú decides sobre tus archivos |
| **MAC** (obligatorio) | Una **política centralizada**, según reglas de seguridad y niveles de clasificación. El usuario no puede cambiarla | Sistemas militares con niveles «secreto» y «confidencial»; SELinux en Linux |
| **RBAC** (por roles) | Los permisos se asignan a **roles** (administrador, profesor, alumno) y cada usuario recibe los de su rol | Eminus: el rol de profesor sube calificaciones y el de alumno solo las ve |

- Tanenbaum describe el control discrecional y el obligatorio en la p. 634, y Silberschatz nombra el RBAC en la p. 485. Ojo: en Silberschatz, «MAC» también es el código de autenticación de mensajes (p. 531), que es un concepto de criptografía y no tiene nada que ver con este.
- **Cómo funciona el control de acceso:** 1) el sistema identifica al usuario o proceso; 2) identifica el archivo pedido; 3) consulta los permisos correspondientes; 4) autoriza o rechaza la operación.

**Matriz de control de acceso**

> El apunte pone esta parte debajo de MAC, pero habla de la matriz de control de acceso, que es otro concepto. Aquí va por separado.

- **Qué es:** una tabla con los sujetos (usuarios o dominios) en las filas y los objetos (archivos) en las columnas. Cada celda dice qué permisos tiene ese sujeto sobre ese objeto (Tanenbaum, p. 624; Silberschatz, p. 489).
- **Ventajas:** representa con claridad las relaciones entre sujetos y objetos, y sirve de base conceptual para los demás mecanismos de control de acceso.
- **Desventajas:** se vuelve enorme con muchos usuarios y archivos, y mantenerla completa sale caro.
- Por eso se implementa con estructuras más prácticas. Leída **por columnas** da una **ACL** por archivo, y leída **por filas**, una **lista de capacidades** por sujeto (Silberschatz, p. 493; Tanenbaum, pp. 625 y 627).

| | `notas.txt` | `tarea.c` | `/etc/shadow` |
|---|---|---|---|
| **ana** | rw | r | — |
| **luis** | r | rw | — |
| **root** | rw | rw | rw |

La ACL de `tarea.c` es su columna: ana `r`, luis `rw`, root `rw`. Las capacidades de ana son su fila: `notas.txt` `rw`, `tarea.c` `r`.

**Lista de control de acceso (ACL)**

- **Qué es:** una estructura asociada a un archivo o directorio que especifica qué usuarios o grupos pueden hacer qué operaciones. Cada entrada indica el usuario o grupo, el tipo de permiso y las reglas de acceso que se le aplican.
- **Qué añade a rwx** (no viene en el apunte): rwx solo tiene tres categorías (propietario, grupo y otros). Con una ACL le das permisos a **un usuario concreto** sin cambiar el propietario ni el grupo del archivo.
- **En Linux**, el comando de clase:

  ```bash
  sudo apt install acl
  setfacl -m u:ana:rw proyecto.txt
  ```

  Crea la entrada de la ACL y le da a la usuaria `ana` permisos de lectura y escritura sobre `proyecto.txt`. `-m` significa modificar; `u:` es un usuario, y con `g:` sería un grupo.
- **Complemento para la VM:** `getfacl proyecto.txt` muestra la ACL, `ls -l` marca el archivo con un `+` al final de los permisos y `setfacl -x u:ana proyecto.txt` quita la entrada.

**Dominios de protección**

- **Qué es:** el conjunto de recursos y operaciones a los que un usuario o proceso tiene permitido acceder. Tanenbaum lo resume como «un conjunto de pares (objeto, permisos)» (p. 622): cada fila de la matriz es un dominio.
- **Puede definir permisos para:** leer archivos, modificar archivos, ejecutar programas y acceder a ciertos dispositivos o recursos.

  > El apunte dice «modificar argumentos». Por el contexto, es «modificar archivos».

- **Cómo funciona:** 1) el sistema fija un conjunto de permisos para el usuario o proceso; 2) cuando el proceso pide una operación, el sistema verifica que esté en su dominio autorizado; 3) si está permitida, se ejecuta; si no, se rechaza.
- **Ventajas:** limita el acceso a los recursos, reduce el impacto de errores y acciones maliciosas, y separa los privilegios de administrador de los ordinarios.
- **Ejemplo** (no viene en el apunte): el usuario de servicio `www-data` del tema 9. Su dominio incluye leer los archivos de la web, pero no `/home` ni `/etc/shadow`. Si atacan el servidor web, el daño se queda dentro de ese dominio.

## ⭐ Marcado por el profesor como «tema de examen»

> Multiprogramación y spooling (3.ª generación).

- **Multiprogramación:** varios trabajos cargados en **memoria** a la vez; mientras uno espera E/S, la CPU atiende a otro.
- **Spooling:** los trabajos se leen de las tarjetas y se guardan en **disco**, para cargarlos después sin esperar al lector.
- Una frase: *la multiprogramación carga en memoria; el spooling almacena en disco.*

## Pendientes antes del examen

- [ ] **Preguntar al profesor por Teams o por correo antes del miércoles**, porque ya no hay clase antes del examen: ¿entran la gestión de espacio y la protección del 19 de octubre? ¿Entran las operaciones con archivos en C del 12? Si dice que no, quita las sesiones 9 y 10 del roadmap y usa ese tiempo como colchón.
- [ ] **En el mismo mensaje:** ¿cuál es la 3.ª forma de iniciar sesión (tema 9)? ¿Simétrico/asimétrico como en el apunte o como en Tanenbaum (tema 3)? En el mapa de bits, ¿0 es libre como en el apunte? Silberschatz usa 1 para libre y Tanenbaum acepta las dos (ver [[#19 de octubre — gestión de espacio y almacenamiento]]).
- [ ] **Teoría de la clase del 12 de octubre:** en [[Sistemas Operativos/Notas en curso|Notas en curso]] solo está el encabezado «Operaciones con archivos en C». Si se dio teoría o se dictaron los modos de apertura, capturarlos y contrastarlos con el tema 10.
- [ ] **Apuntes del 5 y el 8 de octubre:** no hay nada en [[Sistemas Operativos/Notas en curso|Notas en curso]]. Confirmar si hubo clase.
- [ ] **Consideraciones para la instalación (tema 5):** la teoría no se capturó. Pedir los apuntes o las diapositivas de esa clase.
- [ ] Ver el vídeo `Concurrencia y paralelismo.mp4` (tema 7) y anotar lo que no esté en el tema. *Solo si sobra tiempo: con tres días, va detrás del roadmap.*
- [ ] Ver `Arquitecturas de sistemas.mp4`: probablemente es el tema 3 (estructura interna) o el 4. Anotar lo que falte. *Solo si sobra tiempo.*
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
| Vie 16 oct     | Sesión 7: sistema de archivos y operaciones en C (tema 10) | Sesiones 5 y 6     |
| ~~Sáb 17 oct~~ | ~~Colchón B~~ → pasa al miércoles 21               |                           |
| ~~Dom 18 oct~~ | ~~Sesión 8: simulacro~~ → pasa al miércoles 21     |                           |

#### 🆕 Plan nuevo: el examen se movió al jueves 22

Quedan tres días. Lo pendiente es la parte en C de la sesión 7, el colchón B, el simulacro y el tema nuevo del 19 de octubre. El tema nuevo va **primero**, para que le toque recuperarlo dos veces antes del examen. Va en dos sesiones porque es largo.

| Fecha          | Qué toca                                                                 | Recuperar (calentamiento)     |
| -------------- | ------------------------------------------------------------------------ | ----------------------------- |
| Lun 19 oct (noche) | Sesión 9: gestión de espacio (clase del 19, primera mitad)           | —                             |
| Mar 20 oct     | Sesión 10: protección de archivos (clase del 19, segunda mitad) + lo que quedó en C de la sesión 7 | Sesión 9 y sesión 6 (permisos) |
| Mié 21 oct     | Mañana: colchón B. Tarde: simulacro (sesión 8)                           | Sesiones 9 y 10               |
| **Jue 22 oct** | **Examen.** Antes, 15 min con el [[#Registro de fallos]] y nada nuevo     |                               |

Si te atrasas, el orden de lo que no se recorta es: **simulacro → sesión 9 → sesión 10 → C**. El colchón B es lo primero que se acorta: haz al menos la mitad de la serie mezclada. Dormir 7–9 h estas tres noches cuenta más que estudiar de más la última.

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
- [x] **Recuperar:** los 8 subsistemas; quantum y cambio de contexto; monolítico vs microkernel.
- [x] Contar en orden la Práctica 1.1: requisitos → hipervisor → máquina virtual → instalación → particiones → software → post-instalación. Comprobar con el tema 5.
- [x] Hipervisor de tipo 1 vs tipo 2, con un ejemplo de cada uno.
- [x] Clasificar 6 dispositivos (teclado, disco, bocinas, tarjeta de red, mouse, pantalla) en las dos clasificaciones del tema 6.
- [x] Registros de control, datos y estado, y para qué sirven los puertos de E/S.
- **Listo si:** describes la instalación sin mirar, con las particiones, y clasificas cualquier dispositivo en ambas clasificaciones.

### Colchón A (mar 13 oct) — Serie mezclada de los temas 1–6
- [x] Primero, lo pendiente: terminar una sesión atrasada o repetir un «Listo si» fallido.
- [x] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [x] Serie mezclada de 45 min, en orden aleatorio: 2 preguntas de cada tema 1–6 del banco, la tabla de generaciones, 1 SO para clasificar y la pregunta ⭐. Antes de contestar cada una, di de qué tema es.

### Sesión 5 (mié 14 oct) — Concurrencia e interfaces (temas 7 y 8)
- [x] **Recuperar:** los 3 registros de E/S; tipo 1 vs tipo 2; memoria virtual vs paginación.
- [x] Concurrencia vs paralelismo sin mirar: qué ocurre en cada uno, qué hardware hace falta y qué es el pseudoparalelismo. Relacionarlo con la multiprogramación y el cambio de contexto.
- [x] Si da tiempo, ver el vídeo de clase `Concurrencia y paralelismo.mp4` y anotar lo nuevo (pendiente de arriba).
- [x] Terminal vs emulador de terminal vs shell; qué hace la shell con un comando antes de ejecutarlo; POSIX.
- [x] La tabla de shells de memoria: BASH, ZSH, FISH, KSH y TCSH, con su cercanía a POSIX y su uso.
- **Listo si:** explicas concurrencia y paralelismo con un ejemplo de un solo núcleo y otro de varios, y ubicas los cinco shells.

### Sesión 6 (jue 15 oct) — Usuarios y permisos en la VM (tema 9)
- [x] **Recuperar:** concurrencia vs paralelismo; terminal / emulador / shell; los 8 subsistemas.
- [x] Sin notas: tipos de usuario con su UID, para qué sirve un usuario de servicio y qué guardan `/etc/passwd`, `/etc/shadow` y `/etc/group`.
- [x] En la VM Debian de la Práctica 1.1, los 10 comandos del banco. Después de cada uno, comprobar el efecto con `id`, `groups`, `ls -l` o `tail /etc/passwd`.
- [x] 10 conversiones rwx ↔ octal en papel (755, 644, 700, 640, `rwxr-x---`, `rw-rw-r--`…).
- [x] `useradd` vs `adduser` y `userdel` vs `userdel -r` vs `userdel -f`.
- **Listo si:** conviertes rwx ↔ octal sin pensarlo y das el comando correcto para crear, modificar o borrar un usuario o un grupo.

### Sesión 7 (vie 16 oct) — Sistema de archivos y operaciones en C (tema 10)
- [x] **Recuperar:** 3 conversiones octales; el comando para meter a un usuario en un grupo sin sacarlo de los demás; para qué es `/etc/shadow`.
- [x] Las 6 capas del sistema de archivos, de memoria y en orden.
- [x] La tabla FAT32 / exFAT / NTFS / ext4 / APFS: origen, límites, journaling y rasgo distintivo.
- [x] Casos: USB para Windows, Mac y Linux con archivos de más de 4 GB; servidor Linux; red mixta Windows/Linux; editar código en un servidor por SSH.
- [x] SMB/Samba vs NFS vs SSHFS en una frase cada uno. En la VM, `ls /proc` y `ls /dev` para ver los sistemas de archivos virtuales.
> 🆕 Las cuatro casillas de C que siguen pasan al **martes 20**, después de la sesión 10.

- [ ] **Operaciones en C (12 oct):** en papel y sin mirar, escribe la función que lee un archivo por línea, con los 4 pasos: `fopen`, comprobar `NULL`, bucle, `fclose`. Después compárala con `operacionesArchivos.c`.
- [ ] Qué función se usa para cada combinación de leer o escribir por carácter, palabra o línea, y con qué se detecta el fin en cada caso (`EOF`, `NULL`, `fscanf` ≠ 1). Diferencia entre `"r"`, `"a"` y `"w"`.
- [ ] Compila el programa con `gcc operacionesArchivos.c -o operacionesArchivos` y pruébalo con `archivoPrueba.txt`. Encuentra y corrige el `fclose` mal puesto en `escribirArchivoPorPalabra`.
- [ ] Une las dos partes: qué llamada al sistema hay debajo de `fopen`, `fgetc`, `fprintf` y `fclose`, y en qué capa vive el programa. Qué hacen *open* y *close* según Tanenbaum.
- **Listo si:** dibujas las 6 capas, eliges el sistema de archivos correcto para cada caso, explicas SMB, NFS y SSHFS en una frase y escribes sin errores una lectura por línea en C, con `fclose` fuera del bucle.

### 🆕 Sesión 9 (lun 19 oct, noche) — Gestión de espacio (tema 10, clase del 19)
Es la misma noche de la clase, así que no hay calentamiento: el tema está fresco. 45–60 min.
- [x] Sin mirar: qué es la gestión de espacio, sus 3 tareas (asignar, registrar, liberar) y la diferencia entre **sector** y **bloque de asignación**. Comprobar con [[#19 de octubre — gestión de espacio y almacenamiento]].
- [x] Fragmentación: un archivo de 5 000 bytes en bloques de 4 096 ocupa ___ bloques, ___ bytes en disco y desperdicia ___ bytes. ¿Es fragmentación interna o externa? Haz otro con 10 000 bytes.
- [x] Llenar de memoria la tabla de contigua / enlazada / indexada: cómo se guardan los bloques, una ventaja, una desventaja y si sufre fragmentación externa. Dibuja un archivo de 3 bloques con cada método.
- [x] Une cada estructura con su SO: MFT, inodos con *extents* y árboles B+.
- [x] Mapa de bits: con `1 0 1 1 0 0 0 1` (bloques 0–7) y la convención del apunte (0 = libre), ¿qué bloques están libres? Asigna un archivo de 2 bloques contiguos y escribe el mapa resultante.
- [x] Las 4 técnicas de espacio libre (mapa de bits, lista enlazada, agrupamiento y conteo), en una frase cada una, con una ventaja y una desventaja.
- **Listo si:** dibujas los 3 métodos de asignación sin mirar, calculas el desperdicio de un archivo y lees y actualizas un mapa de bits.

### 🆕 Sesión 10 (mar 20 oct) — Protección de archivos + lo pendiente en C
- [x] **Recuperar:** contigua vs enlazada vs indexada; fragmentación interna vs externa; qué valor marca un bloque libre en el mapa de bits; 2 conversiones octales y para qué sirve `/etc/shadow` (sesión 6).
- [x] Sin mirar: definición de protección de archivos y los 4 objetivos (confidencialidad, integridad, disponibilidad y control de acceso), con un ejemplo de cómo se rompe cada uno.
- [ ] DAC, MAC y RBAC: clasifica 1) tú haces `chmod 600` a tu archivo; 2) un sistema militar con niveles «secreto» y «confidencial»; 3) en Eminus, el profesor sube calificaciones y el alumno solo las ve. ¿Cuál de los tres son los permisos rwx del tema 9?
- [ ] Matriz de control de acceso: dibuja una de 3 usuarios × 3 archivos. Explica por qué no se guarda entera y qué sale de leerla por columnas (ACL) y por filas (capacidades).
- [ ] **En la VM Debian:** `sudo apt install acl`; crea un usuario de prueba, `setfacl -m u:usuario:rw archivo`, luego `getfacl archivo` y `ls -l archivo` (fíjate en el `+`). Quítalo con `setfacl -x u:usuario archivo`.
- [ ] Dominio de protección: definición, los 3 pasos de cómo funciona y las 3 ventajas. Ejemplo: el usuario de servicio `www-data` del tema 9.
- [ ] **Lo pendiente de la sesión 7:** las cuatro casillas de C (función de lectura por línea en papel, tabla de funciones y modos, compilar y corregir el `fclose`, y las llamadas al sistema de debajo).
- **Listo si:** clasificas cualquier escenario en DAC, MAC o RBAC, explicas qué da una ACL que rwx no da y escribes el `setfacl` sin mirar. Más el «Listo si» de la sesión 7.

### Colchón B (mié 21 oct, mañana) — Pendientes + serie mezclada de los temas 1–10
- [ ] Primero, lo pendiente: terminar una sesión atrasada o repetir un «Listo si» fallido.
- [ ] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [ ] Serie mezclada de 45 min, en orden aleatorio:
  - 1 pregunta de cada tema 1–8.
  - 3 de usuarios y permisos, con 2 conversiones octales y 1 comando.
  - 5 de sistema de archivos: 1 caso de elección, 1 función en C de leer o escribir, 1 método de asignación, 1 mapa de bits y 1 caso de DAC/MAC/RBAC o de ACL.
  - La pregunta ⭐.

### Sesión 8 (mié 21 oct, tarde) — Simulacro
- [ ] Sin apuntes, 60 min, **mezclados, no por tema**:
  - **Un tercio de teoría base (temas 1–4):** generaciones con la ⭐, clasificar un SO, subsistemas y memoria virtual.
  - **Un tercio de los temas 5–8:** instalación, E/S, concurrencia vs paralelismo y shells.
  - **Un tercio práctico (temas 9 y 10):** comandos de usuarios y grupos, permisos en octal, capas, elección de sistema de archivos, una función en C que lea o escriba un archivo, **un método de asignación o un mapa de bits, y un modelo de control de acceso o una ACL**.
- [ ] Corregir con este temario y volver solo a lo que fallaste.
- [ ] Repaso final de 15 min: contestar otra vez sin mirar solo lo que fallaste hoy y lo que quede en el registro. Y a dormir temprano.

### Jueves 22 — antes del examen
- [ ] 15 min: el [[#Registro de fallos]] sin mirar y la pregunta ⭐. Nada nuevo.

### Registro de fallos

Anota aquí cada pregunta o ejercicio que falles en un calentamiento, un «Listo si» o el simulacro. Los colchones empiezan rehaciéndolos; borra una línea cuando te salga bien en dos días distintos.

- 

> Índice de la materia: [[Sistemas Operativos (materia)]]
