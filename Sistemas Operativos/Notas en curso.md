---
materia: Sistemas Operativos
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---

# Sistemas Operativos — notas en curso

## Usuarios y gestión de usuarios



10 septiembre 2026

Gestion de usuarios o administracion de usuarios
Un usuario
	Entidad que puede ser una persona preoceso o dispositvo, que interactua con la computadora y pose una identidad digital especifica. La identidad determina sus permisos, privilegios y niveles de acceso
	Normalmente tiene un nombre de usuario, y en muchos casos una contraseña(autenticacion), internamente el sistema operativo los identifica de forma unica 
		Tiene las siguientes funciones
			Administrar servicios de red
			
La autenticacion 
	se da normalmente por algo que SABE, ES, O TIENE (introduccion a la ciberseguridad)

Esta gestion es fundamental en la seguridad, pues puede convertise en un agujero importante de seguridad que permita accesos no autorizados o comprometa los recursos del sistema.

Puede ser identificado con un numero unico de grupo, o un numero unico de usuario.



funciones desde la perpesectiva del sistema operativo
Control de acceso y autenticacion : Validar quien intenta ingresar con contraseñas
			Asignacion de propiedad, que archivos pertenecen a un perfil especifico para que nadie mas pueda modificarlos sin persmiso
Asignacion de propiedad: Marcar que archivos, carpetas y configuraciones pertenecen a ese perfil especifico para que nadie mas pueda modificarlos sin permiso
Aislamiento de procesos, garantizar que los programas que ejecuta un usuario no interfieran ni espien las aplicaciones que tiene abiertas otro usuario en el mismo equipo
Auditoria y registo: Registrar en el historial del sistema, que acciones realizo esa entidad


Tipos de usuario
Cada uno tiene niveles distintos de acceso permisos y privilegios dentro del sistema. 
basado en linux

Administrador o superusuario
- el usuario adminisitrador en linux se le conoce como root
- Los privilegios mas elevados
	- Instalar programas, modificar configuraciones, crear o eliminar usuarios y administrar permisos
- Las cosas que solo puede hacer el root
	- Instalar actualizaciones o instalar paquetes nuevos
	- eliminar directorios y archivos 
- Su prompt es un "#"

Usuairo estandar o normal
- El usuario con el que se inicia sesion dentro de un sistema, puede utilizar aplicaciones y trabajar con sus propios archivos pero tiene restricciones para modificar aspectos importantes del sistema
- una cuenta normal, creado sin problemas dentro del sistema por un superusuario
- normalmente compuesto por usuario y contrasena
- usuarioNormal$- (prompt)
- tiene un espacio de trabajo (workspace) propio /home/usuarioNormal
- tiene un UID (ID DE USUARIO)

Usuario invitado
- Un usuario estandar con permisos aun mas limitados, para accesos temporales

Usuarios del sistema/especiales
- Usuarios "logicos", pues suelen ser servicios
- tambien conocidos como usuarios sin login (no tienen contraseña, no se utilizan para iniciar sesion)
- estan muy ligados a los daemons
- generalmente con un UID entre 1 y 100

Administracion de usuarios y grupos

Creacion de usuarios 
Modificacion
eliminacion

14 de sep 2026

Que clase de servicios podemos meter en u nsistema operativo linux?
- Apache (web) puerto 80
- mysql (base de datos) puerto 3306

cuando inicializamos un servicio, creamos un usuario especial 



Concepto de grupo
Los usuarios, se reunen en grupos, lo cual es una expresion logica para reunir a un conjunto de usuarios que tienen caracteristicas en comun

Archivos de usuarios, gurpos y contraseñas
La mayoria de los sistemas operativos se ayudan de archivos de configruacion
- Archivods passwd, almacena informacion basica y publica de las cuentas de usuario
- archivo shadow, almacena de forma segura las contraseñas cifradas con hash
- archivo group, este archivo define los gripos del sistema, permiteiendo organizar los usuarios para compartir persmisos en archivos y directorios



useradd y adduser, para agregar usuarios, son las dos formas para agregar usuarios desde la linea de ocmandos
adduser es un script de alto nivel, interactivo
useradd es de bajo nivel,

![[Pasted image 20260914094121.png]]


agregar o actualizar la contraseña con passwd
para agregar o modificar la contraseña de un usuario, debeera de estar creado anteriormente
root es el unico que puede realizar el cmabio
usarios normales, pueden cambiar su contraseña 
el comando es passwd usuario

el comando usermod permite cambiar de grupo, añadir comentarios, cambiar directorio de trabajo, cambiar login o nombre de usuario, cambiar el shell por defecto


eliminar usuarios
existen 3 formas, dependiendo de que comando se elimina de forma distinta
- userdel usuario: elimina la cuenta de los arcihvos shadow y passwd pero no elimina su directorio de trabajo, es decir elimina el usuario pero mantiene sus datos
- userdel -r elimina totalmente, pero con el flag r elima directoios de travajo y archivos
- uesrdel -f usuario, todo todo, sin importar si el usuario esta actualmente en el sistema trabajando, muy radical y puede causar inestabildiades

eliminar y editar grupos
groupadd nombreDelGrupo
groupdel nombreDelGrupo
groupmod  -n nuevoNombre antiguoNombre


añadir o eliminar usuarios del grupo

usermod -a(dd)G(roup) nombreDelGrupo NombreDelUsuario
gpasswd -d nombreUsuario nombreGrupo (para sacarlo)


## Gestión de permisos

Administracion de permisos

gestion de permisos en linux
los permisos son un mecanismo de seguridad que controla que acciones puede realizar un usuario, proceso o programa sobre un recurso del sistema

la mayoria de los sistemas operativos (hay muchas mas pero esta es la principal) se basa en tres pilares para evaluar los perimsos
- El Sujeto que quiere hacer algo
- El objeto (el recurso al que le quiero aplicar una operacion)
- La accion (como lo voy a hacer
Los tres permisos basicos en linux son
- read -> r
- write -> w
- execute -> x

Los permisos pueden ser aplicados a
- Propietario de larchivo
- Grupo como conjunto de usuarios con roles similares
- Otros, cualquier otra persona que tenga cuenta en el sistema 



Clase 17 de septiembre 2026

Permisos en linux

para identiricar los atriutos de un archivo o directorio, detminar cuales son los permisos y propietarios ls -l
![[Pasted image 20260917092250.png]]

Referencias binarias para configurar permisos en linux

Para deonmiar y configurar permisos 
el primer numero permisos de propietario
segundo permisos de gurpo
y el ultimo representa permiso de otros usuarios

los numeros representan los caracteres rwx asigandno a cada letra un valor
r=4
w=2
x=1
sumamos los numeros y segun el resultado es el permiso que tiene alguien sobre ese archivo

comando de permiso _Chmod_ (agregar o eliminar un permiso a algo)

chmod [permisos] nombreArchivo

se puede especificar los permisos a traves de representacion binaria, o utiliznaod la letra inicial a quien va dirigido el permiso 
usuario = u(ser)
grupo = g(roup)
otros = o(thers)
todos = a(ll)
seguido del signo (+) o (-)
seguido del permiso correspondinete r/w/x
seguido del nombre de archivo


Gestion de permisos sobre un grupo 
asignar permisos a nivel de grupo es distinto:
1.- Primero se requiere crear un grupo (entidad que envuelve a varios usuarios)
	sudo groupadd licic
2.- Vincular un directorio o archivo al grupo: se le asigna la carpeta o archivo al gurpo correspondiente (cambio de propietario)
	sudo chown : licic /ruta/elemento
3.- Asignar los permisos al directorio



## Inicio de sesión

existen 3 formas de logearse en el sistema operativo
- De forma grafica
- A traves de CLI




## Sistema de archivos

28 de septiembre 2026
Sistema de archivos (tema pesado)
Que es?
Uno de los 8 subsistemas (no confundirse con el sistmea de gestion de almacenamiento secundario) , se encarga de la gestion logica del almacenamiento secundario, es el conjunto de estructuras, metodos, y mecanismos que utiliza un sistema operativo para organizar, almacenar, gestionar, leer, modificar y recuperar informacion de manera logica y estructurada en un dispositivo de almacenamienot como un disco duro, un ssd o una memoria USB, permite organizar los datos en archivos carpetas y directorios, facilianto su localizacion y acceso por partede los usuarios
Sirve para:
- Organizar archivos
- Nos permite copiar, pegar, eliminar archivos
- Visualizacion de las rutas de los archivos
- Controlar accesos a los archivos
- Gestionar el espacio de almacenamiento: asignando y liberando espacio segun las necesiades de los archivos
- Permitir el uso compartido de archivos entre usuarios y procesos autorizados

Como funcionan?
Manteniendo informacion sobre aspectos como
- Donde se encuentra almacenado un arcihvo
- cuanto espacio ocupa en su dipositivo de almacenamiento
- Tamaño, tipo y otros datos importantes
- Si esta siendo utilizado (tabla de archivos)
- Fecha de creacion y modificacion
- Permisos de acceso
- Identificadores necesarios para acceder al archivo


Existen diferentes sistemas de archivos
- EXTFAT32
	- Considerado el sucesor de fat32
	- Elimina la restriccion de 4gb de limite de archivo
	- estrucutra simple y no desgasta las memorias flash
	- Creado en el 2006 para windows embedded
	- La volvieron libre y linux ahora lo sporta de manera nativa
	- Los usos siguen siendo los mismos que su predecesor pero con mas almacenamiento y un flujo de datos mas grande
	- Teoricamente alcanza 16 exabytes para tamaño de archivo
	- Tamaño maximo de particion 128 petabytes
	- Compatibilidad masiva
	- sin limite de archivos
	- Falta de journaling
	- Carece de funciones avanzadas como los permisos de archivos locales de NTFS Y EXT4, el cifrado nativo del sistema de archivos o la compresion automatica
		- Region de arranque
		- Region de respaldo
		- REgion de clusteres
		- Tabla de asignacion de archivos
		- Mapa de bits de espacio libre
		- Directorio raiz y datos
- FAT32: Alta compatibilidad
	- De microsoft nacio en el 96 junto a windows 96, evolucion directa de fat16 y fat12
	- Todavia usado por memorias usb, tarjetas sd, discos externos portatiles, disposiitvos multimedia en automoviles o televisores
	- El tamaño de los archivos no soportan archivos mayores a 4 gb
	- Tamaño maximo de particion: 8tb en practica pero en la practica se limita a 32 gb
	- No tiene journaling, si sufre un apagon es dificil recuperar archivos
	- Casi cualquier sistema operativo lo soporta (leer y escribir)
	- Ligero y con bajo consumo de recursos de procesamiento y memoria
	- Carece de permisos de seguridad avanzados o cifrado nativo.
		- Estructura
			- Sector de arranque
				- primer sector de la particion, con informacion basica como punteros a otras secciones, informacion del volumen y el codigo de inicio
			- Region FAT
				- Guarda dos copias de la tabla de asignacion de archivos
			- Directorio raiz
				- Estrucutra fija que lista los archivos y subcaperetas principales
			- Region de datos
				- Donde se graban el contenido de los archivos y subdirectorios dividios en clústeres, ocupa casi toda la particion.
- NTFS: solo windows
	- Por microsoft desde el 93 con windows XP
	- El estandar de windows SO
	- Discos duros y de estado solido, principales para sistemas operativos windows.
	- Tamaño maximo de archivo 16 tb teoricos
	- tamaño maximo de particion 256 tb
	- SI tiene journaling
	- Usa MFT, para contener informaciondetallada de los archivos
	- Alta seguridad mediante permisos de archivos locales y remotos
	- soporte nativo para cifrado de datos
	- resistente a fallas gracias al journaling
	- arbol binario de alto rendimiento para localizar a los archivos
	- compatibilidad limitada con mac y linux
	- consume mayor espacio en metadatos, no es recomendado para unidades de almacenamiento pequeñas
		- Sector de arranque
		- MFT (tabla maestra de archivos)
			- El nucleo de NTFS, base de datos donde cada archivo o directorio tiene al menos un registro que detalla sus atributos, es una lista de todos los contenidos de esta volumen de NTFS
		- Archivos de sistema
			- Contiene archivos ocultos que gestionan el espacio libre, la seguridad y el registr de transacciones
- EXT4: Para linux
- APFS: Apple, macOS

Estructura en capas de un sistema de archivos
Estan diseñados bajo un modelo o arqutectura en capas, cada capa tiene sus propias tareas de forma jerarquica para separar las funciones de alte y de bajo nivel.
Esta dividido asi para reducir la complejidad y facilitar el mantenimiento, y permite que los archivos interactuen con el hardware (mediante drivers)
Las capas mas altas son de interaccion con el usuario, y las de bajo nivel son de interaccion con el hardware

Capa de aplicacion del usuario
Es la que inicia cualquier, no forma parte interna del sistema de archivos pero es la que iniica cualquieraccion meidante llamdas al sistema (syscalls) las funciones tipicas son: Open(), read(), write y close()

Capa de archivos logico
Maneja la estrucutra conceptual del sistema. Administra directorios, los nombres los archivos y los permiso de seguridad (lectura y escritura). Gesitona los metadatos y la estructura de directorios las rutas y el control de acceso
Contrloa los bloques de control de archivos FCB que guardan los metadatos del archivo pero no su contenido

Capa de modulo de organizacion de archivos
Puente entre el mundo logico y el mundo fisico, nombres y carpetas con bloques de datos en el medio de almacenamiento. Sabe como estan asignados los archivos en el almacenamiento
Rastrea el espacio libre en el dispostiivo y decide donde colocar los nuevos datos

Sistema de archivos basico
Se encarga de emitir comandos genericos hacia el hardware para leer y escribir bloques fisicos de datos
Envia instrucciones abstractas como "lee el bloque 45092" al controlador de disco correspondiente
Esto ayuda a administrar los buferes y cache del sistema operativo. Guarda fragmenos de datos de uso frecuente en la memoria RAM para agilizar el rendmiento y evitar leer el disco constantemente

Control de E/S
Es el nivel mas bajo del software compuesto por los drivers y los controladores de interrupciones
Traduce los comandos abstractos del sistema basico en instrucciones de bajo nivel, que el circuito de hardware puede entender, como leer corriente electrica en seldas en un ssd o mover el cabezal a un cilindo y sector especificos en un disco mecanico

Capa de hardware
El componente fisico donde residen los datos de forma permanente. Se encuentran al ifnal de toda la estrucutra de capas y recibe las señales electricas u ordenes directas del controlador de netrada/salida
Convierte los pulsos electricos y las instrucciones de bajo nivel en almacenamiento real y permanente. Esta capa entiende posiciones fisicas como direcciones de memoria o coordenadas goegraficas de un diso, no datos ni carpetas, ni archivos.



Se encuentra a nivel alto en el sistema operativo


Segun donde se almacenen los datos
Existen:
- De disco (locales)
	- Son los que interactuan directamente con el hardware fiisco y los sectores magneticos
	- Para SO de usuario final o medios de almacenamiento
	- Almacenamiento mecanico y discos inteernos
- En red (distribuidos)
	- No controlan nada fisicamente de forma directa, funciona con un protocolo de comunicacion para hacerle creer al sistema que un directorio que se encuentra en la red se encuentra montado sobre un disco de almacenamiento local
		- NFS (para conectar linux con linux) SAMBA/SMB (para conectar windows, mac y linux entre si)
		- SSHFS para compartir de forma segura y cifrada
- Virtuales/especiales (utiles en administracion de servidores)
	- NO son sistemas que se montan sobre un medio de almacenamiento o en una red, existen solo en memoria ram o mientras una computadora esta encendida o mientras un proceso en ejecucion lo mantenga, para manejar tareas internas de un proceso
		- /proc: un sistema de archivos virtual donde cada "archivo" es en realidad un proces o de la computadora o informacion del procesador
		- /dev: muestra los ocmponentes del hardware como si fueran archivos de texto para poder interactuar con ellos
		- el registro de windows, que organiza toda la configuracion del sistema de forma jerarquica en la memoria

Que es un archivo?
Un conjunto de datos con la intencion de representar algo (fotos, documentos, binarios) nosotros como usuarios lo vemos como una entidad, almacenado en un almacenamiento secundario. Una computadora tiene control sobre el archivo

El meido en el que se almacenan los archivos se divide en bloques de longitud fija, siendo el sistema de archivos el encargado de asignar u numero de bloques a cada archivos

Que es un directorio?
Un contenedor virtual que me permite administarr archivos y subdirectorios. Normalmente en los GUIS los vemos como carpetas

- Organiza
- Localiza
- Da estructura (estructura de arbol): permite crear ramas de directorios dentro de otros y todos parten de un directorio raiz



> **Bandeja de entrada de la materia.** Todo lo de clase entra aquí, bajo el encabezado de la fecha, sin preocue uparse por la estructura.
>
> Al estudiar para el parcial: selecciona cada bloque que sea un concepto y usa `Ctrl+P` → **Extraer selección actual**. Obsidian crea la nota y deja el enlace aquí. Cuando este archivo quede solo con enlaces, el parcial está repasado.
>
> Índice de la materia: [[Sistemas Operativos (materia)]]

