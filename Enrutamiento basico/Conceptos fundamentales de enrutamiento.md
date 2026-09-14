---
materia: Enrutamiento basico
semestre: 3
tipo: concepto
tags:
  - redes
  - enrutamiento
  - routers
sr-due: 2026-09-15
sr-interval: 2
sr-ease: 246
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

- **RIP**
- **IGRP** / **EIGRP**
- **OSPF**
- **IS-IS**
- **BGP**

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
