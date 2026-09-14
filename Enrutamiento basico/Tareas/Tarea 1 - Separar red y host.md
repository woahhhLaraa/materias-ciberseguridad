---
materia: Enrutamiento basico
semestre: 3
tipo: tarea
tags: [redes, ip, ejercicios]
---

# Tarea 1 — Separar red y host

Ejercicios de [[Direccionamiento IP con clases]].

## Parte 1 — Separar el número de red y el número de host

| Dirección IP    | Clase | Número de red | Número de host |
| --------------- | ----- | ------------- | -------------- |
| 84.32.1.1       | A     | 84.0.0.0      | 0.32.1.1       |
| 53.200.77.6     | A     | 53.0.0.0      | 0.200.77.6     |
| 115.25.44.100   | A     | 115.0.0.0     | 0.25.44.100    |
| 25.4.12.210     | A     | 25.0.0.0      | 0.4.12.210     |
| 69.0.0.25       | A     | 69.0.0.0      | 0.0.0.25       |
| 149.215.32.1    | B     | 149.215.0.0   | 0.0.32.1       |
| 173.5.88.23     | B     | 173.5.0.0     | 0.0.88.23      |
| 157.223.4.203   | B     | 157.223.0.0   | 0.0.4.203      |
| 190.3.4.24      | B     | 190.3.0.0     | 0.0.4.24       |
| 192.215.32.1    | C     | 192.215.32.0  | 0.0.0.1        |
| 213.34.56.66    | C     | 213.34.56.0   | 0.0.0.66       |
| 201.201.201.201 | C     | 201.201.201.0 | 0.0.0.201      |
| 219.33.54.10    | C     | 219.33.54.0   | 0.0.0.10       |

## Parte 2 — Escribir las direcciones en binario y hexadecimal

| Dirección IP | Binario | Bits iniciales | Clase | Hexadecimal |
|---|---|---|---|---|
| 84.32.1.1 | 0101 0100 . 0010 0000 . 0000 0001 . 0000 0001 | 01 | A | 54.20.01.01 |
| 53.200.77.6 | 0011 0101 . 1100 1000 . 0100 1101 . 0000 0110 | 00 | A | 35.C8.4D.06 |
| 115.25.44.100 | 0111 0011 . 0001 1001 . 0010 1100 . 0110 0100 | 01 | A | 73.19.2C.64 |
| 25.4.12.210 | 0001 1001 . 0000 0100 . 0000 1100 . 1101 0010 | 00 | A | 19.04.0C.D2 |
| 69.0.0.25 | 0100 0101 . 0000 0000 . 0000 0000 . 0001 1001 | 01 | A | 45.00.00.19 |
| 149.215.32.1 | 1001 0101 . 1101 0111 . 0010 0000 . 0000 0001 | 10 | B | 95.D7.20.01 |
| 173.5.88.23 | 1010 1101 . 0000 0101 . 0101 1000 . 0001 0111 | 10 | B | AD.05.58.17 |
| 157.223.4.203 | 1001 1101 . 1101 1111 . 0000 0100 . 1100 1011 | 10 | B | 9D.DF.04.CB |
| 190.3.4.24 | 1011 1110 . 0000 0011 . 0000 0100 . 0001 1000 | 10 | B | BE.03.04.18 |
| 192.215.32.1 | 1100 0000 . 1101 0111 . 0010 0000 . 0000 0001 | 11 | C | C0.D7.20.01 |
| 213.34.56.66 | 1101 0101 . 0010 0010 . 0011 1000 . 0100 0010 | 11 | C | D5.22.38.42 |
| 201.201.201.201 | 1100 1001 . 1100 1001 . 1100 1001 . 1100 1001 | 11 | C | C9.C9.C9.C9 |
| 219.33.54.10 | 1101 1011 . 0010 0001 . 0011 0110 . 0000 1010 | 11 | C | DB.21.36.0A |

> ⚠️ **Corrección respecto a la entrega original.** La primera fila estaba mal: se puso `84 = 0100 1010 = 4A`, pero 4A hexadecimal es 74 decimal, no 84.
> El valor correcto es **84 = 0101 0100 = 0x54**. Las otras doce filas están bien.

## Relacionadas

- [[Direccionamiento IP con clases]] — la teoría que estos ejercicios aplican: rangos y bits iniciales de cada clase
- [[Tarea 2 - Clases IP y direcciones de red]] — la continuación: identificar la clase y calcular la dirección de red
- [[Conversion entre bases]] — el método de conversión a binario y hexadecimal
