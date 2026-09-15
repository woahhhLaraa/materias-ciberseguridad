---
materia: Sistemas Operativos
semestre: 3
tipo: referencia
tags: [sistemas-operativos, concurrencia, paralelismo, procesos, hilos, sincronizacion]
---

# Concurrencia y paralelismo

> Documento de investigacion externo, no apunte de clase: conserva su estructura original (TL;DR, Key Findings, Details, Recommendations, Caveats) y sus reservas sobre las fuentes.
> Material de apoyo del mismo tema: ![[Concurrencia y paralelismo.mp4]]


## TL;DR
- La concurrencia es la capacidad de un sistema operativo de gestionar múltiples tareas cuyos periodos de vida se solapan en el tiempo ("dealing with lots of things at once"), lo que NO exige ejecución física simultánea; el paralelismo ("doing lots of things at once") sí la exige y requiere hardware con varias unidades de proceso.
- El SO materializa la concurrencia mediante procesos e hilos, planificados por el scheduler mediante multiplexación de la CPU y cambio de contexto; cuando varias tareas comparten datos aparecen condiciones de carrera que se controlan protegiendo la sección crítica con exclusión mutua (semáforos, mutex, monitores, variables de condición, spinlocks, barreras).
- Los peligros clásicos son las condiciones de carrera, los deadlocks (las cuatro condiciones de Coffman), la inanición (starvation) y la inversión de prioridades; Linux (planificador EEVDF, futex, RCU) y Windows (planificador apropiativo de 32 niveles, SRW locks, secciones críticas) ilustran implementaciones modernas.

## Key Findings
1. **Concurrencia ≠ paralelismo.** Concurrencia es tener múltiples acciones "en progreso" a la vez (estructura lógica); paralelismo es ejecutarlas simultáneamente (mejora de rendimiento). Puede haber concurrencia sin paralelismo (un solo núcleo con time-sharing) y todo paralelismo implica concurrencia.
2. **La concurrencia aparente** se logra en un solo núcleo mediante multiprogramación: el SO conmuta rápidamente entre tareas creando la ilusión de simultaneidad. La **concurrencia real** requiere multiprocesadores/multi-core.
3. **Procesos vs. hilos:** los procesos tienen espacios de direcciones separados; los hilos comparten el espacio de direcciones del proceso, por lo que su cambio de contexto es más barato (no hay que invalidar la TLB) pero exigen sincronización cuidadosa.
4. **El problema de la sección crítica** requiere satisfacer tres condiciones (Silberschatz): exclusión mutua, progreso y espera acotada (bounded waiting).
5. **Deadlock** requiere las cuatro condiciones de Coffman (1971): exclusión mutua, retención y espera, no apropiación y espera circular. Romper una previene el deadlock.
6. **Herramientas de sincronización:** semáforos (Dijkstra, 1965), mutex, monitores, variables de condición, spinlocks y barreras, cada uno con compromisos distintos.
7. **Modelos de concurrencia:** multihilo con memoria compartida, multiproceso, basado en eventos (async), actores y CSP/corrutinas.

## Details

### 1. Definición: concurrencia frente a paralelismo
En el contexto de los sistemas operativos, un sistema es **concurrente** si puede soportar dos o más acciones *en progreso* al mismo tiempo, y **paralelo** si puede soportar dos o más acciones *ejecutándose simultáneamente*. La frase clave es "en progreso": en los sistemas concurrentes múltiples acciones pueden estar en progreso (pero no necesariamente ejecutándose) a la vez, mientras que en los sistemas paralelos varias se ejecutan de forma simultánea. La formulación más citada procede de la charla de Rob Pike "Concurrency is not Parallelism" (conferencia Waza de Heroku, 2012): *"Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once… Concurrency is about structure, parallelism is about execution."*

La distinción tiene consecuencias de diseño. La concurrencia se centra en la **estructura lógica** de las tareas: por ejemplo, un programa con interfaz gráfica crea hilos separados para gestionar el teclado, autoguardar copias y responder a clics. El paralelismo se centra en el **rendimiento** (throughput y latencia), dividiendo una tarea en subtareas que se ejecutan a la vez en varios núcleos. La concurrencia puede existir sin paralelismo (multiprogramación en un solo núcleo), pero todo paralelismo real presupone concurrencia.

Históricamente, la programación concurrente nació con los sistemas operativos de multiprogramación en los años 60; en 1965 Edsger Dijkstra introdujo los semáforos y el problema de los filósofos comensales.

### 2. Cómo funciona la concurrencia a nivel de SO

**Procesos e hilos.** El proceso es la unidad de abstracción fundamental: un programa en ejecución con su espacio de direcciones, y es la unidad "más pesada" de planificación del kernel, dueña de recursos (memoria, descriptores de archivo, sockets). Un **hilo** es una secuencia de control dentro de un proceso que ejecuta sus instrucciones de forma independiente. Los hilos de un mismo proceso comparten el espacio de direcciones y los recursos, pero cada uno mantiene su propio contexto de ejecución (registros, contador de programa, pila).

**Planificación (scheduling).** El planificador decide qué tarea ocupa la CPU. En sistemas de tiempo compartido cada hilo o proceso recibe un *quantum* (time slice) antes de que el planificador conmute al siguiente, garantizando un reparto equitativo. La planificación puede ser **apropiativa** (preemptive), donde un hilo de mayor prioridad interrumpe a uno de menor, o **no apropiativa**.

**Cambio de contexto (context switching).** Es la operación mediante la cual el SO conmuta la CPU de un hilo/proceso a otro: guarda el estado del actual (registros, contador de programa, puntero de pila) en su bloque de control de proceso (PCB) o de hilo (TCB) y restaura el del siguiente. La ilusión de concurrencia se logra mediante cambios de contexto que ocurren en rápida sucesión (decenas o cientos por segundo). Se dispara cuando: (a) expira el quantum, (b) un proceso pide E/S y se bloquea, (c) llega un proceso de mayor prioridad, o (d) ocurre una interrupción de hardware. El cambio de contexto tiene coste: ciclos de CPU para salvar/restaurar estado, y fallos de caché. El cambio entre hilos del mismo proceso es más barato que entre procesos, porque no se cambia el espacio de direcciones ni se invalida la TLB.

**Multiplexación de CPU.** En un núcleo único, el SO multiplexa la CPU en el tiempo (time-sharing): reparte el procesador entre los procesos intercalando su ejecución para dar apariencia de ejecución simultánea. En multiprocesadores/multi-core, distintos hilos se asignan a distintos núcleos para paralelismo real.

### 3. Problemas clásicos de la concurrencia

**Condición de carrera (race condition).** Ocurre cuando el comportamiento de un programa depende del orden temporal relativo de eventos (por ejemplo, el orden en que se planifican los hilos), y varios hilos acceden a datos compartidos, al menos uno modificándolos. El ejemplo canónico es el incremento `count++`: dos hilos leen el mismo valor, ambos lo incrementan y ambos escriben, perdiéndose una actualización. Análogamente, una transferencia bancaria concurrente puede dejar un saldo incorrecto.

**Sección crítica.** Es el segmento de código donde se accede a un recurso compartido y que no debe ser ejecutado por más de un proceso/hilo a la vez. Según Silberschatz (*Operating System Concepts*), una solución al problema de la sección crítica debe cumplir tres condiciones:
- **Exclusión mutua:** si un proceso ejecuta su sección crítica, ningún otro puede ejecutar la suya.
- **Progreso:** si ninguno está en la sección crítica, la decisión de quién entra no puede posponerse indefinidamente.
- **Espera acotada (bounded waiting):** existe un límite al número de veces que otros procesos entran antes de que a un proceso que ha solicitado entrar se le conceda; ningún proceso espera para siempre.

**Exclusión mutua.** Es la propiedad de control de concurrencia que evita las condiciones de carrera: un hilo nunca entra en su sección crítica mientras otro hilo concurrente ya está accediendo a ella.

**Deadlock (interbloqueo).** Un conjunto de procesos queda bloqueado porque cada uno espera un recurso retenido por otro, creando un ciclo. En su artículo fundacional "System Deadlocks" (Edward G. Coffman, Jr., Michael J. Elphick y Arie Shoshani, *ACM Computing Surveys* 3(2), junio de 1971, pp. 67–78) se formalizaron las cuatro condiciones necesarias y suficientes (condiciones de Coffman):
1. **Exclusión mutua:** al menos un recurso es no compartible.
2. **Retención y espera (hold and wait):** un proceso retiene recursos mientras espera otros.
3. **No apropiación (no preemption):** un recurso solo puede liberarlo voluntariamente el proceso que lo retiene.
4. **Espera circular (circular wait):** existe una cadena circular de procesos, cada uno esperando un recurso del siguiente.

El SO puede tratar el deadlock de cuatro formas: **prevención** (negar estructuralmente una condición), **evitación** (algoritmo del banquero, que solo concede recursos si el estado sigue siendo "seguro"), **detección y recuperación** (grafo de asignación de recursos + selección de víctima), e **ignorarlo** ("algoritmo del avestruz").

**Inanición (starvation).** Un proceso está listo pero nunca obtiene los recursos/CPU que necesita, posponiéndose indefinidamente. Suele deberse a planificación por prioridades donde procesos de alta prioridad monopolizan la CPU. Diferencia clave con el deadlock: el deadlock es espera infinita y circular; la inanición es "espera larga" y puede resolverse si cambian las condiciones (p. ej., mediante *aging*, que eleva progresivamente la prioridad de los procesos que esperan).

**Inversión de prioridades (priority inversion).** Una tarea de alta prioridad queda bloqueada indirectamente por una de prioridad media porque una de baja prioridad retiene un recurso compartido. El caso más famoso fue el **Mars Pathfinder** (1997). Según el relato autorizado de Glenn E. Reeves, líder del equipo de software del Pathfinder en el JPL ("What really happened on Mars?", 15 de diciembre de 1997): *"The higher priority bc_dist task was blocked by the much lower priority ASI/MET task. The solution was obvious: priority inheritance. The priority inheritance flag for the mutex was set to 'off' in VxWorks."* Los reinicios del sistema los detectaba un watchdog; el fallo se corrigió subiendo desde la Tierra un programa en C que cambió a "true" el flag de herencia de prioridad del mutex. El fundamento teórico es el protocolo de herencia de prioridad de Sha, Rajkumar y Lehoczky (1990); una alternativa es el protocolo de techo de prioridad (priority ceiling).

**Problemas clásicos de sincronización** (Dijkstra y sucesores), usados como *benchmarks*:
- **Productor-consumidor (buffer acotado):** productores y consumidores comparten un buffer finito; se resuelve con semáforos contadores `full` y `empty` más un mutex.
- **Lectores-escritores:** múltiples lectores pueden acceder a la vez, pero un escritor necesita acceso exclusivo.
- **Filósofos comensales (Dijkstra, 1965):** cinco filósofos y cinco tenedores; si todos toman su tenedor izquierdo a la vez, hay deadlock. Ilustra a la vez deadlock e inanición; una solución simple es limitar a cuatro comensales o imponer un orden de adquisición.

### 4. Herramientas y mecanismos de sincronización

- **Semáforo (Dijkstra, 1965):** entero con dos operaciones atómicas: `P`/`wait`/`down` (proberen, decrementar) y `V`/`signal`/`up` (verhogen, incrementar). Un **semáforo binario** (máximo valor 1) se usa como mutex; un **semáforo contador** controla el acceso a N instancias de un recurso. Sirve tanto para exclusión mutua como para señalización/sincronización entre tareas. Su debilidad: no encapsula bien (es fácil introducir errores de orden que causan deadlock) y no soporta difusión (broadcast) a múltiples hilos.
- **Mutex (mutual exclusion lock):** primitiva de bloqueo con operaciones `lock`/`unlock` para proteger secciones críticas arbitrarias. A diferencia del semáforo, típicamente solo el hilo que adquirió el mutex puede liberarlo. Es más claro y menos propenso a errores que el semáforo para exclusión mutua.
- **Monitor:** construcción de alto nivel que combina un mutex y una o varias variables de condición, encapsulando los datos compartidos y garantizando que las operaciones se ejecuten atómicamente. Un monitor puede verse como un superconjunto del mutex; es más seguro porque el bloqueo y la señalización están integrados. Lenguajes como Java (`synchronized`) lo implementan de forma nativa.
- **Variable de condición:** permite a un hilo dormir hasta que un predicado se cumpla, sin espera activa, liberando atómicamente el mutex asociado. La operación `wait` (p. ej. `pthread_cond_wait`) libera el mutex, bloquea, y al ser despertado vuelve a adquirir el mutex atómicamente. Soporta `signal` (despertar uno) y `broadcast` (despertar a todos), superando la limitación de los semáforos.
- **Spinlock:** cerrojo de espera activa (busy-wait): el hilo comprueba repetidamente el cerrojo en un bucle hasta adquirirlo, consumiendo CPU. Es eficiente solo cuando el cerrojo se retiene muy poco tiempo y el coste de dormir/despertar sería mayor; es indispensable en contextos donde no se puede dormir (manejadores de interrupción).
- **Barrera:** punto de sincronización donde varios hilos deben esperar hasta que todos lleguen antes de continuar; muy usada en computación paralela (p. ej. OpenMP) para separar fases de cómputo.

Compromiso general: los mutex y las variables de condición **bloquean** (duermen) al hilo que espera, cediendo la CPU; los spinlocks **giran** (busy-wait), gastando ciclos pero evitando el coste de un cambio de contexto. Los mutex por sí solos no bastan para todos los problemas (p. ej. productor-consumidor), de ahí los semáforos, monitores y barreras.

### 5. Tipos y modelos de concurrencia

**Por unidad de ejecución:**
- **Concurrencia a nivel de procesos:** cada tarea es un proceso con su propio espacio de direcciones; mayor aislamiento y robustez (un fallo no corrompe a otros procesos), pero comunicación más costosa (IPC) y cambio de contexto más caro (invalidación de TLB, remapeo de memoria virtual). Un proceso puede consumir un orden de magnitud más de memoria que un hilo.
- **Concurrencia a nivel de hilos:** los hilos comparten memoria dentro de un proceso; comunicación barata y cambio de contexto ligero, pero exige sincronización cuidadosa (thread safety) porque un hilo con un fallo puede corromper el espacio del proceso entero.

**Real vs. aparente:**
- **Concurrencia real (multiprocesador/multi-core):** varias tareas se ejecutan físicamente a la vez, cada una en un núcleo/procesador.
- **Concurrencia aparente / pseudo-concurrencia (time-sharing en un solo núcleo):** el SO conmuta rápidamente entre tareas creando la ilusión de simultaneidad; en cualquier instante solo una tarea está realmente ejecutándose.

**Modelos de programación concurrente:**
- **Multihilo con memoria compartida:** hilos que comparten memoria y se coordinan con locks/semáforos; aprovecha múltiples núcleos, pero es propenso a race conditions y deadlocks (Java, C++, pthreads).
- **Multiproceso:** procesos aislados que se comunican por IPC; más robusto, más pesado.
- **Basado en eventos / asíncrono (event loop):** un bucle de eventos de un solo hilo procesa una cola de eventos ejecutando callbacks cuando completan operaciones de E/S; muy eficiente en memoria para cargas intensivas en E/S y elimina muchas race conditions al ser monohilo, pero el trabajo intensivo en CPU bloquea el bucle. Se apoya en facilidades del SO como `epoll` (Linux), `kqueue` (BSD) e IOCP (Windows). Ejemplos: Node.js, asyncio de Python.
- **Modelo de actores (Hewitt, 1973):** cada actor es un proceso ligero con estado privado y un buzón (mailbox); los actores se comunican solo por mensajes asíncronos, sin memoria compartida. El estado nunca se comparte, lo que elimina las race conditions de memoria compartida. Implementado en Erlang y Akka (Scala/JVM).
- **CSP (Communicating Sequential Processes, Hoare, 1978) y corrutinas:** procesos que se comunican por **canales** en lugar de memoria compartida; los canales pueden ser síncronos o asíncronos. Es el modelo de las goroutines y canales de Go. Las corrutinas (async/await) permiten multiplexar muchas tareas ligeras sobre pocos hilos del SO.

Estos modelos no son excluyentes: Go combina canales estilo CSP con goroutines que internamente usan varios hilos del SO; Rust soporta tanto hilos POSIX con memoria compartida como programación asíncrona.

**Mapeo de hilos usuario→kernel:** modelo 1:1 (cada hilo de usuario mapea a un hilo del kernel, planificados independientemente), N:1 (muchos hilos de usuario sobre un hilo del kernel, planificados en espacio de usuario) y M:N (muchos hilos de usuario sobre un pool de hilos del kernel).

### 6. Implementación en sistemas operativos modernos

**Linux.**
- *Planificación:* durante años el planificador por defecto de la clase `SCHED_NORMAL` fue el **Completely Fair Scheduler (CFS)**, incorporado en el kernel 2.6.23 (octubre de 2007) por Ingo Molnár. CFS abandona los quanta fijos y las prioridades explícitas: reparte la CPU de forma justa mediante el **virtual runtime (vruntime)**, y usa un árbol rojo-negro para elegir siempre la tarea con menor vruntime (la más "hambrienta" de CPU). Según Kernel Newbies, *"Linux 6.6 has been released on Sunday, 29 Oct 2023 […] it is replaced by code that uses a new algorithm, called EEVDF"*: a partir del kernel **6.6 (29 de octubre de 2023)**, CFS fue reemplazado por **EEVDF (Earliest Eligible Virtual Deadline First)**. EEVDF fue implementado en Linux por Peter Zijlstra (Intel) —serie de parches publicada en lore.kernel.org en mayo de 2023— y se basa en el informe técnico de 1995 "Earliest Eligible Virtual Deadline First: A Flexible and Accurate Mechanism for Proportional Share Resource Allocation" de Ion Stoica y Hussein Abdel-Wahab (College of William & Mary). EEVDF calcula el "lag" (diferencia entre el tiempo virtual que le corresponde a una tarea y el que realmente ha consumido): una tarea es **elegible** solo si su lag ≥ 0, y entre las elegibles se ejecuta la de **plazo virtual (virtual deadline)** más temprano. Las tareas real-time usan las políticas `SCHED_FIFO`/`SCHED_RR`.
- *Sincronización en espacio de usuario:* el **futex** ("Fast Userspace Mutex"), propuesto por contribuidores de IBM en 2002 e integrado en el kernel 2.6.0 (diciembre de 2003), es el bloque de construcción de las primitivas de alto nivel (`pthread_mutex_t`, `pthread_cond_t`, semáforos POSIX, `std::mutex`). Su clave: en el caso sin contención, la operación de lock/unlock se resuelve enteramente en espacio de usuario con instrucciones atómicas (un CAS), y solo se llama al kernel (operaciones `FUTEX_WAIT`/`FUTEX_WAKE`) cuando hay contención, para dormir/despertar hilos.
- *Sincronización en el kernel:* **spinlocks** (`spinlock_t`, definido en `include/linux/spinlock.h`) para secciones cortas donde no se puede dormir (contexto de interrupción); son cerrojos de un solo poseedor que giran hasta adquirirse. Según la documentación del kernel (*Unreliable Guide To Locking*, docs.kernel.org), en kernels compilados sin `CONFIG_SMP` pero con `CONFIG_PREEMPT` "los spinlocks simplemente desactivan la apropiación", y sin ambos "los spinlocks no existen en absoluto". El **mutex del kernel** (`struct mutex`, introducido en 2006 por Ingo Molnár, definido en `include/linux/mutex.h`) es un cerrojo durmiente que además hace *optimistic spinning* (busca el equilibrio entre girar unos ciclos y dormir). Los **semáforos** del kernel (`struct semaphore`) son cerrojos durmientes que, a diferencia del mutex, pueden usarse desde contexto de interrupción y ser liberados por una tarea distinta; hoy se prefieren mutex y completions (Robert Love, *Linux Kernel Development*). **RCU (Read-Copy-Update)**, añadido en octubre de 2002 y desarrollado por Paul E. McKenney (IBM Linux Technology Center, con Jonathan Walpole de Portland State University), está optimizado para datos de lectura mayoritaria: los lectores se ejecutan concurrentemente con los actualizadores sin adquirir cerrojos, sin instrucciones atómicas y (salvo en Alpha) sin barreras de memoria.

**Windows.**
- *Planificación:* usa un planificador **apropiativo dirigido por prioridades** con un esquema de **32 niveles**. Según Microsoft Learn (Win32, "Scheduling Priorities"): *"The priority levels range from zero (lowest priority) to 31 (highest priority). Only the zero-page thread can have a priority of zero."* La clase variable/dinámica (1–15) es para hilos de aplicaciones y sistema, y la clase de tiempo real (16–31) tiene prioridades fijas; el nivel 0 lo usa el hilo de página cero (gestión de memoria). El hilo listo de mayor prioridad siempre obtiene la CPU, apropiándose de uno de menor prioridad; los hilos de igual prioridad se despachan en round-robin. Windows aplica *boosts* temporales de prioridad tras completar E/S, recibir entrada de usuario o sufrir inanición, pero —como precisa Microsoft Learn en "Priority Boosts"— *"the system does not boost the priority of threads with a base priority level between 16 and 31. Only threads with a base priority between 0 and 15 receive dynamic priority boosts."*
- *Sincronización:* objetos del kernel "pesados" (Mutex, Event, Semaphore, WaitableTimer) que devuelven un HANDLE y sirven entre procesos, pero implican una transición a modo kernel (más lentos). Primitivas ligeras en modo usuario: la **sección crítica (CRITICAL_SECTION)**, que evita la llamada al sistema en el caso sin contención, y el **SRW lock (Slim Reader/Writer, desde Windows Vista)**, que distingue lectores compartidos de escritores exclusivos, se implementa mayormente en modo usuario y solo cae al kernel bajo contención. Windows 8 introdujo `WaitOnAddress`, funcionalmente similar al futex de Linux.

### 7. Ventajas y desafíos de la programación concurrente

**Ventajas:**
- **Aprovechamiento del hardware multi-core:** el paralelismo reduce el tiempo de ejecución (throughput y latencia).
- **Capacidad de respuesta (responsiveness):** una interfaz sigue reaccionando mientras hilos en segundo plano hacen trabajo pesado o E/S.
- **Mejor utilización de recursos:** mientras una tarea se bloquea en E/S, el SO planifica otra, evitando ciclos de CPU desperdiciados.
- **Estructuración modular:** aplicaciones y el propio SO pueden estructurarse como conjuntos de procesos/hilos cooperantes.
- **Escalabilidad:** servidores que atienden miles de conexiones concurrentes.

**Desafíos:**
- **No determinismo:** el resultado puede depender del orden de planificación, dificultando la reproducción y las pruebas de errores.
- **Race conditions, deadlocks, inanición e inversión de prioridades:** requieren sincronización correcta, difícil de razonar.
- **Coste de la sincronización:** los cerrojos serializan el acceso e introducen contención y sobrecarga; el propio cambio de contexto tiene coste.
- **Límite teórico de la aceleración (Ley de Amdahl):** la parte secuencial de un programa acota la mejora máxima obtenible al paralelizar. Si la fracción secuencial es F, la aceleración máxima con P procesadores es 1/(F+(1−F)/P); p. ej., si el 90 % es paralelizable, con 5 procesadores el máximo es ~3,6×. Añadir hilos indiscriminadamente no siempre acelera.
- **Depuración compleja:** los bugs de concurrencia (Heisenbugs) aparecen de forma intermitente; se usan herramientas como ThreadSanitizer o Valgrind.

## Recommendations
1. **Para el estudio:** dominar primero la tríada exclusión mutua / progreso / espera acotada y las cuatro condiciones de Coffman antes de pasar a las primitivas concretas; son el marco conceptual que estructura todo lo demás.
2. **Al elegir mecanismo de sincronización:** usar el constructo de mayor nivel disponible (monitor / variable de condición) frente a las primitivas de bajo nivel (semáforos), porque reducen los errores de orden; reservar los spinlocks para secciones críticas muy cortas y contextos que no pueden dormir.
3. **Al elegir modelo de concurrencia:** para E/S intensiva, preferir el modelo basado en eventos/async o actores (evitan gran parte de las race conditions); para cómputo intensivo en CPU, el multihilo con memoria compartida sobre múltiples núcleos; medir con la Ley de Amdahl antes de añadir hilos.
4. **Para ciberseguridad específicamente:** prestar atención a las race conditions de tipo **TOCTOU (time-of-check to time-of-use)**, una clase de vulnerabilidad derivada directamente de la concurrencia; y comprender que las primitivas de sincronización mal usadas son fuente de fallos de disponibilidad (deadlocks/DoS).
5. **Umbral de decisión:** si el perfilado muestra que la contención de cerrojos o el cambio de contexto domina el tiempo de ejecución, reconsiderar el modelo (p. ej., pasar de locks a estructuras lock-free/RCU o a paso de mensajes) antes de añadir más hilos.

## Caveats
- Muchas fuentes secundarias (blogs, Medium) coinciden con los libros de texto, pero para afirmaciones precisas conviene citar Silberschatz *Operating System Concepts*, Tanenbaum *Modern Operating Systems*, o Robert Love *Linux Kernel Development*, y la documentación oficial (kernel.org, Microsoft Learn).
- Sobre EEVDF hay una ligera discrepancia de matiz entre fuentes: la documentación del kernel describe la transición en 6.6 "como nueva opción en 2024", mientras que Kernel Newbies, Wikipedia y la prensa técnica afirman que reemplazó a CFS en 6.6 (29 de octubre de 2023), con estabilización hasta 6.8 (marzo de 2024). El consenso: la fusión inicial ocurrió en 6.6.
- Las cifras de coste de cambio de contexto y de memoria por proceso/hilo varían mucho según hardware y SO; deben tomarse como órdenes de magnitud, no valores exactos.
- El detalle exacto de las primitivas de Windows y del planificador puede variar entre versiones (NT, XP, Vista, 10, 11); las fuentes reflejan un modelo general estable pero no cada build.

## Relacionadas

- [[Gestion de procesos]] — los procesos e hilos que aqui se planifican, vistos desde los apuntes de clase
- [[Gestion de memoria]] — el espacio de direcciones que los hilos comparten y los procesos no
- [[Tipos de sistemas operativos]] — el tiempo compartido y el multiprocesamiento que hacen posible la concurrencia
- [[Capas de un sistema operativo]] — donde vive el planificador dentro del kernel
- [[Sistemas Operativos (materia)]] — indice de la materia
- [[Teoria de grafos]] — el grafo de asignacion de recursos con que se detecta el deadlock es un grafo dirigido
- [[Riesgo amenaza y vulnerabilidad]] — las race conditions TOCTOU como clase de vulnerabilidad nacida de la concurrencia
