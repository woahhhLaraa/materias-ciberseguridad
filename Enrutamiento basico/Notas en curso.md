---
materia: Enrutamiento basico
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---
# Enrutamiento basico — notas en curso

26 agosto 2026
Enmascaremiento variable
Ahorro de espacios de direcciones IP
CIDR es el protocolo entero, usando VLSM, para que CIDR funcionara se tuvieron que modificar protocolos de enrutamiento añadiendo como info obligatoria el tamaño de las mascaras, dejando de lado RIPV1 y entrando a RIPV2, CIDR engloba TODO el cambio para el funcionamiento del direccionamiento sin clases (estudiar mas el direccionamiento sin clases)

Tablas de ruteo:
Es un resumen de un proceso de enrutamiento completo hecho por otro.
Tiene todas las redes conocidas a las que puedo llegar, indica por donde debe ir un paquete para ir de una red A a una red Z, muestra como esta conectada ya sean seriales, fastethernet, dependiendo de la red (normalmente por su topologia) a la que vas, te manda por un camino u otro

Sumarizacion:
Cuando dos redes se parecen y voy a ellas por el mismo camino, se puede hacer una "simplificacion".
![[Pasted image 20260826093625.png]]

Estudiar esta red

Agregacion:
Reduccion de numero de rutas posibles en una red, para que el enrutador funcione de manera mas eficiente. La maxima agregacion la obtenemos cuando usamos la ruta por default

Cuando utilizar VLSM O CIDR
VLSM: Cuando se necesita segmentar una red interna en subredes de diferentes tamaños, normalmente en redes pequeñas, redes internas

CIDR: Para asigar direcciones ip a ISP y grandes organizaciones y para agregar rutas con el fin de minimizar el tamaño de la tabla de enrutamiento global. Se utiliza la signar bloques ip y gestionar rutas entre varias redes, normalmente en redes grandes o entre redes.


![[Pasted image 20260826095441.png]]




Ejercicio
![[Pasted image 20260826102335.png]]


Respuesta
![[Pasted image 20260826102402.png]]



![[Pasted image 20260826102618.png]]





> Índice de la materia: [[Enrutamiento basico]]

