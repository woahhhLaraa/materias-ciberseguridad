---
materia: Sistemas Operativos
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---

# Sistemas Operativos — notas en curso

Interfaces graficas

NUI
	VOZ TACTO GESTOS
CLI
	COMANDOS
		teclado
GUI
	ENTORNO GRAFICO
		teclado
		raton
		o pantalla tactil


Interpretes de comandos, shells y emuladores
Las interfaces de linea de comandos permiten al usuario interactucar con el sistema operativo mediante comandos. Tenemos que dividir conceptos relacionados pero diferentes
- Interprete de comandos
	- Viene dentro de SHELL
	- Es el que de verdad TOMA los comandos y  los interpreta
	- Ya viene dentro del KERNEL?
	- Trabaja en texto
	- Sintaxis especifica
	- Admitir variables, parametros, redirecicones y tuberias
	- Comandos de forma interactiva o mediante scripts
	- Facilita la automatizacion de tareas
		- Bash (Tambien es un shell)
		- Zsh (Tambien es un shell)
		- PowerShell
		- Command Prompt (tambien es shell)
- Shell
	- La pantalla donde escribes el comando (la pantalla en negro SIN, el entorno grafico)
	- Programa o entorno que proporciona al usuario una interfaz para interactuar con el OS
		- Bash
		- Zsh
		- Fish
		- PowerShell
- Emulador de terminal
	- Capa de software adicional
	- Emula el funcionamiento de un terminal dentro de otro entorno normalmente una interfaz gracia
	- La ventana que aparece al abrir fish dentro del entorno grafico de linux, emula como si estuviera en el shell sin interfaz grafica

El normal que estos conceptos aparezcan juntos y forman parte de un mismo programa



10 septiembre 2026

Servicios de red (funciones de un usuario) (investigar)
SERVIDOR WEB 80
SSH 22
FPT 20/21
SMPTP POP3 IMAP
DHCP
DNS


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

Administracion de permisos

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

> **Bandeja de entrada de la materia.** Todo lo de clase entra aquí, bajo el encabezado de la fecha, sin preocuparse por la estructura.
>
> Al estudiar para el parcial: selecciona cada bloque que sea un concepto y usa `Ctrl+P` → **Extraer selección actual**. Obsidian crea la nota y deja el enlace aquí. Cuando este archivo quede solo con enlaces, el parcial está repasado.
>
> Índice de la materia: [[Sistemas Operativos (materia)]]

