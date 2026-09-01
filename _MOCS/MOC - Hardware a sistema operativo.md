---
tipo: moc
hilo: hardware-so
tags:
  - moc
  - hardware
  - sistemas-operativos
  - historia
  - memoria
  - procesos
  - paginacion
semestres:
  - 1
  - 3
sr-due: 2026-09-12
sr-interval: 14
sr-ease: 270
---
#review

# MOC — Hardware → sistema operativo

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[Generaciones de computadoras]] (sem. 1) → [[Jerarquia de memoria]] (sem. 1) → [[Tecnicas de entrada y salida]] (sem. 1) → [[Generaciones de sistemas operativos]] (sem. 3) → [[Gestion de memoria]] (sem. 3) → [[Gestion de procesos]] (sem. 3)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

## El arco del hilo

Dos cronologías de la misma historia —hardware en primer semestre, software en tercero— más las piezas que explican *por qué* el software tuvo que aparecer. La idea de fondo se repite en todas las notas técnicas: **cada avance del SO existe porque el procesador era más rápido que lo que lo rodeaba y había que dejar de hacerlo esperar.** La caché resuelve la espera frente a la memoria; las interrupciones y el DMA la resuelven frente a los dispositivos; la multiprogramación y el tiempo compartido la resuelven frente a los trabajos.

Las dos últimas secciones cierran el arco volviendo sobre los mismos objetos, ya desde el software. La **gestión de memoria** retoma la memoria virtual que la sección 2 presentó como un truco de hardware y muestra quién la construye: la paginación, el mapa virtual por proceso y la MMU —que existe por el mismo motivo que el DMA de la sección 3, descargar al procesador de trabajo repetitivo—. La **gestión de procesos** hace lo propio con la multiprogramación que la sección 4 dejó como dato histórico ⭐, y explica el mecanismo: quantums y cambio de contexto.

Visto entero, el hilo describe **un solo reparto**. El SO administra dos recursos con la misma estrategia de dividir y simular: divide la memoria y le hace creer a cada programa que la tiene entera; divide el tiempo y le hace creer a cada tarea que tiene el procesador entero. La paginación y la concurrencia son la misma idea aplicada a ejes distintos.

### Las dos cronologías alineadas

| Época | Hardware (sem. 1) | Sistemas operativos (sem. 3) |
|---|---|---|
| 1940-1955 | 1ª gen — tubos de vacío, ENIAC, UNIVAC, EDVAC | 1ª gen — **no había SO** |
| 1955-1965 | 2ª gen — transistor, IBM 1401, COBOL/FORTRAN | 2ª gen — mainframes, sistemas por lotes |
| 1965-1980 | (circuitos integrados) | 3ª gen — multiprogramación ⭐, spooling ⭐, tiempo compartido |
| 1971-1990 | 4ª gen — microprocesadores, VLSI, PC | 4ª gen — DOS, UNIX, interfaces gráficas |
| 1990-hoy | 5ª y 6ª gen — portátiles, paralelo/vectorial, caché L1/L2/L3 | 5ª gen — móviles, Android, iOS, HarmonyOS |

> ⚠️ Las dos clasificaciones no numeran igual: la 3ª generación de SO (1965-1980) cae dentro de lo que hardware cuenta como parte de la 4ª. No mezclar los números en el examen; cada materia usa su propia tabla.

---

## 1. Generaciones de computadoras

*Fuente: [[Generaciones de computadoras]] — Organización de computadoras, sem. 1*

### Primera generación (1940-1956)

Comienza con las máquinas de cálculo automáticas con propósitos militares en la Segunda Guerra Mundial, basadas en **válvulas y tubos de vacío**.

**Charles Babbage** fue la primera persona que tuvo la idea de una máquina de cálculo programable.

**Características:** tubos de vacío; tarjetas perforadas para introducir datos y programas; cilindros magnéticos para almacenar información e instrucciones internas.

**Equipos destacados:**
- **ENIAC** (1946) — primera computadora electrónica de propósito general
- **UNIVAC** (1951) — primer ordenador comercialmente exitoso, aplicaciones científicas y comerciales
- **EDVAC** (1946) — introdujo el concepto de **programa almacenado en memoria**, permitiendo ejecutar instrucciones guardadas en ella

### Segunda generación

Nace con el **transistor**, que sustituye a las válvulas de vacío actuando como interruptor o amplificador. Creado por **John Bardeen, Walter Brattain y William Shockley**.

**Características:**
- Menor tamaño y menor calor
- Consumo eléctrico reducido
- Redes de núcleos magnéticos para almacenamiento; por primera vez las instrucciones podían guardarse directamente en la memoria
- Nacen **COBOL** y **FORTRAN**
- Primer sistema de disco magnético, de 5 MB

**Modelo emblemático:** IBM 1401 — lector de tarjetas, unidad de cinta, consola y CPU.

**Innovaciones clave:** el transistor y el circuito integrado.

**Impacto:** se usó para el primer simulador de vuelo, la primera vez que la computación salía de la investigación pura.


### Tercera Generacion
Se empiezan a utilizar los chips de silicio, dando cabida a procesadores mas pequenos, con menos consumo energetico y mas poder de procesamiento

**Características:**
- Nacimiento del a multiprogramacion
- Nacimiento de los lenguajes de programacion (Se dejan de usar tarjetas perforadas)
- El nacimiento de los primeros OS

**Eventos importantes
- Uso de chips de silicio

### Cuarta generación (1971-1984)

> Las fuentes varían en la fecha de cierre. Todas coinciden en que inicia en 1971.

**Características:**
- Nacen los **microprocesadores**
- Tecnología **VLSI**: chips extremadamente rápidos que permitieron el desarrollo de microprocesadores
- Nace la **computadora personal**
- Desarrollo de SO y lenguajes: sistemas de tiempo compartido, tiempo real. Nacen C, C++ y dBASE
- Nace el precursor de internet

**Eventos importantes:** aparecen los primeros virus y antivirus; creación del disquete (*floppy disk*).

**Equipos destacados:**
- **Altair 8800** — una de las primeras microcomputadoras
- **Apple II** (1977) — con el primer Apple OS, para uso común
- **Commodore PET** — primer ordenador personal de Commodore

### Quinta generación

Se diversificó hacia equipos **portátiles, livianos y cotidianos**. Revolucionaron el mercado e impulsaron una nueva idea de uso: la computadora ya no necesitaba estar fija en un mueble.

- Primera supercomputadora
- Lectura de información escrita
- Los procesadores ejecutan varias etapas de las instrucciones **en paralelo**

### Sexta generación (1990-actualidad)

Se caracteriza por su arquitectura:
- Arquitecturas combinadas **paralelo/vectorial**, con miles de procesadores vectoriales trabajando simultáneamente
- Las redes WAN mundiales crecen mediante fibra óptica y satélite
- Microprocesadores con **caché interna en tres niveles** (L1, L2, L3), con tamaños de decenas de MB

Nacen también las minicomputadoras.

---

## 2. Jerarquía de memoria

*Fuente: [[Jerarquia de memoria]] — Organización de computadoras, sem. 1*

Dentro de un procesador tenemos la unidad lógica, la unidad de control y los registros. Ver [[MOC - Estructura interna de un CPU]].

### Memoria caché

Intermediario entre la memoria principal (RAM) y el procesador.

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

## 3. Técnicas de entrada y salida de datos

*Fuente: [[Tecnicas de entrada y salida]] — Organización de computadoras, sem. 1*

Tres formas de mover datos entre un dispositivo y la memoria. Las dos primeras pasan por la CPU; la tercera la evita.

### 1. E/S programada

El procesador envía una orden al módulo de E/S y después **debe hacer comprobaciones periódicas programadas** hasta que la operación concluya. El módulo no realiza ninguna acción para avisar al procesador.

- Es **síncrona**
- Se desperdicia mucho tiempo de CPU en esperar (*polling*)

### 2. E/S mediante interrupciones

El procesador envía la orden y **se olvida** del asunto. Solo vuelve a atender cuando el módulo de E/S manda un mensaje avisando que terminó.

- Es **asíncrona**
- ✅ El procesador puede hacer otra cosa mientras tanto

### 3. Acceso directo a memoria (DMA)

Se añade un módulo adicional, el **DMA**, para quitarle carga al procesador y que no tenga que dedicar instrucciones a los dispositivos de E/S.

El módulo lleva los datos **directamente a la memoria principal** y solo avisa al procesador cuando la acción ya está hecha.

- Usa interrupciones para el aviso final
- ✅ Es la más eficiente para transferencias grandes: el procesador no toca los datos

### Comparación

| Técnica        | ¿Quién espera?                     | ¿Los datos pasan por la CPU? |
| -------------- | ---------------------------------- | ---------------------------- |
| Programada     | La CPU, activamente                | Sí                           |
| Interrupciones | Nadie; la CPU trabaja en otra cosa | Sí                           |
| DMA            | Nadie                              | **No**                       |

---

## 4. Generaciones de sistemas operativos

*Fuente: [[Generaciones de sistemas operativos]] — Sistemas Operativos, sem. 3*

La evolución del SO está estrechamente ligada a la evolución de las **arquitecturas de computadoras** sobre las que se ejecutan. Clasificación de cinco generaciones según **Tanenbaum y Herbert Bos**. Las fechas son referenciales.

### 1ª generación — 1945-1955
Primeras computadoras eléctricas con **tubos de vacío**.
- Todo era mecánico
- Se ejecutaba directamente sobre el hardware
- Todo en lenguaje máquina
- **No había sistema operativo**

### 2ª generación — 1955-1965
- **Mainframes**
- Automatización de tareas
- Uso del **transistor** (sustituye a los tubos de vacío)
- **Sistemas por lotes** — el antecesor del SO como lo conocemos
- Código en FORTRAN y ensamblador, transferido a tarjetas perforadas

### 3ª generación — 1965-1980
- **Circuitos integrados**, componentes electrónicos más pequeños
- ⭐ **Multiprogramación** (tema de examen): técnica que permite tener varios trabajos cargados en memoria. Es la evolución del procesamiento por lotes.
- ⭐ **Spooling** (tema de examen): técnica que permite leer y almacenar los trabajos de las tarjetas directamente **en el disco**, en lugar de cargarlos en memoria principal.
- **Tiempo compartido**: variante de multiprogramación para que varios usuarios usen la computadora de forma interactiva, compartiendo recursos mediante pequeños turnos
- El SO ya administra los recursos de forma compleja
- Interfaces CLI

> Diferencia clave entre los dos temas de examen: **multiprogramación** carga varios trabajos en *memoria*; **spooling** los almacena en *disco*.

### 4ª generación — 1980-1990
- **Computadoras personales**, más compactas
- Circuitos aún más pequeños
- Primer microprocesador: **Intel 8080** (1974), 8 bits, propósito general
- Primeros SO para PC: DOS, MS-DOS, Windows, Linux, UNIX, BSD
- Nacen las **interfaces gráficas** *user friendly*
- Las PC empiezan a conectarse mediante redes

### 5ª generación — 1990-actualidad
- Nacen los **dispositivos móviles** con sus SO y su integración a internet y la vida diaria
- La comunicación inalámbrica adquiere gran importancia
- Nacen **Android**, **iOS** y **HarmonyOS**

---

## 5. Gestión de memoria

*Fuente: [[Gestion de memoria]] — Sistemas Operativos, sem. 3*

Cómo el sistema operativo administra el uso de la memoria principal entre los programas. Es una de las funciones esenciales listadas en [[Definicion y funciones del sistema operativo]].

### Memoria virtual

Es un **concepto**, o una ilusión que crea el sistema operativo para los programas. Sirve para manejar el uso del espacio de la memoria principal, evitando que los programas "se pisen" al escribir en ella.

Además, si esa memoria real se llegase a quedar sin espacio (por un proceso muy complejo, o por múltiples procesos), tiene permitido **asignar un espacio de la memoria secundaria** para su beneficio.

> Este mismo tema aparece en la sección 2 de este documento desde el lado del hardware, donde se le llama *archivo de paginación* y se presenta como un método económico para aumentar el tamaño de la memoria usando disco. Aquí se ve desde el software: quién crea la ilusión y cómo.

### Paginación

Si bien la memoria virtual es un concepto, la **paginación es la técnica** que utiliza para lograr lo que conocemos como memoria virtual.

El sistema operativo le da a cada programa o proceso un **"mapa de apodos"** o mapa virtual propio de la memoria, para hacerle creer que tiene todo el acceso a la memoria para él solo y de forma secuencial.

- El programa usa esos "apodos" para referirse a la memoria real, **sin saber ni cómo se llama de verdad ni dónde está ubicada físicamente**
- El sistema operativo solo interviene en la creación, la expansión o la resolución de problemas del mapa virtual

### La MMU

La **MMU** (unidad de gestión de memoria) lee esos "apodos" y los **traduce** para meter los datos en los espacios reales de la memoria principal. La escritura sucede directamente en el lugar físico de la memoria, sin un lugar intermedio donde se almacene el dato.

Es un componente de **hardware físico que existe dentro de la propia CPU**, pero que no forma parte de su esquema lógico.

Su razón de existir es **bajar la carga lógica del CPU**: miles de millones de entradas a la memoria le quitarían mucho tiempo y poder de procesamiento.

> Es el mismo argumento que justifica el DMA en la sección 3 de este documento: añadir un módulo dedicado para que el procesador no gaste instrucciones en trabajo repetitivo.

---

## 6. Gestión de procesos

*Fuente: [[Gestion de procesos]] — Sistemas Operativos, sem. 3*

Cómo el sistema operativo reparte el **tiempo de CPU** entre varias tareas. Es la continuación práctica de la multiprogramación que aparece como dato histórico en la sección 4 de este documento.

### Tiempo de CPU o ráfaga de CPU

Los sistemas con **multiprogramación** llevaron a que un CPU pudiera ejecutar varias tareas de manera simultánea, mediante un **cambio de contexto**. Las tareas comparten el procesador por *quantums* de tiempo.

#### Quantum de tiempo

La cantidad de milisegundos que un CPU puede dar a una tarea.

#### Cambio de contexto

El momento del cambio de una tarea a otra durante la multiprogramación con tiempo de CPU. Cuando vuelve a la misma tarea que dejó, la reinicia **desde el momento en que se quedó** la última vez.

### Paralelismo y concurrencia

| | Qué ocurre | Qué hace falta |
|---|---|---|
| **Paralelismo** | Dos o más procesos se ejecutan **exactamente al mismo tiempo** | Varios procesadores, o varios núcleos de un solo procesador |
| **Concurrencia** | Dos o más procesos se ejecutan **uno por uno**, pero con un cambio de contexto tan rápido y eficiente que da la **ilusión** de paralelismo | Un solo núcleo basta |

⚠️ Ambos términos quedaron marcados en clase como "buscar" — conviene contrastarlos con Tanenbaum antes del examen.

> La diferencia se apoya en hardware: el paralelismo real depende de que existan varios núcleos. Ver [[MOC - Estructura interna de un CPU]], sección 7.

---

## Relacionadas

- [[00 - Indice]] — el índice maestro con todos los hilos
- [[Definicion y funciones del sistema operativo]] — gestionar memoria, procesos y dispositivos son funciones del SO
- [[MOC - Estructura interna de un CPU]] — comparte la jerarquía de memoria, y su sección de multinúcleo es la condición de hardware del paralelismo de la sección 6
- [[Tipos de sistemas operativos]] — en qué desembocó la quinta generación: sistemas de servidor, escritorio y móviles
- [[Arquitectura de entrada y salida]] — el módulo de E/S sobre el que operan las tres técnicas de la sección 3
- [[Buses y estructuras de interconexion]] — el bus compartido cuya frecuencia obliga a que exista la caché
- [[Arreglos de discos RAID]] — el disco al fondo de la jerarquía, donde se apoya la memoria virtual
