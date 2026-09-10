---
materia: Enrutamiento basico
semestre: 3
tipo: concepto
tags: [redes, ip, mascaras, subnetting]
---

# Enmascaramiento y subnetting

## Enmascaramiento

Quitar información específica de un dispositivo dentro de una IP. En este caso, para **no decirle a un enrutador a qué dispositivo exacto va un paquete** —lo que aumentaría enormemente la dificultad y la complejidad— y que solo le interese **a qué red va**. Dentro de la propia red se define el dispositivo.

Las máscaras y cómo se aplican dependerán del **número de subredes** que una red necesite.

### Ejemplo de cálculo

Si necesitamos **40 subredes**:

```
40 → en binario = 101000 → 6 bits
```

Se toman prestados **6 bits** de la porción de host para identificar la subred.

> Regla general: con *n* bits prestados se obtienen 2ⁿ subredes. Con 6 bits: 2⁶ = 64 ≥ 40 ✓ (con 5 bits solo habría 32, insuficiente).

## Subnetting

Dividir una red en dos o más redes más pequeñas.

### El problema del subnetting clásico

Con el subnetting de la época, **todas las subredes tenían el mismo tamaño**, lo que lleva a ineficiencia en la asignación de direcciones: una subred que necesita 5 hosts recibe el mismo bloque que una que necesita 200.

La solución fue permitir máscaras variables, introduciendo la técnica **VLSM**. Ver [[CIDR y VLSM]].


## Como funcionan las mascaras de forma practica

> Punto de partida: [[Funcionamiento de IPv4]] — una direccion son 32 bits repartidos en cuatro octetos, y cada octeto llega como maximo a 255.

Las mascaras (/24..) indican el numero de bits que son usados para representar la red (recordemos que el total de bits son 32), el resto de los bits se usan para representar el host, entonces en una mascara de red /24, 32-24 = 8, entonces nos queda un octeto entero para jugar con los hosts 

1111 1111 . 1111 1111 . 1111 1111 . 0000 0000 = 255. 255. 255. 000

Para obtener el numero de hosts totales, usamos la formula 2(pow)n. Donde n es el numero de bits que tenemos disponibles para el host segun nuestra mascara, segun el ejemplo anterior, tenemos 8 (un octeto), disponibles. Entonces, 2(pow)8 = 256.

Ese 256 es el numero total de hosts disponibles, sin embargo de esos 256, 2 de esos hosts son el broadcast y la representacion de la propia red, entonces a esos 256 restamos 2 = 254

254 es el numero de hosts a nuestra disposicion para conectar computadoras u otros.


## Relacionadas

- [[Funcionamiento de IPv4]] — los 32 bits y los octetos sobre los que se aplica toda mascara
- [[Direccionamiento IP con clases]] — las clases A, B y C de cuya porción de host se toman los bits prestados
- [[Conversion entre bases]] — el binario necesario para calcular máscaras
