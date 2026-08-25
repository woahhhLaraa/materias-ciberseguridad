---
materia: Matematicas discretas
semestre: 1
tipo: concepto
tags: [matematicas, logica]
---

# Lógica proposicional

## Para qué sirve

La lógica se utiliza para establecer si un razonamiento es **válido o no**, teniendo en cuenta que una frase puede tener diferentes interpretaciones.

En matemáticas es la herramienta para demostrar teoremas, inferir resultados y resolver problemas. En computación se aplica principalmente en el estudio de los **lenguajes formales** y las relaciones entre ellos, así como en la obtención de resultados de forma recursiva.

La demostración formal de teoremas es la representación de enunciados usando notación lógica.

## Proposición

Oración, frase o expresión matemática que puede ser **verdadera o falsa, pero no ambas a la vez**. Es el elemento fundamental de la lógica matemática.

> Nota: en los apuntes originales aparece como "preposición". El término correcto es **proposición** — "preposición" es una categoría gramatical distinta.

## Proposiciones compuestas

Una proposición es compuesta cuando está integrada por dos o más proposiciones simples conectadas por **operadores lógicos**.

| Operador | Símbolo | Nombre |
|---|---|---|
| y | ∧ | Conjunción |
| o | ∨ | Disyunción |
| entonces | → | Condicional |
| si y solo si | ↔ | Bicondicional |

## Ejemplos de clase

### Ejemplo 1
> El automóvil arranca **si y solo si** el tanque tiene gasolina **y** la batería tiene corriente.

- **P**: el automóvil arranca
- **Q**: el tanque tiene gasolina
- **R**: la batería tiene corriente

**P = Q ∧ R**

### Tabla de verdad

| Q | R | P |
|---|---|---|
| 1 | 1 | **1** |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 0 |

La conjunción solo es verdadera cuando **ambas** proposiciones lo son.

### Ejemplo 2
> El alumno tiene derecho a examen si tiene el 80% de asistencias y entregó todas las tareas.

- **P**: el alumno tiene derecho a examen
- **Q**: tiene el 80% de asistencias
- **R**: entregó todas las tareas

**P = Q ∧ R** — misma estructura que el ejemplo anterior.

## Relacionadas

- [[Relaciones y sus propiedades]] — donde el condicional deja de ser un ejemplo de clase y pasa a definir propiedades de una relación
