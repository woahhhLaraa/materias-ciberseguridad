---
materia: Sistemas Operativos
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---

# Sistemas Operativos — notas en curso

27 de agosto

Capas o subsistemas de un sistema operativo
El SO es un conjunto de susbsistemas que se comunican entre si para dar la impresion de que es una unica entidad

En representaciones las vemos como capas una encima de la otra, pero en la realidad son sistemas que se comunican entre si y no tienen porque estar completamente serparadas


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


Por lo general, las unidades ES consisten en un componenente mecanico y un componente electronico
- El dispositivo fisico: el aparato real que intractua con un el mundo fisico
- Controlador de dispositivo: tarjeta de circuito integrado que actua como el cerebro del dispositivo



Proceso: Programa en ejecucion




> **Bandeja de entrada de la materia.** Todo lo de clase entra aquí, bajo el encabezado de la fecha, sin preocuparse por la estructura.
>
> Al estudiar para el parcial: selecciona cada bloque que sea un concepto y usa `Ctrl+P` → **Extraer selección actual**. Obsidian crea la nota y deja el enlace aquí. Cuando este archivo quede solo con enlaces, el parcial está repasado.
>
> Índice de la materia: [[Sistemas Operativos (materia)]]

