---
materia: Enrutamiento basico
semestre: 3
tipo: concepto
tags: [redes, ip, ipv4, binario, octetos]
---

# Funcionamiento de IPv4

Las redes IPv4 tienen un **máximo de 32 bits** para representar la red y los hosts. Esos 32 bits son todo el espacio que hay: lo que se le da a la red se le quita al host, y al revés.

## Los octetos

La dirección se mide por **octetos**: cuatro grupos de 8 bits separados por puntos.

```
1111 1111 . 1111 1111 . 1111 1111 . 1111 1111
    255   .     255   .     255   .     255
```

Cada número entre punto y punto decimal es un **octeto**. El máximo es **255** porque son 8 bits en binario y, con los 8 bits encendidos, 255 es el número más grande que se puede formar (2⁸ − 1).

## Relacionadas

- [[Enmascaramiento y subnetting]] — cómo se reparten esos 32 bits entre porción de red y porción de host
- [[Direccionamiento IP con clases]] — cómo se repartió este espacio de 32 bits en los bloques fijos A, B y C
- [[Capa de red - IPv4 e IPv6]] — el protocolo IP visto en segundo semestre, y por qué 32 bits acabaron siendo pocos
- [[Conversion entre bases]] — el binario que hace que 8 bits den como máximo 255
