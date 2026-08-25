---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, representacion-de-datos, numeracion]
---

# Conversión entre bases

## Métodos

- **Conversión directa** — cuando la base destino es potencia de la base inicial (binario ↔ octal ↔ hexadecimal). Se agrupan bits.
- **Conversión indirecta** — pasa por base 10 como paso intermedio.
- **Divisiones sucesivas** — de base 10 a cualquier base.

## Divisiones sucesivas: base 10 → base Q

Se divide el número original entre la base Q. El cociente se sigue dividiendo entre la base hasta que llegue a 0. Cada residuo se reserva, y **se leen en orden inverso** para construir el nuevo número.

### Ejemplo: 325₁₀ → base 2

```
325 / 2 = 162   residuo 1
162 / 2 =  81   residuo 0
 81 / 2 =  40   residuo 1
 40 / 2 =  20   residuo 0
 20 / 2 =  10   residuo 0
 10 / 2 =   5   residuo 0
  5 / 2 =   2   residuo 1
  2 / 2 =   1   residuo 0
  1 / 2 =   0   residuo 1
```

Leyendo los residuos de abajo hacia arriba: **101000101₂**

Comprobación: 256 + 64 + 4 + 1 = 325 ✓

## Conversión directa por agrupación

Porque 8 = 2³ y 16 = 2⁴:

- **Binario → octal**: agrupar de **3 bits** desde la derecha
- **Binario → hexadecimal**: agrupar de **4 bits** desde la derecha
- **Octal → hexadecimal**: pasar por binario

### Ejemplos de clase

| Conversión | Resultado |
|---|---|
| 36₈ → base 2 | 011 110 |
| 764₈ → base 16 | pasar a binario: 111 110 100 → reagrupar de 4: 1 1111 0100 → **1F4₁₆** |
| FB₁₆ → base 2 | 1111 1011 |

## Ejercicios pendientes de clase

Marcados pero sin resolver en los apuntes:
- 335 → base 8
- 1520 → base 16
- 251 → hexadecimal
- 821 → base 8
- 365 → ?

## Relacionadas

- [[Sistemas numericos]] — las cuatro bases entre las que se convierte, y por qué son esas cuatro
- [[Aritmetica binaria]] — qué hacer con el binario una vez convertido: sumarlo con acarreo
