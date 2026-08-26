---
materia: Arquitectura de redes
semestre: 2
tipo: concepto
tags: [redes, topologia, clasificacion]
---

# Clasificación de redes

> Fundamentos de arquitecturas de redes

Las redes se clasifican por tamaño, alcance y dimensiones.

## Por alcance geográfico

| Sigla | Nombre | Alcance |
|---|---|---|
| **PAN** | Personal Area Network | Personal |
| **LAN** | Local Area Network | Local |
| **MAN** | Metropolitan Area Network | Metropolitana |
| **WAN** | Wide Area Network | Área amplia |
| **GAN** | Global Area Network | Global |

## Por topología

La **topología de red** establece la forma de la red en cuanto a **conectividad física**.

Su objetivo es la **fiabilidad del tráfico** para el envío correcto de datos.

Formalmente, una topología es un grafo — ver [[Teoria de grafos]].

## Por protocolo de comunicación

Dos familias:

| Familia | Ejemplos |
|---|---|
| **Sistemas con escucha** | Redes Ethernet — ver [[CSMA-CD y colisiones]] |
| **Paso de testigo** | Redes Token Ring, Token Bus — ver [[Token Ring]] |

La diferencia de fondo: en los sistemas con escucha cualquiera puede hablar cuando cree que hay silencio (y a veces chocan); en el paso de testigo solo habla quien tiene el testigo (y nunca chocan).

## Relacionadas

- [[Componentes de red]] — los dispositivos concretos que estas redes conectan
- [[Diseno de red LAN]] — la clasificación aplicada: determinar la topología es parte del paso 2
