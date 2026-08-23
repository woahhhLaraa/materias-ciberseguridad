---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, representacion-de-datos, numeracion]
---

# Sistemas numéricos

**Sistema numérico:** conjunto de símbolos llamados dígitos, más las operaciones que se pueden hacer entre ellos.

Los cuatro usados en ciberseguridad y tecnologías: **decimal, binario, octal y hexadecimal**.

## Tipos de representación

- **Posicional** — la posición de cada dígito indica su peso o relevancia. Cuanto más a la derecha, menos significativo.
- **Polinomial** — el valor del número expresado como suma de potencias de la base.

## Los cuatro sistemas

| Sistema | Base | Dígitos | Nota |
|---|---|---|---|
| **Decimal** | 10 | 0-9 | El habitual |
| **Binario** | 2 | 0, 1 (bits) | Presencia o ausencia de voltaje |
| **Octal** | 8 | 0-7 | Base = 2³ |
| **Hexadecimal** | 16 | 0-9, A-F | Base = 2⁴ |

## Por qué octal y hexadecimal

**Ambas son potencias exactas de 2**, y ahí está toda la razón de su existencia: reducen el número de dígitos necesarios para representar números binarios sin perder la correspondencia directa con los bits.

- Octal: 1 dígito = 3 bits
- Hexadecimal: 1 dígito = 4 bits

Por eso el hexadecimal se usa como **notación abreviada de números binarios**.

## Sobre el binario

- 1 byte = 8 bits
- 32 y 64 bits: cantidad de bits con los que puede trabajar un procesador
- Imágenes de 8 y 16 bits (profundidad de color)

## Relacionadas

- [[Conversion entre bases]]
- [[Aritmetica binaria]]
- [[Direccionamiento IP con clases]] — donde el binario y el hexadecimal se usan de verdad
