---
materia: Introduccion a las redes de computo
semestre: 2
tipo: concepto
tags: [redes, confiabilidad, qos]
---

# Redes confiables

> Clase del 02/03/26

Cuatro características que debe cumplir una red para considerarse confiable.

## 1. Tolerancia a fallas

Disminuir el impacto de una falla limitando la cantidad de dispositivos afectados. Se logra proporcionando **redundancia** mediante una red de **paquetes conmutados**.

- La conmutación por paquetes divide el tráfico en paquetes que se enrutan a través de la red
- En teoría, **cada paquete puede tomar una ruta diferente** hacia el destino

Esa es exactamente la propiedad que da la tolerancia: si un enlace cae, los paquetes siguientes rodean.

## 2. Escalabilidad

Una red escalable puede expandirse fácil y rápidamente para admitir usuarios y aplicaciones nuevas **sin replantear toda la red** y sin afectar la arquitectura existente.

## 3. Calidad de servicio (QoS)

El principal mecanismo para garantizar la entrega confiable de contenido a todos los usuarios. Con QoS implementada, un router puede administrar más fácilmente el flujo de tráfico de voz, datos o video.

Es la respuesta al problema de la [[Tecnologias de acceso a internet|red convergente]].

## 4. Seguridad

- Implementación de firewalls
- Impedir el acceso incluso dentro de la misma LAN para diferentes usuarios
- Seguridad de la infraestructura
- Seguridad física de los dispositivos
- Se busca implementar la [[Triada CIA]]: confidencialidad, integridad y disponibilidad

## Nota de conexión

Las cuatro características se enfrentan entre sí en el diseño real: la redundancia cuesta dinero, la seguridad cuesta latencia, y QoS cuesta complejidad de configuración. La metodología [[Metodologia de diseno de redes top-down]] existe para resolver esos compromisos con criterio.

## Relacionadas

- [[Amenazas y soluciones de seguridad en red]] — la cuarta característica, la seguridad, desarrollada aparte y por capas
- [[Tendencias de red]] — las exigencias nuevas —BYOD, video, nube— que ponen a prueba estas cuatro características
