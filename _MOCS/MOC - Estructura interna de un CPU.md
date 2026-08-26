---
tipo: moc
hilo: estructura-cpu
tags: [moc, hardware, arquitectura, cpu, memoria]
semestres: [1]
---
#review

# MOC — Estructura interna de un CPU

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[Jerarquia de memoria]] (sem. 1)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

⚠️ Hilo en construcción. De momento solo la jerarquía de memoria tiene nota; las secciones 2 a 7 son el esqueleto de lo que falta capturar de Organización de computadoras.

## El arco del hilo

El procesador no es una caja que ejecuta instrucciones: es un conjunto de piezas que trabajan a velocidades distintas, y casi todo su diseño interno sale de administrar esa diferencia.

La **jerarquía de memoria** es el caso más visible del problema. El procesador corre más rápido que la memoria principal, así que sin un intermediario pasaría el tiempo esperando: de ahí la caché, y de ahí que tenga niveles. La misma lógica reaparece en la **arquitectura de entrada y salida**, donde los dispositivos externos son todavía más lentos y hacen falta módulos que amortigüen la diferencia.

Las secciones pendientes son las otras piezas de ese mismo reparto: la **ALU** y la **unidad de control** como las que ejecutan y coordinan, los **registros** como el escalón más rápido de la jerarquía, la **segmentación** como forma de que ninguna pieza quede ociosa, y **RISC/CISC** y **multinúcleo** como las dos apuestas históricas sobre cómo repartir el trabajo.

---

## 1. Jerarquía de memoria

*Fuente: [[Jerarquia de memoria]] — Organización de computadoras, sem. 1*

Dentro de un procesador tenemos la unidad lógica, la unidad de control y los registros — las piezas que desarrollan las secciones siguientes de este documento.

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

---

## 2. Modelo de von Neumann

⚠️ Pendiente de capturar.

## 3. Componentes del procesador

⚠️ Pendiente de capturar.

### Unidad aritmético-lógica (ALU)

### Unidad de control

### Registros

## 4. Ciclo de instrucción

⚠️ Pendiente de capturar.

## 5. Segmentación (pipeline)

⚠️ Pendiente de capturar.

## 6. Arquitecturas RISC y CISC

⚠️ Pendiente de capturar.

## 7. Multinúcleo

⚠️ Pendiente de capturar.

---

## Relacionadas

- [[00 - Indice]] — el índice maestro con todos los hilos
- [[MOC - Hardware a sistema operativo]] — el otro hilo que pasa por la jerarquía de memoria, encadenándola hacia el SO
- [[Buses y estructuras de interconexion]] — los buses conectan el CPU con la memoria y los dispositivos
- [[Arquitectura de entrada y salida]] — cómo el procesador se comunica con los módulos de E/S
- [[Tecnicas de entrada y salida]] — E/S programada, interrupciones y DMA: cuánta carga recae en el CPU
- [[Generaciones de computadoras]] — el microprocesador y la ejecución en paralelo aparecen en la cuarta y quinta generación
