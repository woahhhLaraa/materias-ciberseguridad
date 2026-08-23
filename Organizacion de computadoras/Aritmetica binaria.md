---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, representacion-de-datos, binario]
---

# Aritmética binaria

**La operación más básica del binario es la suma.**

## Tabla de la suma binaria

Los bits solo tienen dos valores posibles:

```
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10   ← escribe 0, acarrea 1
```

El único caso interesante es el último: `1 + 1` produce **acarreo**.

## Procedimiento con comprobación

Ejemplo: `10101 + 1101`

1. Hacer la suma en binario
2. Como comprobación, convertir ambos sumandos a decimal y sumarlos
3. Verificar que ambos resultados coincidan tras la conversión

```
   10101   (21)
 +  1101   (13)
 -------
  100010   (34)
```

21 + 13 = 34 ✓

El paso 2 no es opcional en los exámenes de esta materia: se pide la comprobación explícita.

## Relacionadas

- [[Sistemas numericos]]
- [[Conversion entre bases]]
