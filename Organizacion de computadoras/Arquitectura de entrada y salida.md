---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, entrada-salida]
---

# Arquitectura de entrada/salida

## Dispositivos externos y periféricos

Requieren un **módulo de E/S** para conectarse.

**Módulo de E/S:** hardware que conecta la entrada/salida con el computador mediante buses.

### Tipos de periféricos

- De interacción con humanos
- De interacción con máquinas
- De comunicación general

### Forma general de un dispositivo externo

Tres partes: **lógica de control**, **buffer** y **transductor**.

## Direccionamiento

Cada dispositivo de E/S tiene una **dirección única**.

## Funciones de un módulo de E/S

1. **Control y temporización** — coordinar el tráfico entre los recursos internos y los dispositivos externos
2. **Comunicación con el procesador** — intercambio de datos a través del bus de datos
3. **Comunicación con los dispositivos externos** — intercambio de órdenes, información de estado y datos
4. **Almacenamiento temporal de datos** (*data buffering*)
5. **Detección de errores** — detectarlos e informarlos al procesador

El punto 4 existe por la misma razón que la caché: los dispositivos externos y el procesador operan a velocidades incompatibles. Ver [[Jerarquia de memoria]].

## Relacionadas

- [[Tecnicas de entrada y salida]] — las tres formas de mover los datos que estos módulos transportan: programada, interrupciones y DMA
- [[Buses y estructuras de interconexion]] — por dónde se conecta el módulo de E/S con el resto de la máquina
- [[Puertos y conectores]] — los conectores físicos concretos por los que entran estos periféricos
