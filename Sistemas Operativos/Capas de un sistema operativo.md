#review 
Recordando que un sistema operativo es en realidad un conjunto de capas que funcionan al unisono, podemos reducir los sistemas de un OS en 8 subsistemas 

## Kernel o nucleo
El corazon del sistema, donde (dependiendo del sistema operativo ya sea monolito o microkernel) puede construirse sobre el kernel, o vivir dentro del kernel.
##  Subsistema de entrada y salida
La entrada y salida no solamente corresponde a los perifericos, sino tambien a tarjetas graficas, de red, dipositivos de almacenamiento secundario (notese, que el almacenamiento principal no forma parte de esta seccion, ni el CPU), basicamente cualquier cosa que permita al PC comunicarse al exterior o con el usuario.

La BIOS (BASIC INPUT OUTPUT SYSTEM) la cual se encuentra integrada directamente en la tarjeta madre, es una herramienta de  firmware utilizada por la cpu con la funcion de inicializar la comunicacion y diagnostico de los sistemas de entrada y salida. Antes de que el sistema operativo se encienda completamente, la BIOS corre un test de integridad tanto en el propio CPU, como en los sistemas basico RAM Y GPU.  Luego usa drivers genericos basico que tiene cargados para controlar la pantalla y leer el teclado (en algunas bios, las mas modernas, utliza el mouse tambien), busca en el almacenamiento secundario alguna unidad de arranque de un sistema operativo y la carga.

Luego, el sistema operativo se ocupa de tomar el control de los dispositivos de entrada y salida, con sus propios drivers (o los cargados por el usuario) coordinandolo todo sin que el usuario tenga que lidiar con los programas particulares de cada hardware


## Subsistema de gestion de procesos
Ver [[Gestion de procesos]]
La capa del sistema que se ocupa de gestionar como cada proceso interactua en el sistema, ya sea con otros procesos, o de forma solitaria.
- Inicializa procesos
- Pausa procesos
- Reanuda procesos
- Cierra procesos
- Comunicacion y sincronizacion de procesos
	- Piplines
	- Paso de mensaje
	- Memoria compartida
	- Sockets
- Gestiona la situacion de interbloqueo (deadlock
- Aqui se asigna el tiempo de cpu o rafaga de cpu a cada proceso
- Aqui es donde vive la multiprogramacion, paralelismo y la concurrencia.
- Mecanismos de seguridad para no matar procesos criticos
- Planificacion de uso de cpu  (mediante el planificador de cpu)

## Subsistema de gestion de memoria
Ver [[Gestion de memoria]]
Se encarga de orquestar el recurso de la memoria a los diferentes procesos que hay en el sistema operativo debido a que la memoria es un recurso compartido y LIMITADO. Su hardare es el MMU
- Asignar espacios de memoria
- Limpiar espacios de memoria
- Manejar la memoria virtual
- Quien usa la memoria en ese momento
- Proteger la memoria de accesos no autorizados (accidentales o no) por parte de un proceso
- Planificacion de acceso a memoria

## Administracion de almacenamiento secundario
Encargado de manejar como los procesos escriben datos en una memoria persistente, quien cuando como y donde, protegiendo igualmente de accesos no autorizados. Gestiona las solicitudes de acceso.
- Quien y cuando puede accesar a escribir o leer en almacenamiento secundario
- Administrar el espacio libre y ocupado
- Mecanismos de seguridad
- Planificacion de disco para atender


## Subsistema de archivos
Para que el usuario se pueda mover en el almacenamiento secundario de una forma fluida y amigable (dependiendo del OS) , se ideo un sistema de archivos, donde cada archivo o dato se puede encontrar en un "lugar especifico (ruta o direccion)" dentro de un explorador de archivos. Protegiendo ciertos archivos (en windows, protegiendo los archivos mas criticos para el funcionamiento del sistema), solicitudes de acceso 
- Crear y eliminar archivos
- Leer archivos
- Modificar archivos
- Administrar directorios
- Busqueda de archivos
- NTFS (New technology file system)
	- Sistema usado desde windows XP
	- Tiene journaling
		- Escribir todos los cambios antes de ser realizados, para tener integridad de archivos en caso de apagones o casos inesperados
	- Maneja hasta 16 tb de informacion ya sea por archivo o por tamano entero de disco, sin embargo, si lo configuras bien, teoricamente puedes tener archivos de hasta 8 petabytes
- FAT32
	- Sistema implementado en los noventas
	- Legacy
	- Hasta 32 gb (teoricamente hasta 2 tb)
	- Tamano maximo de archivo de 4 gb
- ext4
	- El sistema mas usado en distribuciones linux
	- Tiene journaling
		- Mas complejo que NTFS, integridad de datos robusta
	- Tamano maximo de archivo de 16 tb (teorico de miles de tbs)

## Subsistema de gestion de redes y comunicaciones
Encargado de que la computadora pueda comunicarse con otras computadoras en una misma red, o en una red aparte. Su componente de hardware son las tarjetas de red

- Protocolos TCP IP
- Proteccion en las comuniaciones
- Enviar y recibir paquetes de datos
- administrar interfaces de red (tarjeta de red
- Gestionar conexiones de red

## Subsistema de interfaz de usuario 
Encargado de manejar ya sea la GUI o la CLI,funcionando como el puente entre el SO y el usuario, manteniendo un lenguaje mas comprensible por los humanos.
- Recibir input por parte del usuario
- Dar output sobre lo que esta sucediendo dentro de la computadora al usuario
- Gestionar ventanas e interfaces graficas
- Facilitar el uso de los servicios y subsistemas anteriores
- Proporcionar notificaciones y gestioanr la comunicacion de errores