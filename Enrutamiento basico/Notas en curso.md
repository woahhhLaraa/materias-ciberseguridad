---
materia: Enrutamiento basico
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---
# Enrutamiento basico — notas en curso

26 agosto 2026
Tablas de ruteo:
Es un resumen de un proceso de enrutamiento completo hecho por otra entidad.
Tiene todas las redes conocidas a las que puedo llegar (como enrutador), indica por donde debe ir un paquete para ir de una red A a una red Z, muestra como esta conectada ya sean seriales, fastethernet, dependiendo de la red (normalmente por su topologia) a la que vas, te manda por un camino u otro

Sumarizacion:
Cuando dos redes se parecen y voy a ellas por el mismo camino, se puede hacer una "simplificacion".
![[Pasted image 20260826093625.png]]

Estudiar esta red

Agregacion:
Reduccion de numero de rutas posibles en una red, para que el enrutador funcione de manera mas eficiente. La maxima agregacion la obtenemos cuando usamos la ruta por default

Cuando utilizar VLSM O CIDR
VLSM: Cuando se necesita segmentar una red interna en subredes de diferentes tamaños, normalmente en redes pequeñas, redes internas

CIDR: Para asigar direcciones ip a ISP y grandes organizaciones y para agregar rutas con el fin de minimizar el tamaño de la tabla de enrutamiento global. Se utiliza la signar bloques ip y gestionar rutas entre varias redes, normalmente en redes grandes o entre redes.







Ejercicio
![[Pasted image 20260826102335.png]]


Respuesta
![[Pasted image 20260826102402.png]]



![[Pasted image 20260826102618.png]]




28 de agosto 1924
CISCO IOS
Para que un enrutador funcione, cuentan con un OS, en cisco el usado es "IOS" o internet operative system.

Todos los desarrollos de software tienen desarollos de capas, el IOS tiene 3
- Hardware (toda la circuiteria fisica)
- Kernel o nucleo
- Shell (la pantalla donde nosotros actuamos) Ya sea CLI o GUI

Usaremos IOS para, teclear comandos para ejecutar programas de red, introducir texto y ordenes. 
Proporciona opciones para configurar interfaces y habilitar memorias de enrutamiento
El IOS se almacena en una memoria FLASH (almacenamiento no volatil) pero es modificable segun seria necesario, si tiene suficiente memoria podria hasta almacenar varias versiones de IOS.
El IOS se copia de la memorai flash a la RAM volatil (por que?) {Creo que de aqui sale el running config y el startup config}

Las funciones principales dle sistema
- Seguridad
- Orientacion
- QoS
- Direccionamiento
- Admnistracion de recursos
- Interfaz

Se puede acceder al shell mediante
- Puerto de consola
- Puerto auxiliar
- SSH

Modos de funcionamiento de cisco ios
- Modo exec ">", capacidad limitada, para operaciones basicas pero no permite ejecutar ningun comando, solo lectura pues
- Modo privilegiado"#", capacidad mas amplia, operaciones de lectura, para ejecutar comandos-
- Modo configuracion global (config)#
	- Config if
	- Config router
	- Config-line
![[Pasted image 20260828075403.png]]


Ver [[Sintaxis basica de comandos IOS]]


Ayudas del IOS
Dos formas de ayuda:
- Ayuda contextual
	- Te muestra los comandos posibles con esas letras en el modo de funcionamiento actual
- Verificador de sintaxis



> Índice de la materia: [[Enrutamiento basico (materia)]]

