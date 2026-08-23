---
materia: Organizacion de computadoras
semestre: 1
tipo: concepto
tags: [hardware, entrada-salida, dma]
---

# Técnicas de entrada y salida de datos

Tres formas de mover datos entre un dispositivo y la memoria. Las dos primeras pasan por la CPU; la tercera la evita.

## 1. E/S programada

El procesador envía una orden al módulo de E/S y después **debe hacer comprobaciones periódicas programadas** hasta que la operación concluya. El módulo no realiza ninguna acción para avisar al procesador.

- Es **síncrona**
- ❌ Se desperdicia mucho tiempo de CPU en esperar (*polling*)

## 2. E/S mediante interrupciones

El procesador envía la orden y **se olvida** del asunto. Solo vuelve a atender cuando el módulo de E/S manda un mensaje avisando que terminó.

- Es **asíncrona**
- ✅ El procesador puede hacer otra cosa mientras tanto

## 3. Acceso directo a memoria (DMA)

Se añade un módulo adicional, el **DMA**, para quitarle carga al procesador y que no tenga que dedicar instrucciones a los dispositivos de E/S.

El módulo lleva los datos **directamente a la memoria principal** y solo avisa al procesador cuando la acción ya está hecha.

- Usa interrupciones para el aviso final
- ✅ Es la más eficiente para transferencias grandes: el procesador no toca los datos

## Comparación

| Técnica | ¿Quién espera? | ¿Los datos pasan por la CPU? |
|---|---|---|
| Programada | La CPU, activamente | Sí |
| Interrupciones | Nadie; la CPU trabaja en otra cosa | Sí |
| DMA | Nadie | **No** |

## Relacionadas

- [[Arquitectura de entrada y salida]]
- [[Definicion y funciones del sistema operativo]] — la gestión de dispositivos es función del SO
