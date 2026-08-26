---
materia: Organizacion de computadoras
semestre: 1
tipo: referencia
tags: [hardware, puertos, conectores]
---

# Puertos y conectores

Referencia de los componentes de interconexión vistos en clase.

## Buses de expansión

### PCI
Bus de interconexión que permite conectar tarjetas de expansión (video, sonido, red). Es una ranura física.
- Velocidad de transferencia: 125 MB/s a 503 MB/s
- Usa la función **bus master**: permite a dispositivos externos saltarse el procesador y acceder directamente
- Viene en varios tamaños

### PCI-X
Versión mejorada del PCI tradicional, con bus de **64 bits**, para servidores. Bus compartido; tiende a ser físicamente más grande.

### PCIe (PCI Express)
Bus de expansión de alta velocidad. **Es el estándar actual.**
- Conecta los componentes más importantes con la placa o el procesador
- Cada dispositivo tiene su **propia conexión directa** con el procesador
- Usa **lanes**: carriles privados y bidireccionales entre la ranura y el procesador

> La diferencia conceptual entre PCI y PCIe: PCI es un bus **compartido**, PCIe son enlaces **punto a punto**. Por eso PCIe escala y PCI no.

## Almacenamiento

### SATA — Serial Advanced Technology Attachment
- Conector de bus para transferencia de datos
- Usado en HDD, SSD y unidades ópticas
- Creado en 2001, para reemplazar a su antecesor **PATA**
- Requiere un cable de alimentación y uno de datos

| Versión | Año | Velocidad | Frecuencia |
|---|---|---|---|
| SATA 1.0 | 2003 | 150 MB/s | 1500 MHz |
| SATA 2.0 | 2004 | 300 MB/s | 3000 MHz |
| SATA 3.0 | 2008 | 600 MB/s | 6000 MHz |

Variantes: **SATA 3.1 / mSATA** (portátiles), **eSATA** (dispositivos externos), **eSATAp** (no requiere cable de poder, compatible con USB), **SATA Express** (velocidades de 1 GB/s; usa 2 puertos SATA más uno extra para señales de sincronización).

### M.2 — Next Generation Form Factor
- Creado en 2012, estandarizado en 2013
- Pensado para reemplazar a SATA
- Más compacto que SATA
- Utiliza el bus **PCIe**
- Velocidad teórica de 20 Gbps; en la práctica ~4 GB/s

## Periféricos

### USB — Universal Serial Bus
Objetivo: unificar y simplificar las conexiones entre equipos y periféricos. Creado en **1996**, primera versión de 12 Mbps. También se usa como fuente de energía.

| Versión | Año |
|---|---|
| USB 1.1 | 1998 |
| USB 2.0 | 2000 |
| USB 3.0 | 2008 |
| USB 3.1 | 2013 |
| USB 3.2 | 2017 |
| USB 4 | 2019 |

### Thunderbolt
- Creado en 2009, lanzado para MacBooks
- Velocidades de más de 100 Gbps
- Usado para edición de video y 3D, 4K y 8K directamente desde SSD, RAID o NAS
- Permite **estación de acoplamiento**: conectar un portátil a todos los periféricos con un solo cable
- Aumenta la capacidad de laptops delgadas para machine learning, renders o simulación

### FireWire (IEEE 1394)
- Diseñado por Apple en 1986
- Técnicamente superior al USB 1.0
- **Obsoleto**: desapareció por alto costo, baja adopción, licencias y falta de compatibilidad
- Velocidad máxima 3.2 Gbps (400 MB/s); conector tipo Ethernet
- Usos: video digital, interfaces de audio profesional, conexión directa entre computadoras

> FireWire es el caso de estudio de que el mejor estándar técnico no gana: perdió contra USB por licenciamiento y ecosistema, no por rendimiento.

## Video

### VGA — Video Graphics Array
- Creado en 1987 por IBM, como estándar de visualización para su línea de computadoras
- Resolución de 320×200 o 640×480, 16 colores
- Frecuencia de 60 Hz
- **Analógico**

Versiones: VGA (640×480), SVGA (800×600), XGA (1024 a 1600), Mini VGA (misma señal, conector más pequeño, laptops antiguas).

### DVI — Digital Visual Interface
- Creado en 1999 para superar la limitación de VGA, que solo transmitía señales analógicas
- Estándar en monitores LCD entre 2000 y 2010; reemplazado por HDMI y DisplayPort a partir de 2010
- Video de alta resolución hasta 2560×1600
- Compatibilidad analógica y digital
- Transferencia máxima de 7.92 Gbps

### HDMI
- Creado en 2002 por Sony, Panasonic y Toshiba, para reemplazar cables analógicos
- Transmite **audio y video en un solo cable**, sin pérdida de calidad

| Versión | Año | Soporte |
|---|---|---|
| HDMI 1.0 | 2002 | 1080p |
| HDMI 1.4 | 2009 | 3D y 4K a 30 Hz |
| HDMI 2.0 | — | 4K a 60 Hz y HDR |
| HDMI 2.1 | — | 4K a 120 Hz, 8K a 60 Hz |

Conectores: **tipo A** (el común), **tipo C** (mini), **tipo D** (micro), **tipo E** (automotriz).

## Relacionadas

- [[Buses y estructuras de interconexion]] — qué es un bus y por qué PCIe da un carril privado en vez de compartir el medio
- [[Arquitectura de entrada y salida]] — el módulo de E/S que hay detrás de cada uno de estos conectores
