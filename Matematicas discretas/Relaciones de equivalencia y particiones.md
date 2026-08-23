---
materia: Matematicas discretas
semestre: 1
tipo: concepto
tags: [matematicas, relaciones, equivalencia]
---

# Relaciones de equivalencia y particiones

## Definición

Una **relación de equivalencia** es aquella que cumple las tres propiedades a la vez:

- **Reflexiva**
- **Simétrica**
- **Transitiva**

Ver [[Relaciones y sus propiedades]] para cada una.

Fórmula de comprobación de la transitividad por matrices: `Mr = MR + MR²`

## Particiones

Una **partición** es un conjunto de clases de equivalencia con dos propiedades:

1. Deben estar contenidos **todos** los elementos del conjunto A
2. La intersección entre las clases de equivalencia debe ser **vacía**

## Ejercicio de clase

![[matriz-relacion-ejercicio-1.png]]

![[matriz-relacion-ejercicio-2.png]]

Como se trata de una relación de equivalencia, sus clases de equivalencia son:

El "1" está presente en las posiciones (1,1), (1,2) y (1,5). Recorriendo cada elemento:

| Elemento | Clase |
|---|---|
| 1 | {1, 2, 5} |
| 2 | {1, 2, 5} |
| 3 | {3, 4} |
| 4 | {3, 4} |
| 5 | {1, 2, 5} |

Cuando se repiten los elementos en cada clase, decimos que tenemos **particiones**. Aquí hay dos: **{1, 2, 5}** y **{3, 4}**.

## Por qué esto importa en redes 🔌

La profesora lo señaló explícitamente: las relaciones de equivalencia son importantes porque **es una propiedad que deben tener las redes**.

- **Simetría** — la computadora 1 puede enviar información a la computadora 2, pero además la 2 puede comunicarse con la 1
- **Reflexividad** — toda computadora tiene comunicación consigo misma
- **Transitividad** — si existe un camino de 1 a 2, y otro de 2 a 5, debe haber uno de 1 a 5

Esta es la conexión formal entre esta materia y [[Introduccion a las redes de computo]].

## Relacionadas

- [[Cerraduras de relaciones]] — qué hacer cuando una relación *no* es de equivalencia
- [[Teoria de grafos]]
