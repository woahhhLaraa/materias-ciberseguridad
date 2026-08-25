---
materia: Enrutamiento basico
semestre: 3
tipo: concepto
tags: [redes, ip, clases, direccionamiento]
---

# Direccionamiento IP con clases

En **1981** se modificaron las clases de IPv4 para crear las tres clases de redes A, B y C. Esto se conoce como **direccionamiento IP con clase** (*classful*).

Cada clase tiene un **identificador único** en los bits iniciales.

## Las cinco clases

| Clase | Primer octeto | Bits iniciales | Uso |
|---|---|---|---|
| **A** | 1 – 126 | `0` | Redes muy grandes |
| **B** | 128 – 191 | `10` | Redes medianas |
| **C** | 192 – 223 | `110` | Redes pequeñas |
| **D** | 224 – 239 | `1110` | **Multicast** |
| **E** | 240 – 255 | `1111` | **Experimental** |

> Nota: el rango 127.x.x.x está reservado para *loopback*, por eso la clase A termina en 126.

## Máscaras por defecto

| Clase | Máscara | Porción de red |
|---|---|---|
| A | 255.0.0.0 | Primer octeto |
| B | 255.255.0.0 | Dos primeros octetos |
| C | 255.255.255.0 | Tres primeros octetos |

## Cómo identificar la clase rápido

Mirar el **primer octeto en decimal** y compararlo con la tabla. En binario, contar los bits `1` iniciales antes del primer `0`.

## Relacionadas

- [[Tarea 1 - Separar red y host]] — los ejercicios de separar red y host para direcciones de cada clase
- [[Tarea 2 - Clases IP y direcciones de red]] — los ejercicios de identificar la clase y calcular la dirección de red
- [[Enmascaramiento y subnetting]] — cómo partir una de estas clases en subredes tomando bits prestados al host
- [[Sistemas numericos]] — el binario y el hexadecimal que se usan aquí
