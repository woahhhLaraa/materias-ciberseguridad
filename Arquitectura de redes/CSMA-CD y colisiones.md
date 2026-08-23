---
materia: Arquitectura de redes
semestre: 2
tipo: concepto
tags: [redes, ethernet, csma, colisiones]
---

# CSMA/CD y colisiones

> Clase del 2/11/26

Toda la información que pase por los cables con el protocolo **CSMA/CD**, creado a partir de Ethernet, tiene que lidiar con la **colisión**: cuando la información se solapa porque varios sistemas hablan al mismo tiempo.

## El procedimiento

1. Se comprueba si todos los dispositivos están callados
2. ¿El medio está disponible?
   - **No** → no se envía; se espera (máximo 16 intentos)
   - **Sí** → se envía el mensaje
3. ¿Ocurrió alguna colisión?
   - **No** → el mensaje fue transmitido correctamente
   - **Sí** → volver a retransmitir, con un máximo de 16 intentos

## Half duplex vs. full duplex

- **Half duplex** — solamente oye **o** habla
- **Full duplex** — habla **y** escucha simultáneamente

## Variantes de persistencia

| Variante | Comportamiento |
|---|---|
| **Persistente** | Escucha persistentemente hasta tener espacio para hablar |
| **No persistente** | Tiempos de escucha aleatorios, y luego habla |
| **Probabilísticamente persistente** | Combinación: escucha persistentemente, pero sus tiempos de habla son aleatorios |

La aleatoriedad existe para evitar que dos estaciones que esperan al mismo tiempo vuelvan a colisionar en cuanto el medio se libere.

## Desventaja principal

**No hay tiempo máximo de entrega garantizado.** Todos los mensajes pueden tardar tiempos distintos según el tráfico. Además, la mayoría de las redes con este protocolo son half duplex.

Ese es precisamente el problema que [[Token Ring]] resuelve.

## Relacionadas

- [[Clasificacion de redes]]
- [[Protocolos y modelos]]
