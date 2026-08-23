---
materia: Matematicas discretas
semestre: 1
tipo: concepto
tags: [matematicas, relaciones, cerraduras]
---

# Cerraduras de relaciones

Cuando una relación **no** es de equivalencia, se convierte en una agregando **cerraduras**, en este orden:

## 1. Cerradura reflexiva

La matriz relación se **suma con la matriz identidad**. Ambas deben ser del mismo tamaño.

> **Matriz identidad:** la diagonal principal compuesta de 1's, rodeada de 0's.

## 2. Cerradura de simetría

A la relación R se le agrega su **relación inversa** Rᵗ, para que la relación resultante tenga la propiedad de simetría:

```
R ∪ Rᵗ        (o en matrices: MR ∪ MᵗR)
```

## 3. Cerradura transitiva

A la relación R se le agrega la matriz que resulta de **multiplicar la relación por sí misma**:

```
MR ∪ M²R
```

## El orden importa

Se aplican en este orden precisamente porque cada cerradura puede romper lo que la anterior garantizó si se hacen al revés. Reflexiva → simétrica → transitiva es el orden que converge.

## Relacionadas

- [[Relaciones de equivalencia y particiones]]
- [[Relaciones y sus propiedades]]
