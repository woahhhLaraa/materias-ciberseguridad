---
materia: Introduccion a las redes de computo
semestre: 2
tipo: concepto
tags: [redes, protocolos, modelos]
modulo: 3
---

# Protocolos y modelos

> Módulo 3 — clase del 25/03/2026

## Qué es un protocolo

Los protocolos son los **"idiomas"** que hablan los dispositivos en común para comunicarse entre ellos. El reglamento.

En todo sistema de comunicación hay: **remitente**, **receptor** y **medio/canal**.

## Qué define un conjunto de reglas

- Un emisor y un receptor
- Idioma y gramática comunes
- Velocidad y momento de entrega
- Requisitos de confirmación o acuse de recibo

## Requisitos de los protocolos informáticos

- Codificación de los mensajes
- Formato y encapsulamiento del mensaje
- Tamaño del mensaje
- Sincronización del mensaje
- Opciones de entrega del mensaje

### Sincronización (*timing*)

Incluye control de flujo, tiempo de espera de respuesta y método de acceso.

### Opciones de entrega

| Opción | Alcance |
|---|---|
| **Unidifusión** (unicast) | Uno a uno |
| **Multidifusión** (multicast) | Uno a muchos |
| **Difusión** (broadcast) | Uno a todos |

> ⚠️ Nota: el **broadcast** se utiliza en redes IPv4, pero **no existe en IPv6**. IPv6 añade en cambio **anycast** como opción de entrega adicional. Ver [[Capa de red - IPv4 e IPv6]].

## Protocolos en detalle

A nivel de redes definen un conjunto común de reglas, implementadas en dispositivos tanto en software como en hardware. Cada uno tiene sus propias funciones, formatos y mediciones.

Cada protocolo trabaja en diferentes capas. Ejemplos: **HTTP** (transferencia de hipertexto), **TCP** (control de transmisión), **IP** (protocolo de internet).

## Suites de protocolos

Un grupo de protocolos que se relacionan entre sí para lograr la comunicación. Se organizan siempre en **capas**, superiores e inferiores:

1. Capa de **aplicación**
2. Capa de **transporte**
3. Capa de **internet**
4. Capa de **acceso a la red**

Este es el modelo **TCP/IP** de cuatro capas.

## Relacionadas

- [[Capa de red - IPv4 e IPv6]] — la capa 3 en detalle: el ejemplo concreto de todo lo que aquí se define en abstracto
- [[CSMA-CD y colisiones]] — un protocolo de acceso al medio concreto
