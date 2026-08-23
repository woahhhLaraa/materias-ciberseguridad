---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, memoria, cache]
---

# Jerarquía de memoria

Dentro de un procesador tenemos la unidad lógica, la unidad de control y los registros.

## Memoria caché

Intermediario entre la memoria principal y el procesador.

- Es **más lenta que el procesador pero más rápida que la memoria principal**

El motivo de su existencia es una diferencia de velocidades: el procesador trabaja a una frecuencia mayor que la de la memoria principal, y el bus de esa memoria maneja su propia frecuencia. Sin un intermediario, el procesador pasaría el tiempo esperando.

> El **bus** es la carretera donde se transmite la información. Ver [[Buses y estructuras de interconexion]].

### Tipos de transferencia

- Memoria principal ↔ caché: **transferencia de bloques** (de palabras)
- Caché ↔ CPU: **transferencia de palabras**

### Orden de búsqueda

El procesador **primero revisa la caché**, y solo después la memoria principal. Por eficiencia.

### Niveles

Existen niveles L1, L2, L3, etc., según el procesador y por cada núcleo.

- **Cuanto menor el nivel, más eficiente** (L1 es la más rápida)
- Además hay una caché compartida entre núcleos. Normalmente el nivel más alto es el compartido.

## Memoria virtual

También llamada **archivo de paginación**.

Método económico para aumentar el tamaño de la memoria usando espacio en disco. Se toma espacio de disco para hacerle creer al sistema operativo que hay más memoria de la que realmente existe.

- Menor costo
- Normalmente guarda datos de acceso poco frecuente

### Organización

Existen **direcciones físicas** y **direcciones virtuales**; la traducción entre ambas es lo que hace posible la ilusión.

## Mapa de memoria

Espacios de memoria asignados a distintos propósitos:

- Para el **sistema operativo**
- Espacio de **usuario** — el que todos los usuarios pueden modificar
- Espacio de **pila** — variables y datos temporales de los programas
- Espacios para **dispositivos de entrada y salida**

## Relacionadas

- [[Definicion y funciones del sistema operativo]] — gestionar memoria es una de sus funciones principales
- [[Arreglos de discos RAID]]
- [[Generaciones de computadoras]] — la caché L1/L2/L3 aparece en la sexta generación
