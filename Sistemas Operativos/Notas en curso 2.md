27 de agosto

Capas o subsistemas de un sistema operativo
El SO es un conjunto de susbsistemas que se comunican entre si para dar la impresion de que es una unica entidad

En representaciones las vemos como capas una encima de la otra, pero en la realidad son sistemas que se comunican entre si y no tienen porque estar completamente serparadas

- Nucleo (Kernel) el corazon del sistema operativo, todo se construye encima de este kernel
	- Nosotros los usuarios no tenemos acceso al kernel, solo a la capa de aplicacion o capa usuario
	- Linux en realidad es el puro kernel, las distribuciones para usuario final son solo eso, distribuciones hechas encima del kernel
	- Se encarga de manejar el hardware comunicandose directamente con el
		- Cpu
		- Memoria
		- Discos
		- Dispositios IO
- Subsistema de entrada salida
	- Se encarga de las comunicaciones con otros dispositivos, sus procesos.
	- Usando BIOS (Investigar)
	- Discos
	- Teclado
	- Raton
	- Impresoras
	- Pantallas
	- Tarjetas de red
	- El objetivo es proporcionar una forma uniforme de utilizar los dispositivos, ocultando a los programas las particulares de cada hardware
		- Controlar y coordinar el acceso a dipositios IO
		- Gestionar los drivers
		- Administrar solicitudes cuando varios procesos utilizan un solo dispositivo IO
		- Almacenamiento temporal como buferes y cache (investigar diferencias, y como pueden ser software o hardware) para un mejor rendimiento
- Subsistema de Gestion de procesos
	- Administra los procesos y proporcionar los servicios necesarios para que puedan ejecutarse
	- Crea y finaliza procesos
	- Suspender y reaundar procesos
	- Sincronizacion entre procesos
	- Comunicacion entre procesos
	- Prevenir y gestoinar situaciones de interbloqueo (deadlock)
	- Asignar  y administrar el tiempo de cpu entre los procesos
	- Mecanismos de seguridad para no matar procesos criticos
	- Para que un proceso se pueda comunicar de ocupa 
		- Memoria compartida
		- paso de mensaje
		- tuberias
		- sockets
- Subsistema de Gestion de memoria
	- La memoria ram es un recurso limitado compartido, es el area donde se mantienen temporalmente los programas y datos que estan siendo utiliazados por el sistema y los procesos del usuario
	- Controla quien usa la memoria y como
	- Decidir que procesos deben cargarse en memoria cuando el espacio disponible no es suficiente para todos
	- Asignar espacio de memoria a los procesos cuando lo necesitan y liberar el esapcio cuando un proceso terminar
	- Proteccion de la memoria para que otro no lee o escriba memoria que no le pertence
	- Gestionar la memoria virtual, permitiendo que los procesos utilicen mas memoria de la que fisicamente esta disponible mediante tecnicas como la paginacion o segmentacion
- Administracion de almacenamiento secundario
	- La ram es volatil y de capacidad limitada, por lo que lo sistemas utilizan dispositivos de almacenamiento secundario como discos HDD y SDD
	- Administra el espacio libre y ocupado del dispositivo de almacenamiento
	- Asignar espacio par aalmacenar archivos y otros datos
	- Gestionar soliciutdes de acceso
	- Implementar mecanisnmos de seguridad de lectura escritura o ejecucion
	- Planificacion de disco para atender solicitudes
- Subsistema de archivos
	- NFTS, FAT32, ext4
	- Proporciona una forma estandar y organizada de como tratar la info que almacenamos en el almacenamiento secundario
	- Crear y elimina archivos
	- Abrir y cerrar archivos
	- Leer archivo
	- Escribir y modificar archivos
	- Crear y administrar directorios
	- Controlar los permisos de acceso a archivos y directorios
- Subsistema de gestion de redes  y comunicaciones
	- Componente del OS que proporcina mecanismos para que el equipo pueda comunicarse co notros dispositivos en otras redes
		- Administrar interfaces de red
		- Gestionar conexiones de red
		- Enviar y recibir paquetes de datos
		- Usar protocolos como TCP IP
		- Proteccion en las comunicaciones de red
		- Administrar configuraciones, direcciones ip, rutas y dns
- Subsistema de interfaz de usuario
	- Permite al usuario interactuar con el sistema operativo y utilizar sus servicios y recursos,
		- Proporciona interfaces para que el usuari pueda interactuar con el sistema
		- Gestionar la comunicacion con el usuario
		- Gestionar ventanas e interfaz grafica
		- Facilitar la manipulacion de archivos y directorios
		- Facilitar la configuracion y administracion del sistema
		- Proportcionar notificaciones y gestionar la comunicacion de errores

Dispositivos de entrada/salida E/S
Aquellos que permiten a la computadora pueda recibir informacion o enviarla hacia el exterior
Se administra mediante el subsistema de entrada y salida

Los clasificamos como
- Dispositivos de bloque
	- Discos de almacenamiento secundario, pues guardan bloques grandes de datos cada uno con su propia direccion
- Dispositivos de caracter
	- Mandan un flujo de caracteres
		- Teclados
		- Interfaces de red
		- mouse
		- Casi todo lo que no sea un disco de almacenamiento
- Por su funcion
	- Dispositivos de entrada
		- Envian informacion pero no lo reciben
	- Dispositivos de salida
		- Permiten enviar informacion desde la computadora hacia el exterior
	- Dispositivos de entrada/salida
		- Tanto recibir como enviar informacion

Por lo general, las unidades ES consisten en un componenente mecanico y un componente electronico
- El dispositivo fisico: el aparato real que intractua con un el mundo fisico
- Controlador de dispositivo: tarjeta de circuito integrado que actua como el cerebro del dispositivo



Investigar que es paginacion








Proceso: Programa en ejecucion