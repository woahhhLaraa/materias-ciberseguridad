---
materia: Introduccion a las redes de computo
semestre: 2
tipo: concepto
tags: [redes, capa-fisica, medios]
---

# Medios de red

Toda comunicación se hace a través de un **medio**, que permite que un mensaje viaje desde el origen hacia el destino.

## Medios guiados

Físicos, se pueden tocar:
- Cable coaxial
- **UTP** (par trenzado sin blindar)
- Fibra óptica / fibra de vidrio

## Medios no guiados

No los podemos ver. Transmisión inalámbrica mediante modulación de frecuencias específicas de ondas electromagnéticas.

## Límites de distancia

Dato clave del curso:

| Medio | Alcance antes de atenuación |
|---|---|
| Cable de cobre | **100 metros** |
| Fibra óptica | **Varios kilómetros** |

Este límite de 100 m es el que determina la distancia máxima del cableado horizontal en el diseño de instalaciones. Ver [[Cableado estructurado]], donde el máximo se fija en 90 m precisamente para dejar margen.

## Términos importantes

- **NIC** (tarjeta de interfaz de red) — la tarjeta que tiene toda computadora que se conecta a la red. Existe alámbrica e inalámbrica.
- **Puerto físico** — clásicamente el puerto Ethernet, conector **RJ-45**
- **Interfaz**

## Relacionadas

- [[Componentes de red]] — los dispositivos que estos medios conectan
- [[Cableado estructurado]] — donde el límite de 100 m se vuelve norma: 90 m de cableado horizontal para dejar margen
- [[Representaciones de red y topologias]] — los medios son las aristas del diagrama; los dispositivos, los vértices
