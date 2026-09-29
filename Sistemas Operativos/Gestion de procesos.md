---
materia: Sistemas Operativos
semestre: 3
tipo: concepto
tags:
  - sistemas-operativos
  - procesos
  - concurrencia
  - multiprogramacion
sr-due: 2026-10-24
sr-interval: 32
sr-ease: 256
---
#review 
# Gestión de procesos

Cómo el sistema operativo reparte el **tiempo de CPU** entre varias tareas. Es la continuación práctica de la multiprogramación que aparece como dato histórico en [[Generaciones de sistemas operativos]].

Proceso: Programa en ejecucion
## Tiempo de CPU o ráfaga de CPU

Los sistemas con **multiprogramación** llevaron a que un CPU pudiera ejecutar varias tareas de manera simultánea, mediante un **cambio de contexto**. Las tareas comparten el procesador por *quantums* de tiempo.

### Quantum de tiempo

La cantidad de milisegundos que un CPU puede dar a una tarea.

### Cambio de contexto

El momento del cambio de una tarea a otra durante la multiprogramación con tiempo de CPU. Cuando vuelve a la misma tarea que dejó, la reinicia **desde el momento en que se quedó** la última vez.

## Paralelismo y concurrencia

|                  | Qué ocurre                                                                                                                                 | Qué hace falta                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Paralelismo**  | Dos o más procesos se ejecutan **exactamente al mismo tiempo**                                                                             | Varios procesadores, o varios núcleos de un solo procesador |
| **Concurrencia** | Dos o más procesos se ejecutan **uno por uno**, pero con un cambio de contexto tan rápido y eficiente que da la **ilusión** de paralelismo | Un solo núcleo basta                                        |


> La diferencia se apoya en hardware: el paralelismo real depende de que existan varios núcleos. Ver [[MOC - Estructura interna de un CPU]], sección 7.

## Relacionadas

- [[Generaciones de sistemas operativos]] — de dónde viene la multiprogramación ⭐ y el tiempo compartido
- [[Gestion de memoria]] — el otro recurso que el SO reparte: si aquí divide el tiempo, allí divide la memoria
- [[Definicion y funciones del sistema operativo]] — administrar la CPU y gestionar procesos son dos de las funciones esenciales
- [[MOC - Estructura interna de un CPU]] — el multinúcleo es la condición de hardware para que haya paralelismo real
- [[MOC - Hardware a sistema operativo]] — el hilo que esta nota cierra: la espera del procesador frente a los trabajos
