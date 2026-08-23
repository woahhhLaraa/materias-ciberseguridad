---
tipo: moc
hilo: ciclo-gestion-seguridad
tags: [moc, proceso, pdca, nist, metodologia]
semestres: [1, 2]
---
#review
# MOC — El ciclo de gestión de seguridad

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[La seguridad informatica como proceso]] (sem. 1) → ciclo PDCA en [[Estandares de seguridad]] (sem. 2) → [[NIST CSF]] (sem. 2) → [[Metodologia de diseno de redes top-down|PDIOO]] (sem. 2)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

## El arco del hilo

Es el mismo esqueleto cíclico contado en cuatro vocabularios distintos. Vale la pena verlos alineados:

| Sem. 1 — proceso | ISO — PDCA | NIST CSF | Redes — PDIOO |
|---|---|---|---|
| Valoración de riesgos | Planificar | Gobernar / Identificar | Planificación |
| Prevención | Hacer | Proteger | Diseño + Implementación |
| Detección | Verificar | Detectar | Operación (monitoreo) |
| Respuesta | Actuar | Responder / Recuperar | Optimización |
| Repetición | (vuelve a Planificar) | (continuo) | (vuelve a Planificación) |

Ninguno de los cuatro tiene un "final": todos vuelven al principio. Esa es la idea que se repite.

---

## 1. La seguridad informática como proceso

*Fuente: [[La seguridad informatica como proceso]] — Introducción a la ciberseguridad, sem. 1*

La seguridad no es un estado que se alcanza, es un **ciclo que se repite**.

### Fases del ciclo

1. **Valoración de riesgos** — el punto de partida siempre es el riesgo
2. **Prevención** de los riesgos identificados
3. **Detección** de incidentes: comprobar si la valoración y la prevención funcionan
4. **Respuesta** en caso de incidente
5. **Repetición**

### Tareas que sostienen el ciclo

- Auditoría
- Reducir la posibilidad de nuevos incidentes
- Facilitar la detección de incidentes
- Minimizar el impacto en el sistema de información
- Recuperación de daños

---

## 2. Estándares de seguridad y el ciclo Deming (PDCA)

*Fuente: [[Estandares de seguridad]] — Marco legal y ético de la ciberseguridad, sem. 2*

Directrices y prácticas recomendadas para proteger la información de una organización o persona frente a amenazas cibernéticas.

### Panorama de estándares

| Estándar                     | Qué aporta                                                                                   |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| [[ISO-IEC 27001]]            | Requisitos para un Sistema de Gestión de Seguridad de la Información (SGSI) de forma general |
| ISO/IEC 27002                | Directrices y controles **concretos** para aplicar medidas efectivas                         |
| [[NIST CSF]]                 | Marco de gestión de riesgo del instituto de estándares de EE. UU.                            |
| [[Controles CIS y PCI DSS]]  | Controles críticos de internet y seguridad de datos de tarjetas de pago                      |
| SOC 2                        | Informe de auditoría sobre controles de servicio                                             |
| ENS y serie 800 del CCN-CERT | Marco español / esquema nacional de seguridad                                                |
| COSO y COBIT                 | Modelos de control interno y gobierno de TI                                                  |

> ⚠️ Pendiente de clase: completar la explicación de COSO y COBIT.

### Objetivo común

Todos apuntan a lo mismo: **confidencialidad, integridad y disponibilidad**. Ver [[MOC - La triada CIA]].

### El ciclo Deming (PDCA)

La propia ISO trabaja sobre el ciclo Deming, de cuatro fases:

1. **Planificar** (Plan)
2. **Hacer** (Do)
3. **Verificar** (Check)
4. **Actuar** (Act) — detección de problemas y necesidades

Es el mismo esqueleto cíclico de la nota anterior y de las funciones del NIST CSF. Conviene verlos como una sola idea repetida en tres vocabularios.

### Por qué las organizaciones los adoptan

Estos estándares se certifican, revisan y auditan periódicamente. Las organizaciones buscan demostrar confianza y compromiso con los datos de sus clientes, y la certificación es la forma más legible de hacerlo: se convierte en **ventaja competitiva**.

### Tipos de publicación

Las normas de seguridad se dividen en tres grupos:

- Nociones fundamentales de seguridad
- Requisitos de seguridad
- Guías de seguridad

---

## 3. NIST CSF (Cybersecurity Framework)

*Fuente: [[NIST CSF]] — Marco legal y ético de la ciberseguridad, sem. 2*

Marco de referencia de ciberseguridad diseñado principalmente para el **sector privado**, que ayuda a las organizaciones a gestionar, evaluar y mejorar sus riesgos.

Desarrollado por el **National Institute of Standards and Technology**, el Instituto Nacional de Estándares y Tecnología de Estados Unidos, cuyo objetivo es promover la innovación, el desarrollo tecnológico y la competitividad industrial mediante estándares y guías.

A diferencia de [[ISO-IEC 27001]], **no es certificable**: es una guía de referencia.

### Objetivos

- Describir el estado objetivo de la ciberseguridad: ¿cómo estamos?
- Identificar y priorizar oportunidades de mejora: ¿qué hago para mejorar?
- Facilitar la comunicación sobre riesgos entre las partes interesadas, internas y externas (interesado = cualquier elemento que participa en el proceso)

### Tres componentes

- **Núcleo** — conjunto de actividades y resultados deseados, organizados en funciones
- **Niveles** — grado en que la gestión adopta los controles definidos
- **Perfiles** — configuración de requisitos, tolerancia al riesgo y recursos actuales frente a los resultados deseados

### Las funciones

**Gobernar → Identificar → Proteger → Detectar → Responder → Recuperar**

#### 1. Identificar (ID)
Comprender el contexto de la organización y sus recursos: activos de información, sistemas y dispositivos, procesos de negocio, riesgos asociados.
👉 *No se puede proteger lo que no se conoce.*

#### 2. Proteger (PR)
Implementar medidas para proteger los activos críticos: control de acceso, protección de datos, capacitación del personal, seguridad física, políticas y procedimientos.
👉 *Se implementan barreras para evitar que los ataques ocurran.*

#### 3. Detectar (DE)
Identificar rápidamente actividad sospechosa: monitoreo, detección de anomalías, análisis de eventos, alertas.
👉 *Detectar rápido significa reducir el daño.*

#### 4. Responder (RS)
Se activa cuando el incidente ya ocurrió: planes de respuesta, análisis del ataque, comunicación interna y externa, contención, mejora de procesos.
👉 *Cuando ocurre un ataque hay que actuar rápido y con un plan.*

#### 5. Recuperar (RC)
Restaurar sistemas y operaciones: restauración de servicios, recuperación de datos, continuidad del negocio, lecciones aprendidas. Su meta es la **ciberresiliencia**.
👉 *No basta con defenderse; también hay que poder recuperarse.*

#### 6. Gobernar (GV) — añadido en CSF 2.0 (2024)
Estrategia de ciberseguridad, gestión organizacional del riesgo, políticas y responsabilidades, supervisión y cumplimiento.
👉 *La ciberseguridad debe ser parte de la estrategia del negocio.*

### Niveles de implementación (madurez)

| Nivel | Nombre | Característica | Idea |
|---|---|---|---|
| 1 | Parcial | Gestión informal, procesos no documentados, aplicación reactiva | Seguridad improvisada |
| 2 | Informado por el riesgo | Reconoce los riesgos, algunas prácticas existen, sin formalizar | Empiezan a tomarlo en serio |
| 3 | Repetible | Procesos documentados, gestión aplicada en toda la organización, planes definidos | Seguridad organizada y consistente |
| 4 | Adaptativo | Alta ciberresiliencia, aprende de incidentes, anticipa amenazas | Seguridad madura y proactiva |

### Pasos para implementarlo

1. **Priorizar y definir alcance** — objetivos, sistemas a proteger, procesos involucrados
2. **Orientar** — evaluación inicial: activos, sistemas, amenazas, regulaciones aplicables
3. **Crear el perfil actual** — estado presente de la ciberseguridad
4. **Evaluación de riesgos** — amenazas, vulnerabilidades, impacto
5. **Crear el perfil objetivo** — nivel de seguridad deseado y controles a implementar
6. **Analizar brechas** — perfil actual vs. objetivo, y de ahí el plan de mejora

---

## 4. Metodología de diseño de redes top-down (PDIOO)

*Fuente: [[Metodologia de diseno de redes top-down]] — Arquitectura de redes, sem. 2*

Proceso de varias fases organizado como un ciclo **PDIOO**:

**P**lanificación → **D**iseño → **I**mplementación → **O**peración → **O**ptimización

### Las fases

#### 1. Análisis de requerimientos
Se identifican los **objetivos y restricciones de negocio**:
- Metas de negocio
- Metas técnicas
- Analizar la red existente
- Analizar el tráfico existente

> El nombre "top-down" viene de aquí: se empieza por el negocio, no por el equipo. El error clásico es elegir el hardware primero.

#### 2. Desarrollo del diseño lógico

#### 3. Desarrollo del diseño físico

#### 4. Pruebas del diseño y documentación

#### 5. Implementación

#### 6. Monitoreo y optimización

---

## Relacionadas

- [[00 - Indice]] — el índice maestro con todos los hilos
- [[MOC - La triada CIA]] — el ciclo existe para sostener C, I y D
- [[MOC - El factor humano]] — el riesgo humano es la entrada del ciclo
- [[Riesgo amenaza y vulnerabilidad]] — el punto de partida de todo el ciclo
- [[Gestion de incidentes y reportes]] — las fases de respuesta en detalle
- [[Familia ISO 27000]]
- [[Proyecto red ECONEX]] — PDIOO aplicado a un caso real
