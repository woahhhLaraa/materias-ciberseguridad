---
materia: Sistemas Operativos
semestre: 3
tipo: concepto
tags:
  - sistemas-operativos
  - memoria
  - paginacion
  - mmu
sr-due: 2026-09-23
sr-interval: 14
sr-ease: 256
---
#review 
# Gestión de memoria

Cómo el sistema operativo administra el uso de la memoria principal entre los programas. Es una de las funciones esenciales listadas en [[Definicion y funciones del sistema operativo]].

## Memoria virtual

Es un **concepto**, o una ilusión que crea el sistema operativo para los programas. Sirve para manejar el uso del espacio de la memoria principal, evitando que los programas "se pisen" al escribir en ella.

Además, si esa memoria real se llegase a quedar sin espacio (por un proceso muy complejo, o por múltiples procesos), tiene permitido **asignar un espacio de la memoria secundaria** para su beneficio.

> Este mismo tema aparece en [[Jerarquia de memoria]] desde el lado del hardware, donde se le llama *archivo de paginación* y se presenta como un método económico para aumentar el tamaño de la memoria usando disco. Aquí se ve desde el software: quién crea la ilusión y cómo.

## Paginación

Si bien la memoria virtual es un concepto, la **paginación es la técnica** que utiliza para lograr lo que conocemos como memoria virtual.

El sistema operativo le da a cada programa o proceso un **"mapa de apodos"** o mapa virtual propio de la memoria, para hacerle creer que tiene todo el acceso a la memoria para él solo y de forma secuencial.

- El programa usa esos "apodos" para referirse a la memoria real, **sin saber ni cómo se llama de verdad ni dónde está ubicada físicamente**
- El sistema operativo solo interviene en la creación, la expansión o la resolución de problemas del mapa virtual

## La MMU

La **MMU** (unidad de gestión de memoria) lee esos "apodos" y los **traduce** para meter los datos en los espacios reales de la memoria principal. La escritura sucede directamente en el lugar físico de la memoria, sin un lugar intermedio donde se almacene el dato.

Es un componente de **hardware físico que existe dentro de la propia CPU**, pero que no forma parte de su esquema lógico.

Su razón de existir es **bajar la carga lógica del CPU**: miles de millones de entradas a la memoria le quitarían mucho tiempo y poder de procesamiento.

> Es el mismo argumento que justifica el DMA en [[Tecnicas de entrada y salida]]: añadir un módulo dedicado para que el procesador no gaste instrucciones en trabajo repetitivo.

## Relacionadas

- [[Jerarquia de memoria]] — la misma memoria virtual vista desde el hardware, con la caché y el mapa de memoria
- [[Gestion de procesos]] — el otro recurso que el SO reparte: si aquí divide la memoria, allí divide el tiempo de CPU
- [[Definicion y funciones del sistema operativo]] — gestionar memoria es una de las funciones esenciales
- [[Tecnicas de entrada y salida]] — el DMA responde al mismo principio que la MMU: descargar al procesador
- [[MOC - Hardware a sistema operativo]] — el hilo donde esta nota continúa a la jerarquía de memoria
