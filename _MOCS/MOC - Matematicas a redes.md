---
tipo: moc
hilo: matematicas-redes
tags: [moc, matematicas, grafos, redes, topologia]
semestres: [1, 2]
---
#review
# MOC — Matemáticas → redes

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[Teoria de grafos]] (sem. 1) → [[Relaciones de equivalencia y particiones]] (sem. 1) → [[Clasificacion de redes|topologías de red]] (sem. 2)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

## El arco del hilo

El hilo más corto y el más señalado en clase: la profesora de Matemáticas discretas dijo explícitamente que las relaciones de equivalencia importan **porque son una propiedad que deben tener las redes**. Un año después, en Arquitectura de redes, la topología aparece definida como "la forma de la red en cuanto a conectividad física" — que es literalmente un grafo. Las dos notas de primer semestre son el aparato formal de algo que en segundo se usa sin nombrarlo:

- Un **grafo** es la topología: vértices = dispositivos, aristas = enlaces, valencia = número de conexiones de un nodo.
- Las **propiedades de equivalencia** son los requisitos de conectividad: reflexiva (loopback), simétrica (comunicación bidireccional), transitiva (enrutamiento por saltos).
- Las **fórmulas del grafo completo** dan el costo del cableado punto a punto: n(n−1)/2 enlaces para conectar todo con todo — la razón por la que las topologías reales no son completas.

---

## 1. Teoría de grafos

*Fuente: [[Teoria de grafos]] — Matemáticas discretas, sem. 1*

> Clase del 13/11/2025

### Qué son

Representaciones de redes para expresar de forma visual y sencilla la relación entre elementos, comúnmente del mismo tipo.

**Para qué sirven:** mediante la teoría de grafos se pueden aprovechar mejor los recursos, eliminando conexiones redundantes y reduciendo costos y distancias.

### Vocabulario

| Término | Símbolo | Definición |
|---|---|---|
| **Grafo** | G | La estructura completa |
| **Vértices** o nodos | V | Los puntos |
| **Lados**, ramas o aristas | L | Las conexiones |
| **Lazo** | — | Arista que sale de un vértice y regresa al mismo vértice |
| **Valencia** de un vértice | — | Número de lados que entran y/o salen de un vértice |

### Tipos de grafos

#### Grafo simple
No tiene lazos ni lados paralelos.

#### Grafo completo
Grafo en donde cada vértice está relacionado con todos los demás, sin lazos ni lados paralelos. Se indica como **Kₙ**, donde n es el número de vértices.

En un grafo completo:

```
Valencia de cada vértice = n − 1

                      n(n − 1)
Número de lados  =  ───────────
                          2
```

#### Comprobación rápida
K₄: valencia 3 en cada vértice, y 4(3)/2 = **6 lados**. ✓

Ver también [[Circuitos de Euler y Hamilton]] e [[Isomorfismo de grafos]].

---

## 2. Relaciones de equivalencia y particiones

*Fuente: [[Relaciones de equivalencia y particiones]] — Matemáticas discretas, sem. 1*

### Definición

Una **relación de equivalencia** es aquella que cumple las tres propiedades a la vez:

- **Reflexiva**
- **Simétrica**
- **Transitiva**

Ver [[Relaciones y sus propiedades]] para cada una.

Fórmula de comprobación de la transitividad por matrices: `Mr = MR + MR²`

### Particiones

Una **partición** es un conjunto de clases de equivalencia con dos propiedades:

1. Deben estar contenidos **todos** los elementos del conjunto A
2. La intersección entre las clases de equivalencia debe ser **vacía**

### Ejercicio de clase

![[matriz-relacion-ejercicio-1.png]]

![[matriz-relacion-ejercicio-2.png]]

Como se trata de una relación de equivalencia, sus clases de equivalencia son:

El "1" está presente en las posiciones (1,1), (1,2) y (1,5). Recorriendo cada elemento:

| Elemento | Clase     |
| -------- | --------- |
| 1        | {1, 2, 5} |
| 2        | {1, 2, 5} |
| 3        | {3, 4}    |
| 4        | {3, 4}    |
| 5        | {1, 2, 5} |

Cuando se repiten los elementos en cada clase, decimos que tenemos **particiones**. Aquí hay dos: **{1, 2, 5}** y **{3, 4}**.

### Por qué esto importa en redes 

La profesora lo señaló explícitamente: las relaciones de equivalencia son importantes porque **es una propiedad que deben tener las redes**.

- **Simetría** — la computadora 1 puede enviar información a la computadora 2, pero además la 2 puede comunicarse con la 1
- **Reflexividad** — toda computadora tiene comunicación consigo misma
- **Transitividad** — si existe un camino de 1 a 2, y otro de 2 a 5, debe haber uno de 1 a 5

Esta es la conexión formal entre esta materia y [[Introduccion a las redes de computo]].

---

## 3. Clasificación de redes

*Fuente: [[Clasificacion de redes]] — Arquitectura de redes, sem. 2*

> Fundamentos de arquitecturas de redes

Las redes se clasifican por tamaño, alcance y dimensiones.

### Por alcance geográfico

| Sigla | Nombre | Alcance |
|---|---|---|
| **PAN** | Personal Area Network | Personal |
| **LAN** | Local Area Network | Local |
| **MAN** | Metropolitan Area Network | Metropolitana |
| **WAN** | Wide Area Network | Área amplia |
| **GAN** | Global Area Network | Global |

### Por topología

La **topología de red** establece la forma de la red en cuanto a **conectividad física**.

Su objetivo es la **fiabilidad del tráfico** para el envío correcto de datos.

Formalmente, una topología es un grafo — ver la sección 1 de este documento.

### Por protocolo de comunicación

Dos familias:

| Familia | Ejemplos |
|---|---|
| **Sistemas con escucha** | Redes Ethernet — ver [[CSMA-CD y colisiones]] |
| **Paso de testigo** | Redes Token Ring, Token Bus — ver [[Token Ring]] |

La diferencia de fondo: en los sistemas con escucha cualquiera puede hablar cuando cree que hay silencio (y a veces chocan); en el paso de testigo solo habla quien tiene el testigo (y nunca chocan).

---

## Relacionadas

- [[00 - Indice]] — el índice maestro con todos los hilos
- [[Cerraduras de relaciones]] — qué hacer cuando una relación *no* es de equivalencia
- [[Componentes de red]]
- [[Diseno de red LAN]]
- [[Representaciones de red y topologias]]
