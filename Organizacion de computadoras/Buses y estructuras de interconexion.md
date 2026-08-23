---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, buses, entrada-salida]
---

# Buses y estructuras de interconexión

**Bus:** conjunto de conductores eléctricos paralelos para manejar información. Cada línea de datos maneja 1 bit. Permiten interconectar todos los componentes de una computadora.

## Tipos de línea por función

- **Líneas de datos**
- **Líneas de direcciones** (de memoria)
- **Líneas de control** — señales para controlar cómo se usan los demás buses (*memory write*, *memory read*). Son especialmente necesarias porque los buses son **medios compartidos**: hay que controlar quién los usa y en qué momento.

## Ubicación

Un bus puede estar en un chip (*on-chip*) o en la tarjeta madre (*on-board*).

## Retardo de propagación

Los buses tienen una jerarquía para su gestión. Cuantos más dispositivos, más tiempo toma, lo que aumenta el **retardo de propagación**. Se intenta evitar la acumulación de peticiones de transferencia, que genera cuello de botella.

## Tipos de línea por dedicación

### Dedicadas
Líneas que solo llevan cierto tipo de datos.
- ✅ **Ventaja:** rendimiento; reduce conflictos por uso del bus
- ❌ **Desventaja:** incrementa el tamaño y el costo del sistema

### Multiplexadas
Líneas con diferentes propósitos, gestionadas por un "tomador de decisiones" (las líneas de control).
- ✅ **Ventajas:** menos líneas, reducción de espacio
- ❌ **Desventajas:** circuitería más compleja; no permite eventos en paralelo (o transmites un dato o transmites otro)

## Métodos de arbitraje

Quién decide qué dispositivo usa el bus:

- **Centralizado** — un único dispositivo de hardware asigna los tiempos del bus
- **Distribuido** — todos los dispositivos deben ser capaces de organizarse entre ellos

Terminología: el árbitro se conoce como **maestro** del bus; el dispositivo con el que interactúa, como **esclavo**.

## Temporización

Cómo se coordinan los eventos en el bus:

- **Síncrona** — la presencia de un evento la determina un reloj, respetando intervalos fijos. Todos los dispositivos usan la misma frecuencia.
- **Asíncrona** — los dispositivos pueden funcionar a diferentes frecuencias.

## Transferencia de datos

- **Escritura**: dato de maestro a esclavo
- **Lectura**: dato de esclavo a maestro

Según el tipo de bus:
- **Multiplexado**: primero la dirección, después la transferencia del dato
- **Dedicado**: siempre es el mismo bus de dirección, se escriba o se lea
- Existen buses de operaciones combinadas

## Relacionadas

- [[Puertos y conectores]]
- [[Jerarquia de memoria]]
- [[Arquitectura de entrada y salida]]
