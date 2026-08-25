---
tipo: moc
hilo: cpu-interno
tags: [moc, hardware, arquitectura, cpu, memoria]
semestres: [1]
---

# MOC — Estructura interna de un CPU

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[Jerarquia de memoria]] (sem. 1)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

> ⚠️ MOC en construcción. Solo [[Jerarquia de memoria]] está consolidada; las demás secciones son el esqueleto del tema y siguen vacías. **El arco del hilo** se escribe cuando haya al menos dos notas en la cadena.

## Modelo de von Neumann

## Componentes del procesador

### Unidad aritmético-lógica (ALU)

### Unidad de control

### Registros

## Jerarquía de memoria

*Fuente: [[Jerarquia de memoria]] — Organización de computadoras, sem. 1*

Dentro de un procesador tenemos la unidad lógica, la unidad de control y los registros; son los componentes de la sección *Componentes del procesador* de este documento.

### Memoria caché

Intermediario entre la memoria principal y el procesador.

- Es **más lenta que el procesador pero más rápida que la memoria principal**

El motivo de su existencia es una diferencia de velocidades: el procesador trabaja a una frecuencia mayor que la de la memoria principal, y el bus de esa memoria maneja su propia frecuencia. Sin un intermediario, el procesador pasaría el tiempo esperando.

> El **bus** es la carretera donde se transmite la información. Ver [[Buses y estructuras de interconexion]].

#### Tipos de transferencia

- Memoria principal ↔ caché: **transferencia de bloques** (de palabras)
- Caché ↔ CPU: **transferencia de palabras**

#### Orden de búsqueda

El procesador **primero revisa la caché**, y solo después la memoria principal. Por eficiencia.

#### Niveles

Existen niveles L1, L2, L3, etc., según el procesador y por cada núcleo.

- **Cuanto menor el nivel, más eficiente** (L1 es la más rápida)
- Además hay una caché compartida entre núcleos. Normalmente el nivel más alto es el compartido.

### Memoria virtual

También llamada **archivo de paginación**.

Método económico para aumentar el tamaño de la memoria usando espacio en disco. Se toma espacio de disco para hacerle creer al sistema operativo que hay más memoria de la que realmente existe.

- Menor costo
- Normalmente guarda datos de acceso poco frecuente

#### Organización

Existen **direcciones físicas** y **direcciones virtuales**; la traducción entre ambas es lo que hace posible la ilusión.

### Mapa de memoria

Espacios de memoria asignados a distintos propósitos:

- Para el **sistema operativo**
- Espacio de **usuario** — el que todos los usuarios pueden modificar
- Espacio de **pila** — variables y datos temporales de los programas
- Espacios para **dispositivos de entrada y salida**

## Ciclo de instrucción

## Segmentación (pipeline)

## Arquitecturas RISC y CISC

## Multinúcleo

## Relacionadas

- [[Jerarquia de memoria]] — la nota fuente de la sección consolidada aquí arriba
- [[MOC - Hardware a sistema operativo]] — el otro hilo donde también vive [[Jerarquia de memoria]]; ahí se estudia junto a las generaciones de hardware y de SO
- [[Buses y estructuras de interconexion]] — los buses conectan el CPU con la memoria y los dispositivos
- [[Arquitectura de entrada y salida]] — cómo el procesador se comunica con los módulos de E/S
- [[Tecnicas de entrada y salida]] — E/S programada, interrupciones y DMA: cuánta carga recae en el CPU
- [[Generaciones de computadoras]] — el microprocesador y la ejecución en paralelo aparecen en la cuarta y quinta generación; la caché L1/L2/L3, en la sexta
- [[Definicion y funciones del sistema operativo]] — gestionar memoria es una de sus funciones principales
- [[Arreglos de discos RAID]] — el nivel más lento de la jerarquía, ya fuera del procesador
- [[00 - Indice]] — el índice maestro con todos los hilos
