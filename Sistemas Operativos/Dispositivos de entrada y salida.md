Aquellos que son capaces de recibir un input por parte de un usuario para ser usado por el sistema operativo a traves de [[Capas de un sistema operativo]] Seccion subsistema de entrada y salida, o en su defecto, dar un output para comunicarse con el usuario

Entre ellos se encuentran:
- Mouse
- Teclado
- Dispositivos de almacenamiento secundario
- Bocinas
- Pantalla
- Tarjeta grafica
- Tarjeta de red

Cada uno de estos dispositivos lo podemos dividir en dos partes
- Su componente fisico, lo que podemos ver y tocar, en mouse teclado bocinas pantalla y almacenamiento secundario, es un componente mecanico
- Su componente logico, una tarjeta o chip que funciona como el cerebro donde tiene tanto su logica, como su controlador, y en algunos casos, memoria y buferes.



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


Para poder comunicarse con el sistema operativo de forma bidireccional, todos los dispositivos de entrada y salida utilizan controladores (drivers). Estos se encuentran dentro de su componente logico. 
En la logica de los drivers se encuentra
Registros ES:
- Registro de control
	- Mediante comandos, el cpu es capaz de controlar el dispositivo ES, escribir y leer.
- Registro de datos
	- El lugar de los registros donde se guarda toda la informacion que se quiere leer por parte del dispositivo ES, tambien es el lugar donde se escribe informacion desde la computadora.
- Registro de estado
	- Aqui el ES indica cual es su estado actual, suspendido, ocupado, encendido, listo, error

Puertos o direcciones ES:
- Tienen la funcion de ser puentes entre el dispositivo ES y el sistema operativo
- Le dan a cada registro proveniente del ES una direccion unica, para que el sistema operativo sepa con quien esta hablando en todo momento
