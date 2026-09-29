---
materia: Enrutamiento basico
semestre: 3
tipo: concepto
tags:
  - redes
  - enrutamiento
  - routers
sr-due: 2026-10-15
sr-interval: 17
sr-ease: 226
---
#review 
# Conceptos fundamentales de enrutamiento

> Clase del 19 de agosto

## Paquete

Unidad con **datos** y **dirección de origen y destino**. Contiene la información que se manda de una red a otra a través del enrutamiento hecho por los routers.

## Enrutamiento por saltos

Los enrutadores **solo necesitan saber el siguiente punto de destino**
para llegar a la dirección final. No conocen la ruta completa.

Esa es la idea que hace escalable a internet: ningún router tiene el mapa entero.

## Tipos de enrutamiento

### Estático
El usuario le dice exactamente al router qué ruta utilizar.

### Dinámico

El router define la ruta según lo que considere adecuado, siguiendo algún protocolo:

Existen dos familias de protocolos de enrutamiento dinamico

Interiores:
	Cuando el trafico se va a dar dentro un sistema autonomo (ejemplo: Dentro de una empresa) donde no va hacia afuera.

- **RIP** - Metrica : vector distancia
- **OSPF** Metrica: estado enlace
- **IS-IS** Metrica : estado  de enlace
- EiGRP metrica: vector distancia

Exteriores:
	Cuando el trafico se da entre sistemas autonomos (ejemplo: Mandar un paquete dentro de la empresa, hacia el internet, u otra red autonoma)
- **BGP** : Vector por ruta (una clase de hibrido entre estado enlace y vector)

Vector distancia: Mide el numero de saltos entre un nodo y otro, entre menos saltos, mas preferencia
Estado de enlace: la metrica de los nodos es la velocidad que manejan entre enlace y enlace, si un enlace es mas rapido aunque tenga mas nodos, lo agarra.

## Enrutado vs enrutamiento
El protocolo enrutado (podria ser un paquete, que fue hecho siguiento el protcolo ipv4 o ipv6) es lo que viaja a traves de la red.
El enrutamiento es lo que decide como va a llegar ahi.



## Protocolos de enrutamiento y las clases

> Clase del 21 de agosto

Los primeros protocolos asumían que lo primero que necesitaban saber —y que estaba **implícito en la dirección IP**— era la **clase** de la dirección.

Protocolos como **RIPv1** solo necesitaban propagar la dirección de red de las rutas conocidas, **sin incluir la máscara**, porque ya sabían de qué clase era la red.

Una década después, con la reducción rápida de direcciones IP, nace **CIDR**. Ver [[CIDR y VLSM]].


Tabla de ruteo:
Cada router, de forma indivual, tiene el conocimiento de los routers que se encuentran de forma inmediata a el, y una tabla que dice algo como: Si recibes un paquete que tiene que ir a un punto final Z, mandala hacia el nodo inmediato C, si va a H, mandalo a J.


## Relacionadas

- [[Direccionamiento IP con clases]] — cómo se lee la dirección de destino con la que el router decide el siguiente salto
- [[Capa de red - IPv4 e IPv6]] — el paquete y el enrutamiento vistos desde la capa 3, en segundo semestre
- [[Sintaxis basica de comandos IOS]] — la CLI con la que todo esto se configura en un router Cisco
