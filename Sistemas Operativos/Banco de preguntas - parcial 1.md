---
materia: Sistemas Operativos
semestre: 3
tipo: ejercicios
tags: [examen, parcial, recuperar]
---

# Banco de preguntas — parcial 1

Preguntas de autoevaluación por tema para los calentamientos de «Recuperar», los colchones y el simulacro del [[Temario primer parcial - Sistemas Operativos|temario]]. Contesta **sin apuntes**, en voz alta o en papel, y después compara con las soluciones. Lo que falles va al [[Temario primer parcial - Sistemas Operativos#Registro de fallos|registro de fallos]].

## Tema 1 — Introducción a los sistemas operativos

1. ¿Qué tienen en común las tres definiciones de SO vistas en clase (Tanenbaum, Silberschatz, profesor)?
2. ¿Cuál es la función que distingue a un SO de simplemente "ejecutar programas"?
3. Explica la diferencia de énfasis entre la definición de Tanenbaum y la de Silberschatz.
4. Nombra los tres componentes básicos de un SO según el esquema shell/kernel/hardware.
5. ¿Qué característica del SO permite que se adapte a distinto hardware?
6. Da dos ejemplos de funciones esenciales de un SO además de proteger recursos.

## Tema 2 — Historia: generaciones de sistemas operativos

1. ¿Qué distingue a la multiprogramación del spooling?
2. ¿En qué generación aparecen la multiprogramación y el spooling?
3. ¿Qué tecnología sustituyó al tubo de vacío en la 2ª generación?
4. ¿Por qué no hay que mezclar la numeración de generaciones de SO con la de Organización de Computadoras?
5. ¿Qué generación introduce las interfaces gráficas *user friendly*?
6. ¿Qué tres sistemas operativos móviles nacen en la 5ª generación?

## Tema 3 — Tipos de sistemas operativos

1. ¿Cuáles son los tres criterios de clasificación de SO vistos en clase?
2. ¿Qué diferencia a un sistema de tiempo real duro de uno blando?
3. ¿Por qué Windows Server puede ser multiusuario sin cambiar su kernel?
4. Compara multiprocesamiento simétrico y asimétrico.
5. ¿Qué arquitectura (monolítica/microkernel/híbrida) usa Linux, y cuál su mayor riesgo?
6. Según Tanenbaum, ¿qué tres servicios ofrece típicamente un SO de mainframe?

## Tema 4 — Capas o subsistemas de un SO

1. Enumera los ocho subsistemas de un SO.
2. ¿Qué es un quantum?
3. ¿Qué pasa en un cambio de contexto cuando el CPU regresa a una tarea que había dejado?
4. ¿Qué es la MMU y por qué existe?
5. Explica la diferencia entre memoria virtual y paginación.
6. ¿Qué subsistema gestiona el espacio libre/ocupado del disco y la planificación de acceso a él?

## Tema 5 — Consideraciones para la instalación de un SO

1. ¿Qué hipervisor pedía el enunciado de la práctica 1.1 y cuál usaste?
2. ¿Cuál es la diferencia esencial entre un hipervisor de tipo 1 y uno de tipo 2?
3. ¿Qué particiones hiciste y con qué esquema?
4. Según el enunciado, ¿cuántos núcleos y cuánta RAM mínima se requieren?
5. Nombra cuatro tareas de post-instalación.
6. ¿Qué distribución e idioma se usaron en la instalación de la práctica?

## Tema 6 — Dispositivos de entrada y salida

1. ¿Qué diferencia hay entre el componente físico y el componente lógico de un dispositivo de E/S?
2. Da un ejemplo de dispositivo "de bloque" y uno "de carácter" (clasificación legacy).
3. ¿Qué tipo de dispositivo según la clasificación actual son las tarjetas gráficas?
4. ¿Qué información guarda el registro de estado de un dispositivo E/S?
5. ¿Para qué sirven los puertos o direcciones E/S?
6. ¿Dónde vive el driver de un dispositivo?

## Tema 7 — Concurrencia y paralelismo

1. ¿Qué necesita existir en hardware para que haya paralelismo real?
2. Según Tanenbaum, ¿qué logra un proceso aun con una sola CPU disponible?
3. ¿Cómo distingue Tanenbaum el pseudoparalelismo del paralelismo real?
4. ¿Qué relación tiene la multiprogramación con el paralelismo aparente?
5. ¿Qué operación costosa dispara un cambio de contexto según Tanenbaum?

## Tema 8 — Interfaces de usuario

1. ¿Qué diferencia hay entre una terminal, un emulador de terminal y una shell?
2. ¿Qué es POSIX?
3. ¿Qué shell es el más usado en Linux y por qué?
4. ¿Qué shell se aleja más de POSIX por buscar comodidad desde el primer uso?
5. Diferencia entre GUI y NUI.
6. ¿Qué shell es el estándar en macOS y en Kali Linux?

## Tema 9 — Manejo de usuarios

1. ¿Qué son los tres principios en los que se basa la autenticación de un usuario?
2. ¿Cuál es el UID típico del superusuario en Linux y cómo se llama?
3. ¿Qué diferencia a `useradd` de `adduser`?
4. Un archivo tiene permisos `rwxr-xr--`. Da su valor en octal.
5. Quieres que un archivo sea `rw-r--r--` con `chmod` numérico. ¿Qué comando usas?
6. Escribe el comando para añadir el usuario `ana` al grupo `licic` sin sacarla de sus otros grupos.
7. ¿Qué diferencia hay entre `userdel usuario` y `userdel -r usuario`?
8. ¿Qué archivo guarda las contraseñas cifradas (hash) de los usuarios y cuál guarda la información básica/pública de las cuentas?

### Comandos para practicar en la VM Debian 13

1. `sudo adduser practica1` — crear un usuario de forma interactiva.
2. `sudo useradd -m practica2` — crear un usuario de bajo nivel (con `-m` para que sí cree `/home`).
3. `sudo passwd practica1` — asignar/cambiar su contraseña.
4. `sudo usermod -aG sudo practica1` — añadirlo a un grupo existente sin sacarlo de los demás.
5. `groups practica1` — verificar a qué grupos pertenece.
6. `sudo groupadd licic` — crear un grupo nuevo.
7. `sudo chown :licic archivo_de_prueba` — cambiar el grupo propietario de un archivo.
8. `ls -l archivo_de_prueba` — leer propietario, grupo y permisos.
9. `chmod 750 archivo_de_prueba` y luego `chmod g-w,o-r archivo_de_prueba` — practicar el modo numérico y el simbólico sobre el mismo archivo.
10. `sudo userdel -r practica2` — eliminar un usuario junto con su `/home`.


## Tema 10 — Sistema de archivos

1. ¿Qué es un sistema de archivos?
2. Nombra tres metadatos que el sistema de archivos guarda sobre cada archivo.
3. Ordena las capas del sistema de archivos de la más alta a la más baja.
4. Vas a formatear una memoria USB de 256 GB que debe poder usarse tanto en Windows como en macOS y Linux, con archivos de más de 4 GB. ¿Qué sistema de archivos eliges y por qué no FAT32?
5. ¿Qué sistema de archivos de red es nativo de Unix/Linux y usa RPC sobre un solo puerto TCP?
6. Quieres editar en tu laptop, en tiempo real, el código que vive en un servidor remoto, usando solo una conexión SSH ya existente. ¿Qué montas?
7. ¿Qué estructura central usa NTFS para guardar los metadatos de cada archivo?
8. ¿Qué usa ext4 para reducir la fragmentación del disco y qué usa para encontrar un archivo?

---
---
---

## Soluciones

### Tema 1 — Introducción a los sistemas operativos

1. Las tres coinciden en que el SO **administra recursos**.
2. **Proteger recursos**, de usuarios y de otros programas.
3. Tanenbaum enfatiza la intermediación con el hardware; Silberschatz, el servicio a las aplicaciones.
4. Shell (interfaz), kernel (comunicación hardware-software) y hardware.
5. La **portabilidad**.
6. P. ej. gestionar memoria y gestionar procesos.

### Tema 2 — Historia: generaciones de sistemas operativos

1. Multiprogramación carga varios trabajos en memoria; spooling los almacena en disco.
2. En la 3ª (1965–1980).
3. El **transistor**.
4. Porque no coinciden: la 3ª de SO cae dentro de la 4ª de hardware.
5. La 4ª (1980–1990), con las PC.
6. Android, iOS y HarmonyOS.

### Tema 3 — Tipos de sistemas operativos

1. Tipo de sistema informático, servicios/capacidades, estructura interna.
2. El duro exige respuesta obligatoria en una ventana mínima (riesgo grave si falla); el blando admite un pequeño retraso.
3. Porque ser monousuario comercial no implica que el kernel carezca de capacidades multiusuario.
4. Asimétrico: un procesador maestro dirige a los esclavos; simétrico: todos los procesadores son iguales y cualquiera ejecuta el SO (ojo: el apunte los tiene al revés).
5. Monolítica; si algo falla, falla todo el kernel.
6. Procesamiento por lotes, procesamiento de transacciones y tiempo compartido.

### Tema 4 — Capas o subsistemas de un SO

1. Kernel, E/S, gestión de procesos, gestión de memoria, almacenamiento secundario, sistema de archivos, redes y comunicaciones, interfaz de usuario.
2. La cantidad de milisegundos que el CPU asigna a una tarea.
3. La reanuda desde el momento exacto en que se quedó.
4. El componente de hardware que traduce el mapa virtual de memoria a direcciones físicas; existe para bajar la carga lógica del CPU.
5. La memoria virtual es el concepto/ilusión; la paginación es la técnica que la implementa.
6. Administración de almacenamiento secundario.

### Tema 5 — Consideraciones para la instalación de un SO

1. El enunciado pedía uno de tipo 2 (VirtualBox); usaste QEMU/KVM con virt-manager.
2. El tipo 1 corre directo sobre el hardware (es en la práctica el propio SO en modo kernel); el tipo 2 corre como aplicación sobre un SO anfitrión.
3. MBR: `/` 25 GB ext4 primaria, `/home` 21 GB ext4 lógica, `swap` 7.7 GB lógica.
4. 4 núcleos y 1–2 GB de RAM.
5. Actualizar el sistema, configurar sudo, verificar la red, endurecimiento básico, snapshot, guest agent, controladores virtio.
6. Debian 13, español (México), teclado latinoamericano.

### Tema 6 — Dispositivos de entrada y salida

1. El físico es lo tocable; el lógico es el chip/tarjeta con su propia lógica, controlador y a veces memoria/búferes.
2. Almacenamiento (bloque); teclado o mouse (carácter).
3. De entrada/salida.
4. Si está suspendido, ocupado, encendido, listo o en error.
5. Dan a cada registro una dirección única para que el SO sepa con quién habla.
6. Dentro de su componente lógico.

### Tema 7 — Concurrencia y paralelismo

1. Varios procesadores, o varios núcleos de un procesador.
2. Operar (pseudo)concurrentemente, convirtiendo una CPU en varias CPU virtuales.
3. El pseudoparalelismo es apariencia por conmutación rápida entre procesos en una sola CPU; el real requiere varias CPUs que comparten memoria física.
4. La multiprogramación es el mecanismo que, conmutando rápido entre procesos, produce esa apariencia de paralelismo.
5. Puede exigir vaciar bloques modificados de la caché y actualizar los registros de la MMU.

### Tema 8 — Interfaces de usuario

1. La terminal es el dispositivo/consola que solo envía y recibe texto; el emulador la imita en un entorno gráfico y se comunica con la shell por una pty; la shell interpreta y ejecuta los comandos.
2. El estándar que da a los shells una terminología y comandos comunes.
3. BASH, por ser histórico desde los 80, muy documentado y con scripts portables.
4. FISH.
5. GUI es visual con botones; NUI elimina periféricos y usa movimientos naturales (manos, voz).
6. ZSH.

### Tema 9 — Manejo de usuarios

1. Algo que sabe, algo que es, algo que tiene.
2. UID 0, root.
3. `useradd` es de bajo nivel y no interactivo; `adduser` es un script de alto nivel e interactivo.
4. 754.
5. `chmod 644 archivo`.
6. `usermod -aG licic ana`.
7. El primero borra la cuenta pero conserva su directorio de trabajo; el segundo borra también el directorio y sus archivos.
8. `/etc/shadow` las contraseñas; `/etc/passwd` la info básica.

### Tema 10 — Sistema de archivos

1. El subsistema del SO que organiza, almacena y gestiona la información en un dispositivo de almacenamiento de forma lógica y estructurada.
2. Cualquiera tres de: ubicación, tamaño, tipo, si está en uso, fechas de creación/modificación, permisos.
3. Aplicación de usuario → archivo lógico → módulo de organización de archivos → sistema de archivos básico → control de E/S → hardware.
4. exFAT; FAT32 limita cada archivo a 4 GB.
5. NFS.
6. SSHFS.
7. La MFT (tabla maestra de archivos).
8. *Extents* para la fragmentación; inodos para localizar el archivo.

