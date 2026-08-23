---
tipo: moc
hilo: triada-cia
tags:
  - moc
  - cia
  - fundamentos
  - normativa
semestres:
  - 1
  - 2
sr-due: 2026-08-26
sr-interval: 3
sr-ease: 250
---
#review
# MOC — La tríada CIA

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[Triada CIA]] (sem. 1) → [[Servicios de seguridad de la informacion]] (sem. 1) → [[ISO-IEC 27001]] (sem. 2) → [[Redes confiables]] (sem. 2)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

## El arco del hilo

Tres palabras de primer semestre (C, I, D) que primero se amplían a ocho servicios, luego se convierten en una norma certificable con auditorías y vigencia de tres años, y finalmente reaparecen como uno de los cuatro requisitos de una red confiable. El mismo criterio en tres niveles de compromiso: definición → gestión → ingeniería.

---

## 1. Tríada CIA

*Fuente: [[Triada CIA]] — Introducción a la ciberseguridad, sem. 1*

### Qué es la seguridad

Antes de la definición técnica conviene fijar la general: **seguridad es la ausencia de peligro**, la cualidad de algo o alguien que está seguro.

**Seguridad informática:** cualquier medida que impida la ejecución de operaciones no autorizadas dirigidas a un sistema.

### Los tres pilares

Recogidos en la ISO/IEC 17799 (hoy absorbida por la familia 27000):

| Pilar | Inglés | Significado |
|---|---|---|
| **Confidencialidad** | Confidentiality | Solo accede quien está autorizado |
| **Integridad** | Integrity | La información no se altera indebidamente |
| **Disponibilidad** | Availability | La información está accesible cuando se necesita |

### Objetivos de la seguridad informática

- Minimizar y gestionar riesgos
- Garantizar la utilización adecuada del sistema
- Limitar pérdidas y permitir la recuperación en caso de fallo
- Cumplir el marco legal y los requisitos de los clientes

### Por qué importa

La tríada es el criterio con el que se decide si un evento es un simple **evento de seguridad** o un **incidente**: si compromete C, I o D, es incidente. Ver [[Gestion de incidentes y reportes]].

---

## 2. Servicios de seguridad de la información

*Fuente: [[Servicios de seguridad de la informacion]] — Introducción a la ciberseguridad, sem. 1*

Los "derechos innegables" de un sistema. Amplían la tríada de tres a ocho.

| Servicio | Qué garantiza |
|---|---|
| **Confidencialidad** | La información solo la lee el destinatario legítimo |
| **Integridad** | Nadie no autorizado la modifica ni la elimina |
| **Disponibilidad** | Está lista para acceder cuando se requiera |
| **Consistencia** | El sistema se comporta como se espera: usuarios con los mismos permisos pueden hacer y ver lo mismo |
| **Autenticación** | La identidad del usuario, mensaje o equipo es legítima (contraseña, 2FA, llaves, biometría) |
| **Autorización** | Se controla el acceso a los servicios; no todos los usuarios tienen los mismos permisos |
| **No repudio** | Nadie puede negar haber enviado o recibido información |
| **Auditabilidad** | Se detectan comportamientos anómalos (intentos de contraseña, anticheat en un videojuego) |

### Consecuencias de incumplirlos

Si alguna de estas funciones falla, el resultado se paga fuera del plano técnico:

- Reputación arruinada
- Vandalismo
- Robo
- Pérdida de ingresos
- Propiedad intelectual dañada

---

## 3. ISO/IEC 27001

*Fuente: [[ISO-IEC 27001]] — Marco legal y ético de la ciberseguridad, sem. 2*

Norma internacional que establece los **requisitos para implementar un Sistema de Gestión de Seguridad de la Información (SGSI)**.

Publicada conjuntamente por:
- **ISO** (International Organization for Standardization) — estándares en múltiples áreas
- **IEC** (International Electrotechnical Commission) — estándares eléctricos y electrónicos

### Qué busca

- Proteger la información de una organización
- Gestionar riesgos de seguridad
- Implementar controles adecuados
- Mejorar continuamente

Está construida sobre la tríada CIA.

### Evolución histórica

| Año | Cambio |
|---|---|
| **2005** | Primera publicación oficial |
| **2013** | Actualización con estructura de alto nivel (HLS) para integrarse con otras normas ISO (9001, 22301) |
| **2022** | Versión vigente. Controles actualizados para nube, teletrabajo y nuevas amenazas digitales |

### Estructura de ISO/IEC 27001:2022

Diez cláusulas obligatorias:

1. Alcance
2. Referencias normativas
3. Términos y definiciones
4. Contexto de la organización
5. Liderazgo
6. Planificación
7. Apoyo
8. Operación
9. Evaluación del desempeño
10. Mejora

Estas cláusulas definen **cómo debe gestionarse la seguridad**, no los controles técnicos concretos. Para eso está la 27002 — ver [[Familia ISO 27000]].

### Certificación

1. Implementar un SGSI
2. Pasar auditorías internas
3. Ser auditada por un organismo certificador acreditado
4. Obtener certificación válida internacionalmente

Vigencia habitual: **3 años**, con auditorías de seguimiento anuales.

### Normalización en México

- **DGN (Dirección General de Normas)** — parte de la Secretaría de Economía. Representa a México ante ISO y supervisa que los organismos de certificación estén acreditados.
- **EMA (Entidad Mexicana de Acreditación)** — acredita a los organismos certificadores y verifica que operen conforme a estándares internacionales.

### Resumen

ISO/IEC 27001 es un estándar internacional, para implementar un SGSI, basado en gestión de riesgos, centrado en proteger la información, certificable y actualizado en 2022. **No es solo tecnología: es gestión, procesos, personas y mejora continua.**

---

## 4. Redes confiables

*Fuente: [[Redes confiables]] — Introducción a las redes de cómputo, sem. 2*

> Clase del 02/03/26

Cuatro características que debe cumplir una red para considerarse confiable.

### 1. Tolerancia a fallas

Disminuir el impacto de una falla limitando la cantidad de dispositivos afectados. Se logra proporcionando **redundancia** mediante una red de **paquetes conmutados**.

- La conmutación por paquetes divide el tráfico en paquetes que se enrutan a través de la red
- En teoría, **cada paquete puede tomar una ruta diferente** hacia el destino

Esa es exactamente la propiedad que da la tolerancia: si un enlace cae, los paquetes siguientes rodean.

### 2. Escalabilidad

Una red escalable puede expandirse fácil y rápidamente para admitir usuarios y aplicaciones nuevas **sin replantear toda la red** y sin afectar la arquitectura existente.

### 3. Calidad de servicio (QoS)

El principal mecanismo para garantizar la entrega confiable de contenido a todos los usuarios. Con QoS implementada, un router puede administrar más fácilmente el flujo de tráfico de voz, datos o video.

Es la respuesta al problema de la [[Tecnologias de acceso a internet|red convergente]].

### 4. Seguridad

- Implementación de firewalls
- Impedir el acceso incluso dentro de la misma LAN para diferentes usuarios
- Seguridad de la infraestructura
- Seguridad física de los dispositivos
- Se busca implementar la tríada CIA: confidencialidad, integridad y disponibilidad

### Nota de conexión

Las cuatro características se enfrentan entre sí en el diseño real: la redundancia cuesta dinero, la seguridad cuesta latencia, y QoS cuesta complejidad de configuración. La metodología [[Metodologia de diseno de redes top-down]] existe para resolver esos compromisos con criterio.

---

## Relacionadas

- [[00 - Indice]] — el índice maestro con todos los hilos
- [[MOC - El ciclo de gestion de seguridad]] — la tríada define *qué* proteger; el ciclo define *cómo*
- [[Gestion de incidentes y reportes]] — la tríada como criterio de qué cuenta como incidente
- [[Guerra de los mundos - analisis de ciberseguridad]] — la tríada aplicada a un caso narrativo
- [[Estandares de seguridad]] — todos los estándares apuntan a C, I y D
