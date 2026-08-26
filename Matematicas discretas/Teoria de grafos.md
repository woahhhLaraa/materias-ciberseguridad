---
materia: Matematicas discretas
semestre: 1
tipo: concepto
tags: [matematicas, grafos]
---

# Teoría de grafos

> Clase del 13/11/2025

## Qué son

Representaciones de redes para expresar de forma visual y sencilla la relación entre elementos, comúnmente del mismo tipo.

**Para qué sirven:** mediante la teoría de grafos se pueden aprovechar mejor los recursos, eliminando conexiones redundantes y reduciendo costos y distancias.

## Vocabulario

| Término | Símbolo | Definición |
|---|---|---|
| **Grafo** | G | La estructura completa |
| **Vértices** o nodos | V | Los puntos |
| **Lados**, ramas o aristas | L | Las conexiones |
| **Lazo** | — | Arista que sale de un vértice y regresa al mismo vértice |
| **Valencia** de un vértice | — | Número de lados que entran y/o salen de un vértice |

## Tipos de grafos

### Grafo simple
No tiene lazos ni lados paralelos.

### Grafo completo
Grafo en donde cada vértice está relacionado con todos los demás, sin lazos ni lados paralelos. Se indica como **Kₙ**, donde n es el número de vértices.

En un grafo completo:

```
Valencia de cada vértice = n − 1

                      n(n − 1)
Número de lados  =  ───────────
                          2
```

### Comprobación rápida
K₄: valencia 3 en cada vértice, y 4(3)/2 = **6 lados**. ✓

## Relacionadas

- [[Circuitos de Euler y Hamilton]] — los dos recorridos que se definen sobre un grafo; el de Euler se decide con la valencia de los vértices
- [[Isomorfismo de grafos]] — cuándo dos grafos de aspecto distinto son el mismo; se decide comparando vértices, lados y valencias
- [[Clasificacion de redes]] — la topología de red es un grafo
- [[Relaciones de equivalencia y particiones]] — el otro eslabón del hilo hacia redes: reflexiva, simétrica y transitiva son los requisitos de conectividad que el grafo dibuja
