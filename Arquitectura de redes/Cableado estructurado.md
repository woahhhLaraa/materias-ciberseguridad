---
materia: Arquitectura de redes
semestre: 2
tipo: concepto
tags: [redes, cableado, capa-fisica]
---

# Cableado estructurado

> Clase del 11/03/2026

## Características

- **Capacidad** — permite transmitir información de múltiples tecnologías
- **Diseño** — óptimo para el trabajo, al mínimo costo posible
- **Administración**
- **Modularidad**
- **Compatibilidad**

## Conceptos básicos

| Término | Qué es |
|---|---|
| **Patch cord** | Cable de terminal |
| **Placa de servicios** | Salida en pared |
| **Cableado oculto** | El que va por dentro de muros o techos |
| **HUB** | Concentrador |
| **Panel de parcheo** | Punto de conexión organizado |
| **Rack** | Gabinete de equipos |
| **Conector de cruce** | Cross-connect |
| **Canaleta** | Contenedor del cable |
| **LAN tester** | Herramienta de verificación |

## Elementos de un cableado

- Área de trabajo
- Clóset de comunicaciones
- Cableado horizontal
- Cuarto de entrada de servicios
- Cuarto de equipo
- Cableado vertebral o **backbone**

## Cableado horizontal

Se llama así porque se instala en el piso o el techo por medio de contenedores.

- Contiene **más cable** que el backbone
- Topología en **estrella**
- Incluye las salidas de telecomunicaciones en el área de trabajo
- ⭐ **Distancia máxima: 90 metros** desde el área de trabajo hasta el clóset de comunicaciones

> Los 90 m no son arbitrarios: el límite físico del cobre es de 100 m ([[Medios de red]]), y se reservan 10 m para los patch cords en ambos extremos.

### Tipos de cable aceptados

- Par trenzado de cuatro pares **sin** blindaje (UTP)
- Par trenzado de dos pares **con** blindaje (STP)

## Relacionadas

- [[Medios de red]] — de dónde sale el límite de 100 m del cobre que aquí se recorta a 90
- [[Diseno de red LAN]] — los pasos de ubicación y selección de hardware donde este cableado se planifica
