---
materia: Sistemas Operativos
semestre: 3
tipo: concepto
tags:
  - sistemas-operativos
  - arquitectura
  - kernel
  - subsistemas
sr-due: 2026-09-03
sr-interval: 3
sr-ease: 250
---
#review
# Capas de un sistema operativo

Un sistema operativo es en realidad un conjunto de capas que funcionan al unísono. Podemos reducir esas capas en **ocho subsistemas**.

## Kernel o núcleo

El corazón del sistema. Dependiendo de la arquitectura (monolítico o microkernel), el resto de las capas puede construirse sobre el kernel o vivir dentro de él — ver la clasificación completa en [[Tipos de sistemas operativos]].

## Subsistema de entrada y salida

Ver [[Dispositivos de entrada y salida]].

No solo corresponde a los periféricos, sino también a tarjetas gráficas, de red y dispositivos de almacenamiento secundario — nótese que el almacenamiento principal no forma parte de esta sección, ni el CPU. Básicamente, cualquier cosa que permita a la PC comunicarse con el exterior o con el usuario.

La **BIOS** (*Basic Input Output System*), integrada directamente en la tarjeta madre, es una herramienta de firmware que usa el CPU para inicializar la comunicación y el diagnóstico de los sistemas de entrada y salida. Antes de que el sistema operativo arranque por completo, la BIOS corre un test de integridad tanto en el propio CPU como en los sistemas básicos de RAM y GPU. Luego usa drivers genéricos básicos para controlar la pantalla y leer el teclado (en las BIOS más modernas, también el mouse), busca en el almacenamiento secundario alguna unidad de arranque de un sistema operativo y la carga.

A partir de ahí, el sistema operativo toma el control de los dispositivos de entrada y salida con sus propios drivers (o los cargados por el usuario), coordinando todo sin que el usuario tenga que lidiar con los programas particulares de cada hardware.

## Subsistema de gestión de procesos

Ver [[Gestion de procesos]].

La capa del sistema que gestiona cómo interactúa cada proceso, ya sea con otros procesos o de forma solitaria:

- Inicializa, pausa, reanuda y cierra procesos
- Comunicación y sincronización de procesos: *pipelines*, paso de mensajes, memoria compartida, sockets
- Gestiona la situación de interbloqueo (*deadlock*)
- Asigna el tiempo de CPU o ráfaga de CPU a cada proceso
- Aquí viven la multiprogramación, el paralelismo y la concurrencia
- Mecanismos de seguridad para no matar procesos críticos
- Planificación de uso de CPU, mediante el planificador de CPU

## Subsistema de gestión de memoria

Ver [[Gestion de memoria]].

Orquesta el recurso de la memoria entre los distintos procesos del sistema, ya que la memoria es un recurso compartido y **limitado**. Su componente de hardware es la **MMU**.

- Asignar y limpiar espacios de memoria
- Manejar la memoria virtual
- Saber quién usa la memoria en cada momento
- Proteger la memoria de accesos no autorizados (accidentales o no) por parte de un proceso
- Planificación de acceso a memoria

## Administración de almacenamiento secundario

Encargada de manejar cómo los procesos escriben datos en memoria persistente — quién, cuándo, cómo y dónde —, protegiendo igualmente contra accesos no autorizados. Gestiona las solicitudes de acceso.

- Decidir quién y cuándo puede acceder a leer o escribir en almacenamiento secundario
- Administrar el espacio libre y ocupado
- Mecanismos de seguridad
- Planificación de disco para atender las solicitudes

## Subsistema de archivos

Para que el usuario se pueda mover por el almacenamiento secundario de forma fluida y amigable, se ideó un sistema de archivos, donde cada archivo o dato se encuentra en un lugar específico (ruta o dirección) dentro de un explorador de archivos. Protege ciertos archivos (en Windows, los más críticos para el funcionamiento del sistema) y gestiona las solicitudes de acceso.

- Crear y eliminar archivos
- Leer y modificar archivos
- Administrar directorios
- Búsqueda de archivos

| Sistema de archivos | Desde | Journaling | Tamaño máximo |
|---|---|---|---|
| **NTFS** (*New Technology File System*) | Windows XP | Sí | 16 TB por archivo o disco (teórico hasta 8 PB bien configurado) |
| **FAT32** | Años 90, legacy | No | 4 GB por archivo; hasta 32 GB de volumen (teórico 2 TB) |
| **ext4** | — (el más usado en distribuciones Linux) | Sí, más complejo que NTFS | 16 TB por archivo (teórico de miles de TB) |

## Subsistema de gestión de redes y comunicaciones

Encargado de que la computadora se comunique con otras computadoras, en la misma red o en una red distinta. Su componente de hardware es la tarjeta de red.

- Protocolos TCP/IP
- Protección en las comunicaciones
- Enviar y recibir paquetes de datos
- Administrar interfaces de red (tarjeta de red)
- Gestionar conexiones de red

## Subsistema de interfaz de usuario

Encargado de manejar la GUI o la CLI, funcionando como puente entre el SO y el usuario y manteniendo un lenguaje comprensible para los humanos.

- Recibir input del usuario
- Dar output sobre lo que sucede dentro de la computadora
- Gestionar ventanas e interfaces gráficas
- Facilitar el uso de los servicios y subsistemas anteriores
- Proporcionar notificaciones y gestionar la comunicación de errores

## Relacionadas

- [[Definicion y funciones del sistema operativo]] — estas ocho capas son el detalle de las funciones esenciales listadas ahí
- [[Dispositivos de entrada y salida]] — desarrolla el subsistema de entrada y salida
- [[Gestion de procesos]] — desarrolla el subsistema de gestión de procesos
- [[Gestion de memoria]] — desarrolla el subsistema de gestión de memoria
- [[Tipos de sistemas operativos]] — la clasificación monolítico/microkernel/híbrido que decide cómo se organizan estas capas dentro del kernel
