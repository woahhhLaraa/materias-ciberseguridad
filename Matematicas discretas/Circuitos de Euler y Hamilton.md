---
materia: Matematicas discretas
semestre: 1
tipo: concepto
tags: [matematicas, grafos, circuitos]
---

# Circuitos de Euler y Hamilton

Dos recorridos que se confunden con facilidad. **La distinción es qué se visita una sola vez.**

| | Euler | Hamilton |
|---|---|---|
| Pasa una sola vez por | **cada lado** (arista) | **cada vértice** |
| Lo que no importa | los vértices se pueden repetir | los lados no importan |

## Circuito de Euler

Para determinar si un grafo tiene un circuito de Euler:

1. El grafo es **conexo** y todos los vértices tienen **valencia par**
2. Seleccionar un vértice cualquiera para empezar el recorrido
3. Al terminar, se debe haber tocado **todos los lados una sola vez cada uno**, cuidando de no desconectar el grafo
4. Escribir en un conjunto todos los puntos recorridos



## Circuito de Hamilton

Similar a Euler, con la diferencia de que en lugar de pasar por todos los **lados** una sola vez, se pasa por cada **vértice** una sola vez.

1. Partir de un punto cualquiera
2. Pasar por todos los vértices, una sola vez, sin repetir. Los lados no importan.

## Cómo recordarlo

**E**uler → **E**dges (aristas). Hamilton, entonces, es el otro: vértices.

## Relacionadas

- [[Teoria de grafos]] — de ahí salen conexo y valencia, las dos condiciones que deciden si hay circuito de Euler
- [[Isomorfismo de grafos]] — la existencia de circuito de Euler se usa allá para descartar que dos grafos sean isomorfos
