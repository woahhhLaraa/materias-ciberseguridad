---
materia: Matematicas discretas
semestre: 1
tipo: concepto
tags: [matematicas, relaciones, conjuntos]
---

# Relaciones y sus propiedades

## Las tres propiedades

### Reflexiva
Cada elemento está relacionado **consigo mismo**: (a, a) siempre está en la relación.

> "Todo se relaciona consigo mismo."

**En la matriz:** la diagonal principal está compuesta de 1's.

### Simétrica
Si un elemento se relaciona con otro, el otro también se relaciona con él: si (a, b) está, también debe estar (b, a).

> "Si A está con B, entonces B está con A."

**En la matriz:** la matriz transpuesta es igual a la matriz original.

### Transitiva
Si un elemento se relaciona con un segundo, y ese segundo con un tercero, entonces el primero se relaciona con el tercero: si (a, b) y (b, c) están, también debe estar (a, c).

> "Si A está con B y B con C, entonces A está con C."

## Relación antisimétrica

Una relación es **antisimétrica** cuando: si (a, b) y (b, a) pertenecen a la relación, **entonces necesariamente a = b**.

Dicho de otro modo: si dos elementos **distintos** a ≠ b aparecen en ambos sentidos —(a,b) y (b,a)—, la relación **no** es antisimétrica. No puede haber reciprocidad entre elementos distintos.

### Ejemplo
Sea R = {(1,1), (2,2), (1,2)}.

Aquí no está el par simétrico (2,1), por lo tanto **R es antisimétrica**. ✅

## ⚠️ Corrección de los apuntes

Los apuntes originales decían: *"Relación simétrica: aquella que cumple con las tres características — simétrica, reflexiva, transitiva."*

Eso es incorrecto. La relación que cumple las tres es la **relación de equivalencia**, no la simétrica. Una relación simétrica solo cumple la simetría.

Ver [[Relaciones de equivalencia y particiones]].

## Relacionadas

- [[Cerraduras de relaciones]] — cómo forzar estas mismas propiedades en una relación que no las cumple
- [[Logica proposicional]] — las tres propiedades se enuncian como condicionales: "si (a,b) y (b,c), entonces (a,c)" es una conjunción seguida de →
