---
materia: Arquitectura de redes
semestre: 2
tipo: concepto
tags: [redes, token-ring, ibm, topologia]
---

# Token Ring

Protocolo basado en la **topología de anillo**, propuesto por **IBM**.

## Cómo funciona

Funciona como una red de vagones: mandando paquetes, firmando paquetes y recibiendo paquetes continuamente de forma **unidireccional**.

Como solo puede transmitir quien tiene el testigo (*token*), **se garantiza siempre un tiempo máximo** para envíos y recepciones.

## Ventajas

- **Elimina las colisiones** por la propia naturaleza del sistema de anillo
- Tiempo máximo de entrega garantizado — justo lo que [[CSMA-CD y colisiones|CSMA/CD]] no puede ofrecer
- Prometen mejores velocidades

## Desventaja

Si un bus se rompe, **se rompe todo el anillo**. Se minimiza con un concentrador de información: el **MAU** (Multistation Access Unit).

## Por qué ganó Ethernet

No está en los apuntes, pero es la pregunta natural: Token Ring era técnicamente superior en determinismo y perdió por costo y por el ecosistema abierto de Ethernet. Es el mismo patrón de [[Puertos y conectores|FireWire contra USB]].

## Relacionadas

- [[Clasificacion de redes]] — la topología de anillo y la familia "paso de testigo", los dos cortes donde cae Token Ring
- [[CSMA-CD y colisiones]] — el rival que ganó: escucha con colisiones frente a testigo sin colisiones
