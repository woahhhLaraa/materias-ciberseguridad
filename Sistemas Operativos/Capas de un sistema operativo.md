Recordando que un sistema operativo es en realidad un conjunto de capas que funcionan al unisono, podemos reducir los sistemas de un OS en 8 subsistemas 
#review 
## Kernel o nucleo
El corazon del sistema, donde (dependiendo del sistema operativo ya sea monolito o microkernel) puede construirse sobre el kernel, o vivir dentro del kernel.
##  Subsistema de entrada y salida
La entrada y salida no solamente corresponde a los perifericos, sino tambien a tarjetas graficas, de red, dipositivos de almacenamiento secundario (notese, que el almacenamiento principal no forma parte de esta seccion, ni el CPU), basicamente cualquier cosa que permita al PC comunicarse al exterior o con el usuario.

La BIOS (BASIC INPUT OUTPUT SYSTEM) la cual se encuentra integrada directamente en la tarjeta madre, es una herramienta de  firmware utilizada por la cpu con la funcion de inicializar la comunicacion y diagnostico de los sistemas de entrada y salida. Antes de que el sistema operativo se encienda completamente, la BIOS corre un test de integridad tanto en el propio CPU, como en los sistemas basico RAM Y GPU.  Luego usa drivers genericos basico que tiene cargados para controlar la pantalla y leer el teclado (en algunas bios, las mas modernas, utliza el mouse tambien), busca en el almacenamiento secundario alguna unidad de arranque de un sistema operativo y la carga.

Luego, el sistema operativo se ocupa de tomar el control de los dispositivos de entrada y salida, con sus propios drivers (o los cargados por el usuario) coordinandolo todo sin que el usuario tenga que lidiar con los programas particulares de cada hardware

Los dispositivos de entrada y salida los clasificamos como

### De bloque (legacy)

Aquellos dispositivos que mueven cantidades de tamano fijo, normalmente dipositivos de almacenamiento.
### De caracter (Legacy)
Aquellos que mueven datos byte por byte, como un teclado o un mouse.

### Por su funcion
Las clasificaciones anteriores, si bien no son incorrectas, han dejado de aplicar a todos los dispositivos ES de la actulidad por lo que se ha empezado a adoptar las siguientes clasificaciones
#### De entrada
Aquellos que reciben informacion pero no mandan informacion
- Teclado
- Mando
- Mouse
#### De salida
Aquellos que permiten comunicarse con el exterior, sin recibir nada.
- Pantallas
- Bocinas
#### Entrada/Salida
Aquellos que pueden hacer las dos cosas
- Tarjetas graficas
- Discos de almacenamiento
## Subsistema de gestion de procesos
Ver [[Gestion de procesos]]
La capa del sistema que se ocupa de gestionar como cada proceso interactua en el sistema, ya sea con otros procesos, o de forma solitaria.
- Inicializa procesos
- Pausa procesos
- Reanuda procesos
- Cierra procesos
- Comunicacion y sincronizacion de procesos
- Gestiona la situacion de interbloqueo (deadlock
- Aqui se asigna el tiempo de cpu o rafaga de cpu a cada proceso
- Aqui es donde vive la multiprogramacion, paralelismo y la concurrencia.
- Mecanismos de seguridad para no matar procesos criticos

## Subsistema de gestion de memoria
Ver [[Gestion de memoria]]
Se encarga de orquestar el recurso de la memoria a los diferentes procesos que hay en el sistema operativo debido a que la memoria es un recurso compartido y LIMITADO
- Asignar espacios de memoria
- Limpiar espacios de memoria
- Manejar la memoria virtual
- Proteger la memoria de accesos no autorizados (accidentales o no) por parte de un proceso

## Administracion de almacenamiento secundario
Encargado de manejar como los procesos escriben datos en una memoria persistente, quien cuando como y donde, protegiendo igualmente de accesos no autorizados. Gestiona las solicitudes de acceso.


## Subsistema de archivos
Para que el usuario se pueda mover en el almacenamiento secundario de una forma fluida y amigable (dependiendo del OS) , se ideo un sistema de archivos, donde cada archivo o dato se puede encontrar en un "lugar especifico" dentro de un explorador de archivos. Protegiendo ciertos archivos (en windows, protegiendo los archivos mas criticos para el funcionamiento del sistema), solicitudes de acceso 
- Crear y eliminar archivos
- Leer archivos
- Modificar archivos
- Administrar directorios
- Los 

## Subsistema de gestion de redes y comunicaciones


## Subsistema de interfaz de usuario 