#!/usr/bin/env python3
"""Genera el examen de práctica (100 reactivos) y su clave de respuestas en PDF."""
import html, random, re, sys
from weasyprint import HTML

OUT = sys.argv[1]

# ---------------------------------------------------------------- reactivos
# Opción múltiple: (tema, pregunta, correcta, [distractores], justificación)
MC = [
 # Tema 1
 (1, "¿Qué tienen en común las definiciones de sistema operativo de Tanenbaum, Silberschatz y la del profesor?",
  "Administrar los recursos del equipo",
  ["Ofrecer una interfaz gráfica al usuario", "Traducir direcciones virtuales a físicas", "Compilar los programas de aplicación"],
  "Las tres coinciden en el núcleo: administrar recursos; difieren en el énfasis."),
 (1, "¿Qué definición pone el énfasis en que el SO «proporciona servicios para facilitar la ejecución de los programas de aplicación»?",
  "La de Silberschatz", ["La de Tanenbaum", "La del profesor", "La del estándar POSIX"],
  "Tanenbaum enfatiza la intermediación; Silberschatz, el servicio a las aplicaciones."),
 (1, "La característica de un SO que consiste en adaptarse a distinto hardware se llama:",
  "Portabilidad", ["Estabilidad", "Eficiencia", "Capacidad de evolución"],
  "Portabilidad = adaptarse a distinto hardware."),
 (1, "¿Cuál de las siguientes NO es una función esencial del SO según las notas?",
  "Compilar el código fuente de las aplicaciones",
  ["Proteger los recursos de usuarios y de otros programas", "Gestionar la memoria", "Proporcionar una interfaz de usuario"],
  "Funciones: administrar CPU, memoria, archivos, dispositivos, procesos, interfaz de usuario y proteger recursos."),
 # Tema 2
 (2, "¿En qué generación no existía sistema operativo y todo se programaba en lenguaje máquina sobre tubos de vacío?",
  "Primera (1945–1955)", ["Segunda (1955–1965)", "Tercera (1965–1980)", "Cuarta (1980–1990)"],
  "1.ª generación: tubos de vacío, todo directo sobre el hardware, sin SO."),
 (2, "En la segunda generación aparecen los sistemas por lotes, a los que se considera:",
  "El antecesor del sistema operativo actual",
  ["La primera interfaz gráfica", "El origen de los dispositivos móviles", "La primera red de computadoras"],
  "2.ª generación: transistores, mainframes y sistemas por lotes, antecesor del SO actual."),
 (2, "⭐ La multiprogramación es:",
  "La técnica que permite tener varios trabajos cargados en memoria a la vez",
  ["La técnica que guarda en disco los trabajos leídos de las tarjetas perforadas",
   "La ejecución de dos procesos exactamente al mismo tiempo en varios núcleos",
   "Un sistema que atiende a un solo usuario a la vez"],
  "Tema marcado por el profesor: mientras un trabajo espera E/S, la CPU atiende a otro."),
 (2, "⭐ El spooling consiste en:",
  "Leer los trabajos de las tarjetas y almacenarlos directamente en disco, en lugar de cargarlos en memoria principal",
  ["Cargar varios trabajos en memoria principal a la vez",
   "Repartir la CPU en turnos entre varios usuarios interactivos",
   "Traducir direcciones virtuales mediante la MMU"],
  "Tema marcado por el profesor: «la multiprogramación carga en memoria; el spooling almacena en disco»."),
 (2, "¿Cuál fue el primer microprocesador de 8 bits y propósito general mencionado en la cuarta generación?",
  "Intel 8080 (1974)", ["Intel 8086 (1978)", "Intel 4004 (1971)", "Motorola 68000 (1979)"],
  "4.ª generación: Intel 8080, 1974, 8 bits, propósito general."),
 (2, "¿Qué sistemas operativos nacen en la quinta generación?",
  "Android, iOS y HarmonyOS", ["DOS, MS-DOS y Windows", "UNIX, BSD y Linux", "Sistemas por lotes en FORTRAN y ensamblador"],
  "5.ª generación (1990–actualidad): dispositivos móviles; Android, iOS y HarmonyOS."),
 # Tema 3
 (3, "¿Cuál NO es uno de los tres criterios de clasificación de los SO vistos en clase?",
  "Según el lenguaje en que fue programado",
  ["Según el tipo de sistema informático", "Según servicios y capacidades", "Según su estructura interna"],
  "Los tres criterios: tipo de sistema informático, servicios y capacidades, estructura interna."),
 (3, "Según Tanenbaum, los tres servicios típicos de un SO de mainframe son:",
  "Procesamiento por lotes, procesamiento de transacciones y tiempo compartido",
  ["Multiprogramación, spooling y paginación", "GUI, NUI y CLI", "Tiempo real duro, tiempo real blando y monotarea"],
  "Tanenbaum, p. 64: lotes, transacciones (p. ej. cheques bancarios) y tiempo compartido."),
 (3, "Un rasgo distintivo de los SO de servidor es que:",
  "Están diseñados para nunca apagarse",
  ["Su principal limitación es la batería", "Corren en microcontroladores con poco almacenamiento", "Atienden a un solo usuario a la vez"],
  "Servidor: multiusuario, multitarea, escalable, orientado a red, robusto y diseñado para nunca apagarse."),
 (3, "¿Qué SO móvil usa el microkernel HongMeng?",
  "HarmonyOS", ["Tizen OS", "iOS", "Roku"],
  "HarmonyOS (Huawei) → microkernel HongMeng. Tizen y Roku usan Linux; iOS, Darwin."),
 (3, "El SO embebido hecho principalmente para sensores en redes IoT es:",
  "TinyOS", ["OpenWRT", "Embedded Linux", "Xiaomi HyperOS"],
  "TinyOS: sensores IoT. OpenWRT: routers. Embedded Linux: cámaras, routers, smart TV."),
 (3, "En un automóvil, los frenos de emergencia y las bolsas de aire requieren un SO:",
  "De tiempo real duro", ["De tiempo real blando", "Multiusuario de escritorio", "Por lotes"],
  "Tiempo real duro: un fallo pone en riesgo vidas. El infoentretenimiento va en un sistema aparte."),
 (3, "En un kernel monolítico, como el de Linux, el principal riesgo es que:",
  "Si un componente falla, falla todo el kernel",
  ["La comunicación entre servidores de espacio de usuario genera mucho overhead",
   "No puede ejecutar más de un proceso", "Los drivers no pueden acceder al hardware"],
  "Monolítico: rápido y eficaz, pero todo vive en el kernel; el overhead es la desventaja del microkernel."),
 (3, "El kernel XNU de macOS e iOS es un ejemplo de arquitectura:",
  "Híbrida", ["Monolítica", "Microkernel puro", "Por lotes"],
  "Híbridos: Windows XP/7/10/11, XNU (macOS, iOS), ReactOS, BeOS."),
 (3, "Según Tanenbaum (p. 566), en el multiprocesamiento simétrico (SMP):",
  "Cualquier CPU puede ejecutar el SO; no hay maestro ni esclavos",
  ["Un procesador maestro dirige a los demás procesadores esclavos",
   "Solo un núcleo ejecuta procesos de usuario", "El SO no detecta más de un procesador"],
  "Ojo: tu apunte original tiene los nombres invertidos; el temario lo corrige con Tanenbaum. Confírmalo con el profesor."),
 # Tema 4
 (4, "¿Qué componente de hardware, dentro de la CPU, traduce las direcciones virtuales a direcciones físicas?",
  "La MMU", ["La BIOS", "El planificador de CPU", "El registro de estado"],
  "MMU: existe para bajar la carga lógica del CPU."),
 (4, "Un quantum es:",
  "La cantidad de milisegundos que el CPU puede dar a una tarea",
  ["El número de procesos cargados en memoria", "El tamaño de una página de memoria virtual", "El tiempo que tarda la BIOS en arrancar"],
  "Quantum: el tiempo de CPU asignado a una tarea por turno."),
 (4, "Tras un cambio de contexto, cuando el CPU vuelve a una tarea, ¿qué hace con ella?",
  "La reanuda desde donde se quedó",
  ["La reinicia desde el principio", "La envía al almacenamiento secundario", "La termina y libera su memoria"],
  "Cambio de contexto: se pasa de una tarea a otra y al volver se reanuda donde se quedó."),
 (4, "¿Cuál es la relación entre memoria virtual y paginación?",
  "La paginación es la técnica con la que se logra la memoria virtual",
  ["La memoria virtual es la técnica con la que se logra la paginación",
   "Ambas son el mismo componente físico de la RAM", "La paginación sustituye a la MMU"],
  "Memoria virtual = concepto/ilusión; paginación = técnica (mapa virtual de «apodos» por proceso)."),
 (4, "De los ocho subsistemas, ¿cuál decide quién y cuándo puede leer o escribir en el almacenamiento secundario y realiza la planificación de disco?",
  "Almacenamiento secundario", ["Sistema de archivos", "Gestión de memoria", "Interfaz de usuario"],
  "Almacenamiento secundario: acceso, espacio libre/ocupado, seguridad y planificación de disco."),
 (4, "¿Qué firmware de la tarjeta madre hace un test de integridad del CPU, RAM y GPU y busca una unidad de arranque?",
  "La BIOS", ["La MMU", "El kernel", "El emulador de terminal"],
  "BIOS: Basic Input Output System; luego el SO toma el control con sus propios drivers."),
 (4, "¿A qué subsistema le corresponde manejar la situación de interbloqueo (deadlock)?",
  "Gestión de procesos", ["Gestión de memoria", "Redes y comunicaciones", "Interfaz de usuario"],
  "Gestión de procesos: crear/pausar/reanudar/cerrar, comunicación, sincronización, deadlock, ráfagas de CPU."),
 # Tema 5
 (5, "Un hipervisor de tipo 2:",
  "Corre como programa de usuario sobre un SO anfitrión, como VirtualBox",
  ["Corre directamente sobre el hardware, como KVM", "Es el firmware de la tarjeta madre", "Solo puede ejecutar SO embebidos"],
  "Tipo 1: directo sobre el hardware (KVM). Tipo 2: sobre un SO anfitrión (VirtualBox)."),
 (5, "En la práctica 1.1, ¿por qué se justificó que KVM actúa como hipervisor de tipo 1?",
  "Porque está integrado en el kernel de Linux y corre directo sobre el hardware",
  ["Porque es un programa de usuario sobre un SO anfitrión", "Porque el enunciado pedía un hipervisor de tipo 1", "Porque usa discos en formato qcow2"],
  "Tanenbaum, p. 600. El enunciado pedía tipo 2 (VirtualBox)."),
 (5, "En el particionado manual MBR de la práctica, ¿qué partición fue primaria?",
  "/ (25 GB, ext4)", ["/home (21 GB, ext4)", "swap (7.7 GB)", "/boot (1 GB, ext2)"],
  "/ primaria; /home y swap lógicas. No hubo partición /boot."),
 (5, "¿Qué procesador y RAM pedía el enunciado de la práctica de instalación?",
  "4 núcleos y 1–2 GB de RAM", ["2 núcleos y 8 GB de RAM", "1 núcleo y 512 MB de RAM", "8 núcleos y 16 GB de RAM"],
  "Además: 30–50 GB de disco, 1 adaptador de red, virtualización activa e ISO de Debian 13."),
 # Tema 6
 (6, "Según la clasificación legacy por forma de transferencia, el teclado es un dispositivo:",
  "De carácter", ["De bloque", "De salida", "De almacenamiento"],
  "De carácter: byte por byte (teclado, mouse). De bloque: tamaño fijo (almacenamiento)."),
 (6, "Según la clasificación actual por función, una tarjeta gráfica es un dispositivo:",
  "De entrada/salida", ["De entrada", "De salida", "De bloque"],
  "E/S: tarjetas gráficas y discos. Entrada: teclado, mouse. Salida: pantallas, bocinas."),
 (6, "¿Qué registro de E/S indica si el dispositivo está suspendido, ocupado, encendido, listo o en error?",
  "El registro de estado", ["El registro de control", "El registro de datos", "El puerto de E/S"],
  "Control: comandos del CPU. Datos: información leída/escrita. Estado: situación actual."),
 (6, "Los drivers (controladores) de un dispositivo se ubican:",
  "Dentro del componente lógico del dispositivo",
  ["En el componente físico o mecánico", "En la MMU", "En el registro de datos"],
  "El componente lógico es el «cerebro»: chip o tarjeta con su lógica, controlador y búferes."),
 # Tema 7
 (7, "¿Qué se necesita para que exista paralelismo real?",
  "Varios procesadores o varios núcleos",
  ["Un cambio de contexto muy rápido", "Un solo núcleo con multiprogramación", "Una interfaz gráfica"],
  "Paralelismo: exactamente al mismo tiempo. La concurrencia sí funciona con un solo núcleo."),
 (7, "Tanenbaum llama pseudoparalelismo a:",
  "La apariencia de paralelismo que da la CPU al conmutar con rapidez entre procesos",
  ["La ejecución simultánea en varias CPU que comparten memoria", "El almacenamiento de trabajos en disco", "La división de la memoria en páginas"],
  "Tanenbaum, p. 114: se distingue del paralelismo real de los multiprocesadores."),
 (7, "Según Tanenbaum (p. 57), un cambio de contexto puede ser costoso porque:",
  "Puede exigir vaciar bloques modificados de la caché y actualizar los registros de la MMU",
  ["Obliga a reiniciar la BIOS", "Borra el contenido del disco", "Cierra todos los archivos abiertos"],
  "Por eso los programadores procuran evitarlo."),
 # Tema 8
 (8, "El emulador de terminal se comunica con la shell mediante:",
  "Una pseudoterminal (pty)", ["La variable PATH", "La consola virtual tty1", "El registro de datos de E/S"],
  "El emulador dibuja texto y captura el teclado; no ejecuta comandos por sí mismo."),
 (8, "Si un comando no es alias, función ni builtin, la shell:",
  "Lo busca en el PATH y lo ejecuta",
  ["Lo envía a la BIOS", "Lo muestra en pantalla sin ejecutarlo", "Lo guarda en /etc/passwd"],
  "La shell divide la cadena, expande variables/comodines/redirecciones/pipes y luego busca en el PATH."),
 (8, "POSIX es:",
  "Un estándar para que los distintos shells manejen la misma terminología y comandos",
  ["Un shell escrito por Zhong Shao", "Un sistema de archivos de Linux", "Un tipo de interfaz natural de usuario"],
  "POSIX da una experiencia similar al usuario entre shells distintos."),
 (8, "La NUI (Natural User Interface) se caracteriza por:",
  "Eliminar el uso de periféricos y apoyarse en movimientos naturales y la voz",
  ["Usar ventanas y botones", "Funcionar solo con comandos de texto", "Requerir una pseudoterminal"],
  "GUI: visual con botones. NUI: manos, brazos, dedos, voz."),
 # Tema 9
 (9, "Según las notas, un usuario es:",
  "Una entidad (persona, proceso o dispositivo) con una identidad digital que determina sus permisos y nivel de acceso",
  ["Únicamente una persona con nombre de usuario y contraseña", "Cualquier proceso que se ejecuta como root",
   "Un conjunto de cuentas con características en común"],
  "No tiene que ser humano. La última opción describe a un grupo."),
 (9, "Los tres principios para autenticar usuarios son algo que el usuario:",
  "Sabe, es y tiene", ["Lee, escribe y ejecuta", "Posee, hereda y comparte", "Pide, recibe y audita"],
  "Sabe (contraseña, PIN), es (biometría), tiene (token, tarjeta). Tanenbaum, p. 672."),
 (9, "¿Cuál es el UID del superusuario (root) en Linux?",
  "0", ["1", "100", "1000"],
  "El superusuario puede saltarse casi todas las reglas de protección (Tanenbaum, pp. 69 y 834)."),
 (9, "Los usuarios de sistema o especiales:",
  "No tienen login ni contraseña, están ligados a los daemons y suelen tener UID entre 1 y 100",
  ["Usan el prompt # y pueden instalar paquetes", "Son usuarios estándar con permisos temporales", "Tienen su espacio de trabajo en /home/usuario"],
  "Son «procesos con permisos». La segunda opción es root; la tercera, invitado; la cuarta, estándar."),
 (9, "¿Por qué se crea un usuario especial para servicios como Apache o MySQL?",
  "Si el servicio se vulnera, el atacante solo puede hacer lo que ese usuario puede hacer",
  ["Para que el servicio pueda saltarse las reglas de protección", "Para que el servicio use el prompt #",
   "Porque el kernel no ejecuta procesos sin contraseña"],
  "Aislamiento de permisos: en los primeros UNIX muchos servicios corrían como root, lo cual era peligroso."),
 (9, "¿Cuál es la diferencia entre `adduser` y `useradd`?",
  "`adduser` es un script interactivo de alto nivel; `useradd` es de bajo nivel y no interactivo",
  ["`useradd` es interactivo; `adduser` no", "`adduser` borra usuarios y `useradd` los crea", "Son idénticos; solo cambia el nombre"],
  "Las dos agregan usuarios desde la línea de comandos."),
 (9, "¿Qué hace `userdel -r usuario`?",
  "Elimina la cuenta y también su directorio de trabajo y sus archivos",
  ["Elimina solo la cuenta y conserva su directorio", "Fuerza el borrado aunque el usuario esté trabajando", "Renombra la cuenta"],
  "`userdel` solo conserva el directorio; `-r` borra todo; `-f` fuerza el borrado."),
 (9, "Un archivo tiene los permisos `rwxr-x---`. ¿Cuál es su valor octal?",
  "750", ["754", "640", "770"],
  "rwx = 4+2+1 = 7; r-x = 4+1 = 5; --- = 0."),
 (9, "El comando `chmod 644 archivo` deja los permisos:",
  "`rw-r--r--`", ["`rwxr--r--`", "`rw-rw-r--`", "`r--r--r--`"],
  "6 = rw-, 4 = r--, 4 = r--."),
 (9, "Después de `sudo groupadd licic`, ¿qué comando vincula un archivo al grupo licic?",
  "`sudo chown :licic archivo`", ["`sudo groupmod -n licic archivo`", "`sudo usermod -aG licic archivo`", "`sudo gpasswd -d licic archivo`"],
  "Procedimiento de clase: crear el grupo, cambiar el grupo propietario con chown y asignar permisos con chmod."),
 # Tema 10
 (10, "¿Cuál es el orden de las capas de un sistema de archivos, de la más alta a la más baja?",
  "Aplicación de usuario → archivo lógico → módulo de organización de archivos → sistema de archivos básico → control de E/S → hardware",
  ["Aplicación de usuario → módulo de organización de archivos → archivo lógico → sistema de archivos básico → control de E/S → hardware",
   "Aplicación de usuario → archivo lógico → módulo de organización de archivos → control de E/S → sistema de archivos básico → hardware",
   "Archivo lógico → aplicación de usuario → sistema de archivos básico → módulo de organización de archivos → control de E/S → hardware"],
  "Las capas altas interactúan con el usuario y las bajas con el hardware."),
 (10, "¿Qué capa del sistema de archivos rastrea el espacio libre y decide dónde colocar los datos nuevos?",
  "Módulo de organización de archivos", ["Archivo lógico", "Sistema de archivos básico", "Control de E/S"],
  "Es el puente entre lo lógico y lo físico. El archivo lógico maneja directorios, nombres, permisos y FCB."),
 (10, "¿Qué sistema de archivos de Microsoft elimina el límite de 4 GB de FAT32, no tiene journaling y no desgasta las memorias flash?",
  "exFAT", ["NTFS", "ext4", "APFS"],
  "exFAT (2006, para Windows Embedded); tu apunte la llama «EXTFAT32»."),
 (10, "En lugar de journaling, APFS usa:",
  "Un esquema redirect-on-write", ["Una tabla MFT", "Dos copias de la tabla FAT", "Bloques de arranque con descriptores de grupo"],
  "Al modificar un archivo escribe en un bloque nuevo libre y actualiza los metadatos."),
 (10, "En ext4, ¿qué dato NO guarda el inodo de un archivo?",
  "El nombre del archivo", ["El propietario", "Los permisos", "La ubicación física en bloques"],
  "El inodo guarda los metadatos, no el nombre."),
 (10, "`/proc`, `/dev` y el registro de Windows son ejemplos de sistemas de archivos:",
  "Virtuales o especiales", ["Locales de disco", "En red o distribuidos", "Con journaling"],
  "Existen solo en RAM o mientras corre un proceso."),
 (10, "¿Qué sistema de archivos en red usa el puerto 22, cifra de extremo a extremo y es más lento que NFS y Samba?",
  "SSHFS", ["NFS", "SMB/Samba", "exFAT"],
  "SSHFS hereda la seguridad de SSH; funciona con FUSE + SFTP."),
 (10, "Samba usa dos demonios, smbd y nmbd. ¿Qué hace nmbd?",
  "Resuelve los nombres de red, para encontrar equipos por nombre en lugar de por IP",
  ["Transfiere archivos, autentica y aplica permisos", "Cifra la conexión con AES", "Monta carpetas remotas con FUSE"],
  "smbd: transferencia, autenticación y permisos."),
 (10, "En `operacionesArchivos.c`, las funciones de escritura abren el archivo con el modo:",
  "`\"a\"`: escribe al final sin borrar lo que hay y, si no existe, lo crea",
  ["`\"w\"`: vacía el archivo antes de escribir", "`\"r\"`: abre solo para leer", "`\"x\"`: abre en modo ejecución"],
  "Las de lectura usan \"r\" (el archivo debe existir). \"w\" no aparece en el programa."),
 (10, "¿Cuál es el error de la función `escribirArchivoPorPalabra` del programa de clase?",
  "`fclose` está dentro del `while`, así que el archivo se cierra después de la primera palabra",
  ["Abre el archivo con el modo `\"r\"`", "No usa `%29s` y puede desbordar el arreglo", "Lee del archivo en lugar de escribir en él"],
  "Escribir en un archivo cerrado es comportamiento indefinido; fclose va una sola vez, después del bucle."),
 (10, "Un archivo de 1000 bytes se guarda en un sistema con bloques de 4096 bytes. ¿Cuánto espacio se desperdicia y qué tipo de fragmentación es?",
  "3096 bytes; fragmentación interna",
  ["3096 bytes; fragmentación externa", "4096 bytes; fragmentación externa", "0 bytes; no hay fragmentación"],
  "Interna = dentro del bloque; externa = entre bloques (huecos de bloques completos)."),
 (10, "¿Qué método de asignación sí sufre fragmentación externa?",
  "La asignación contigua", ["La asignación enlazada", "La asignación indexada", "Ninguno de los tres"],
  "Silberschatz, p. 379. La enlazada y la indexada no la sufren."),
 (10, "¿En qué modelo de control de acceso el propietario del recurso concede o retira los permisos?",
  "DAC (discrecional)", ["MAC (obligatorio)", "RBAC (por roles)", "Dominios de protección"],
  "DAC: los permisos rwx con chmod. MAC: política centralizada. RBAC: permisos por rol."),
 (10, "Si la matriz de control de acceso se lee por columnas, se obtiene:",
  "Una ACL por cada archivo", ["Una lista de capacidades por cada sujeto", "Un mapa de bits del disco", "La tabla de inodos"],
  "Por filas: lista de capacidades (cada fila es un dominio)."),
 (10, "¿Qué hace `setfacl -m u:ana:rw proyecto.txt`?",
  "Crea una entrada de ACL que da a la usuaria ana lectura y escritura sobre proyecto.txt",
  ["Cambia el propietario de proyecto.txt a ana", "Quita a ana todos los permisos sobre proyecto.txt", "Agrega a ana al grupo rw"],
  "-m = modificar; u: = usuario (g: sería grupo). Requiere `sudo apt install acl`."),
]

# Verdadero/falso: (tema, enunciado, valor, justificación)
TF = [
 (2, "La tercera generación de SO coincide con la tercera generación de hardware vista en Organización de computadoras.", False,
  "Son líneas de tiempo distintas: la 3.ª de SO cae en lo que el hardware cuenta como 4.ª."),
 (2, "El tiempo compartido es una variante de la multiprogramación que permite a varios usuarios usar la computadora de forma interactiva mediante pequeños turnos.", True,
  "Aparece en la 3.ª generación, junto con la multiprogramación y el spooling."),
 (3, "Que un SO sea monousuario en su versión comercial implica que su kernel no puede ser multiusuario.", False,
  "Ejemplo: Windows Server."),
 (3, "En un microkernel, los drivers de dispositivos se ejecutan como procesos en espacio de usuario.", True,
  "El kernel solo conserva IPC, planificación básica, memoria mínima e interrupciones."),
 (8, "El emulador de terminal ejecuta los comandos por sí mismo.", False,
  "Los ejecuta la shell; el emulador solo dibuja el texto y captura el teclado."),
 (9, "`/etc/passwd` almacena las contraseñas cifradas de los usuarios.", False,
  "passwd guarda la información básica y pública; las contraseñas con hash están en /etc/shadow."),
 (9, "Los procesos heredan el UID del usuario que los lanzó.", True, "Tanenbaum, p. 69."),
 (9, "`userdel usuario`, sin opciones, borra la cuenta pero conserva su directorio de trabajo.", True,
  "Para borrar también el directorio se usa -r."),
 (9, "`usermod -aG grupo usuario` saca al usuario de todos sus demás grupos.", False,
  "-a (append) lo añade al grupo sin quitarlo de los demás."),
 (10, "El sistema de archivos es lo mismo que el subsistema de almacenamiento secundario.", False,
  "Son subsistemas distintos; el sistema de archivos hace la gestión lógica del almacenamiento."),
 (10, "Según el apunte del profesor, en el mapa de bits de espacio libre un 0 indica bloque libre y un 1, bloque ocupado.", True,
  "Silberschatz usa la convención contraria; en el examen usa la del profesor y escríbela junto al mapa."),
 (10, "En la asignación enlazada, cada bloque apunta al siguiente, y si se daña un enlace es difícil llegar a los bloques que siguen.", True,
  "Además es lenta de recorrer y los punteros ocupan espacio."),
 (10, "En el modelo MAC, el usuario puede cambiar la política de permisos de sus propios archivos.", False,
  "En MAC decide una política centralizada; quien decide en DAC es el propietario."),
 (10, "Una ACL permite dar permisos a un usuario concreto sin cambiar el propietario ni el grupo del archivo.", True,
  "rwx solo distingue propietario, grupo y otros."),
]

# Relación de columnas: (titulo, instrucción, [(concepto, descripción)], distractor)
MATCH = [
 ("Bloque A — Shells", "Relaciona cada shell con su descripción. Sobra una descripción.",
  [("BASH", "Implementa POSIX, es el más usado en Linux y es fuerte en scripting"),
   ("ZSH", "Muy personalizable; es el shell estándar en macOS y en Kali"),
   ("FISH", "Cómodo desde el primer uso, se aleja de POSIX y no se recomienda para scripting de sistema"),
   ("KSH", "Pionero en POSIX; su código se liberó en 2000 tras salir de AT&T"),
   ("TCSH", "Scripting al estilo del lenguaje C; relegado a sistemas heredados")],
  "Estándar que unifica la terminología de los shells (no es un shell)"),
 ("Bloque B — Comandos de Linux", "Relaciona cada comando con lo que hace. Sobra una descripción.",
  [("`passwd usuario`", "Agrega o cambia la contraseña de un usuario que ya existe"),
   ("`ls -l`", "Muestra los atributos, permisos y propietario de archivos y directorios"),
   ("`gpasswd -d usuario grupo`", "Saca al usuario de ese grupo"),
   ("`groupmod -n nuevo antiguo`", "Renombra un grupo"),
   ("`userdel -f usuario`", "Fuerza el borrado de la cuenta aunque el usuario esté trabajando en el sistema")],
  "Crea un grupo nuevo"),
]

# Completar: (tema, texto con ____ , respuesta, justificación)
FILL = [
 (2, "⭐ «La multiprogramación carga en ________; el spooling almacena en ________».", "memoria; disco", "Frase del tema marcado por el profesor."),
 (3, "El kernel de iOS es ________, de tipo UNIX.", "Darwin", "Tabla de SO móviles."),
 (4, "Un ________ es un programa en ejecución.", "proceso", "Gestión de procesos."),
 (6, "En los registros de E/S de ________, el CPU escribe y lee comandos para controlar al dispositivo.", "control", "Los otros dos son de datos y de estado."),
 (9, "El prompt ________ identifica al superusuario y el prompt ________ a un usuario estándar.", "#; $", "Tipos de usuario en Linux."),
 (9, "Un ________ es una expresión lógica para reunir usuarios con características en común.", "grupo", "Se define en /etc/group."),
 (10, "ext4 usa ________ para reducir la fragmentación y ________ para localizar los archivos.", "extents; inodos", "Tabla de tipos de sistemas de archivos."),
 (10, "En la asignación ________, un bloque índice guarda las referencias a todos los bloques de datos del archivo.", "indexada", "Tanenbaum la llama nodo-i (los inodos de ext4)."),
 (10, "La técnica de espacio libre que guarda la dirección del primer bloque libre y cuántos bloques contiguos le siguen se llama ________.", "conteo (o recuento)", "Silberschatz, p. 388. El agrupamiento guarda direcciones de n bloques libres."),
 (10, "Un ________ de protección es el conjunto de recursos y operaciones a los que un usuario o proceso tiene permitido acceder.", "dominio", "Tanenbaum: un conjunto de pares (objeto, permisos)."),
]

assert len(MC) + len(TF) + sum(len(m[2]) for m in MATCH) + len(FILL) == 100, \
    (len(MC), len(TF), len(FILL))

# --------------------------------------------------------------- utilidades
def fmt(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = s.replace("⭐", '<span class="star">★</span>')
    return s.replace("________", '<span class="blank"></span>')

rng = random.Random(2026)
pos = [i % 4 for i in range(len(MC))]
rng.shuffle(pos)
L = "abcd"

mc_items = []
for (tema, q, ok, bad, why), p in zip(MC, pos):
    opts = bad[:]
    rng.shuffle(opts)
    opts.insert(p, ok)
    mc_items.append((tema, q, opts, L[p], ok, why))

match_items = []
for titulo, instr, pares, distr in MATCH:
    descr = [d for _, d in pares] + [distr]
    rng.shuffle(descr)
    letras = {d: L[i] if i < 4 else "ef"[i - 4] for i, d in enumerate(descr)}
    match_items.append((titulo, instr, pares, descr, letras))

CSS = """
@page { size: letter; margin: 1.8cm 1.9cm 1.8cm 1.9cm;
  @bottom-center { content: "Página " counter(page) " de " counter(pages); font-size: 8.5pt; color: #666; } }
body { font-family: "DejaVu Sans", sans-serif; font-size: 9.8pt; line-height: 1.38; color: #111; }
h1 { font-size: 15pt; margin: 0 0 2pt; }
.sub { color: #444; margin: 0 0 10pt; font-size: 10pt; }
.datos { width: 100%; border-collapse: collapse; margin-bottom: 10pt; }
.datos td { padding: 5pt 4pt 2pt; font-size: 9.5pt; }
.datos .l { border-bottom: 0.7pt solid #333; width: 60%; }
.instr { border: 0.8pt solid #999; background: #f4f4f4; padding: 6pt 9pt; margin-bottom: 12pt; font-size: 9pt; }
.instr p { margin: 2pt 0; }
h2 { font-size: 11.5pt; border-bottom: 1.2pt solid #222; padding-bottom: 2pt; margin: 14pt 0 6pt; }
h3 { font-size: 10.5pt; margin: 10pt 0 2pt; }
.q { break-inside: avoid; margin: 0 0 7pt; }
.n { font-weight: bold; }
ol.opts { list-style: none; margin: 2pt 0 0 16pt; padding: 0; }
ol.opts li { margin: 1pt 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.8pt; background: #eee; padding: 0 2pt; }
.blank { display: inline-block; width: 3.2cm; border-bottom: 0.7pt solid #222; }
.tf { display: inline-block; width: 1.4cm; border-bottom: 0.7pt solid #222; margin-right: 4pt; }
.star { color: #b8860b; }
table.match { width: 100%; border-collapse: collapse; margin: 4pt 0 8pt; break-inside: avoid; }
table.match td { vertical-align: top; padding: 3pt 4pt; }
table.match td.c1 { width: 44%; } table.match td.c2 { width: 56%; }
.paren { display: inline-block; width: 0.9cm; }
table.key { width: 100%; border-collapse: collapse; font-size: 8.8pt; }
table.key td, table.key th { border: 0.5pt solid #aaa; padding: 2.5pt 4pt; vertical-align: top; text-align: left; }
table.key th { background: #e8e8e8; }
table.key tr { break-inside: avoid; }
table.key td.r { font-weight: bold; white-space: nowrap; width: 1%; text-align: center; }
table.key td.num { width: 1%; text-align: right; }
table.grid { border-collapse: collapse; margin: 4pt 0 10pt; }
table.grid td { border: 0.5pt solid #888; padding: 2pt 5pt; font-size: 9pt; text-align: center; }
table.grid td.h { background: #e8e8e8; font-weight: bold; }
.nota { font-size: 8.8pt; color: #333; border-left: 2.5pt solid #b8860b; padding: 3pt 8pt; margin: 8pt 0; background: #fbf6e8; }
"""

def head(titulo, extra=""):
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{titulo}</title>
<style>{CSS}</style></head><body>
<h1>{titulo}</h1>
<p class="sub">Examen de práctica · 100 reactivos · Temas 1 a 10{extra}</p>"""

# ----------------------------------------------------------------- examen
n = 0
parts = [head("Primer parcial de Sistemas Operativos")]
parts.append("""<table class="datos"><tr><td>Nombre:</td><td class="l"></td><td>Fecha:</td><td class="l" style="width:22%"></td></tr>
<tr><td>Matrícula:</td><td class="l"></td><td>Aciertos:</td><td class="l">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/ 100</td></tr></table>
<div class="instr"><p><b>Instrucciones.</b> Cada reactivo vale un punto. No se permite consultar apuntes.</p>
<p><b>I.</b> Opción múltiple (1–66): encierra la letra de la única respuesta correcta.
<b>II.</b> Verdadero o falso (67–80): escribe V o F en la línea.
<b>III.</b> Relación de columnas (81–90): escribe en el paréntesis la letra que corresponde.
<b>IV.</b> Completar (91–100): escribe la palabra o palabras que faltan.</p>
<p><span class="star">★</span> marca los temas que el profesor señaló como «tema de examen».</p></div>""")

parts.append("<h2>I. Opción múltiple</h2>")
for tema, q, opts, _, _, _ in mc_items:
    n += 1
    lis = "".join(f"<li>{L[i]}) {fmt(o)}</li>" for i, o in enumerate(opts))
    parts.append(f'<div class="q"><span class="n">{n}.</span> {fmt(q)}<ol class="opts">{lis}</ol></div>')

parts.append("<h2>II. Verdadero o falso</h2>")
for tema, s, v, _ in TF:
    n += 1
    parts.append(f'<div class="q"><span class="n">{n}.</span> <span class="tf"></span> {fmt(s)}</div>')

parts.append("<h2>III. Relación de columnas</h2>")
for titulo, instr, pares, descr, letras in match_items:
    parts.append(f"<h3>{titulo}</h3><p style='margin:0 0 3pt'>{instr}</p><table class='match'>")
    filas = max(len(pares), len(descr))
    for i in range(filas):
        c1 = ""
        if i < len(pares):
            n += 1
            c1 = f'<span class="n">{n}.</span> <span class="paren">(&nbsp;&nbsp;&nbsp;&nbsp;)</span>{fmt(pares[i][0])}'
        c2 = f"{letras[descr[i]]}) {fmt(descr[i])}" if i < len(descr) else ""
        parts.append(f"<tr><td class='c1'>{c1}</td><td class='c2'>{c2}</td></tr>")
    parts.append("</table>")

parts.append("<h2>IV. Completar</h2>")
for tema, s, _, _ in FILL:
    n += 1
    parts.append(f'<div class="q"><span class="n">{n}.</span> {fmt(s)}</div>')
parts.append("</body></html>")
assert n == 100
HTML(string="".join(parts)).write_pdf(f"{OUT}/Examen primer parcial - Sistemas Operativos.pdf")

# ------------------------------------------------------------------ clave
n = 0
k = [head("Clave de respuestas", " · Hoja de respuestas")]
# rejilla rápida
k.append("<h2>Respuestas rápidas</h2>")
rapido = []
for _, _, _, letra, _, _ in mc_items:
    rapido.append(letra)
for _, _, v, _ in TF:
    rapido.append("V" if v else "F")
for _, _, pares, _, letras in match_items:
    for c, d in pares:
        rapido.append(letras[d])
for _, _, r, _ in FILL:
    rapido.append("ver IV")
k.append("<table class='grid'>")
for fila in range(0, 90, 15):
    k.append("<tr>" + "".join(f"<td class='h'>{i+1}</td>" for i in range(fila, fila + 15)) + "</tr>")
    k.append("<tr>" + "".join(f"<td>{rapido[i]}</td>" for i in range(fila, fila + 15)) + "</tr>")
k.append("</table>")
cuenta = {l: rapido[:66].count(l) for l in L}
k.append(f"<p style='font-size:8.5pt;color:#555'>Reparto de respuestas en opción múltiple: "
         + ", ".join(f"{l}) {c}" for l, c in cuenta.items()) + ". Verdadero: "
         + f"{rapido[66:80].count('V')}, falso: {rapido[66:80].count('F')}.</p>")

k.append("<h2>I. Opción múltiple</h2><table class='key'><tr><th>#</th><th>Resp.</th><th>Tema</th><th>Respuesta y por qué</th></tr>")
for tema, q, opts, letra, ok, why in mc_items:
    n += 1
    k.append(f"<tr><td class='num'>{n}</td><td class='r'>{letra}</td><td class='num'>{tema}</td><td>{fmt(ok)}. <span style='color:#444'>{fmt(why)}</span></td></tr>")
k.append("</table>")

k.append("<h2>II. Verdadero o falso</h2><table class='key'><tr><th>#</th><th>Resp.</th><th>Tema</th><th>Por qué</th></tr>")
for tema, s, v, why in TF:
    n += 1
    k.append(f"<tr><td class='num'>{n}</td><td class='r'>{'V' if v else 'F'}</td><td class='num'>{tema}</td><td>{fmt(why)}</td></tr>")
k.append("</table>")

k.append("<h2>III. Relación de columnas</h2><table class='key'><tr><th>#</th><th>Resp.</th><th>Concepto</th><th>Descripción</th></tr>")
for titulo, _, pares, descr, letras in match_items:
    for c, d in pares:
        n += 1
        k.append(f"<tr><td class='num'>{n}</td><td class='r'>{letras[d]}</td><td>{fmt(c)}</td><td>{fmt(d)}</td></tr>")
    sobra = [d for d in descr if d not in dict((b, a) for a, b in pares)][0]
    k.append(f"<tr><td></td><td class='r'>{letras[sobra]}</td><td colspan='2' style='color:#555'><i>Sobra en el {titulo.split(' —')[0].lower()}:</i> {fmt(sobra)}</td></tr>")
k.append("</table>")

k.append("<h2>IV. Completar</h2><table class='key'><tr><th>#</th><th>Respuesta</th><th>Tema</th><th>Nota</th></tr>")
for tema, s, r, why in FILL:
    n += 1
    k.append(f"<tr><td class='num'>{n}</td><td class='r' style='text-align:left'>{fmt(r)}</td><td class='num'>{tema}</td><td>{fmt(why)}</td></tr>")
k.append("</table>")

k.append("""<div class="nota"><b>Dos dudas abiertas en tus notas que afectan a este examen.</b>
(1) Reactivo 19: tu apunte original invierte simétrico y asimétrico; la clave sigue al temario corregido con Tanenbaum (p. 566).
(2) Reactivo 77: la clave usa la convención del profesor para el mapa de bits (0 = libre), aunque Silberschatz usa la contraria.
Las dos están en tu lista de preguntas para el profesor.</div>""")
k.append("</body></html>")
assert n == 100
HTML(string="".join(k)).write_pdf(f"{OUT}/Examen primer parcial - Sistemas Operativos - Respuestas.pdf")
print("ok", cuenta)
