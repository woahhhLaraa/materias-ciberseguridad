---
materia: Marco legal y etico de la ciberseguridad
semestre: 2
tipo: concepto
tags: [normativa, nist, marco]
---

# NIST CSF (Cybersecurity Framework)

Marco de referencia de ciberseguridad diseñado principalmente para el **sector privado**, que ayuda a las organizaciones a gestionar, evaluar y mejorar sus riesgos.

Desarrollado por el **National Institute of Standards and Technology**, el Instituto Nacional de Estándares y Tecnología de Estados Unidos, cuyo objetivo es promover la innovación, el desarrollo tecnológico y la competitividad industrial mediante estándares y guías.

A diferencia de [[ISO-IEC 27001]], **no es certificable**: es una guía de referencia.

## Objetivos

- Describir el estado objetivo de la ciberseguridad: ¿cómo estamos?
- Identificar y priorizar oportunidades de mejora: ¿qué hago para mejorar?
- Facilitar la comunicación sobre riesgos entre las partes interesadas, internas y externas (interesado = cualquier elemento que participa en el proceso)

## Tres componentes

- **Núcleo** — conjunto de actividades y resultados deseados, organizados en funciones
- **Niveles** — grado en que la gestión adopta los controles definidos
- **Perfiles** — configuración de requisitos, tolerancia al riesgo y recursos actuales frente a los resultados deseados

## Las funciones

**Gobernar → Identificar → Proteger → Detectar → Responder → Recuperar**

### 1. Identificar (ID)
Comprender el contexto de la organización y sus recursos: activos de información, sistemas y dispositivos, procesos de negocio, riesgos asociados.
👉 *No se puede proteger lo que no se conoce.*

### 2. Proteger (PR)
Implementar medidas para proteger los activos críticos: control de acceso, protección de datos, capacitación del personal, seguridad física, políticas y procedimientos.
👉 *Se implementan barreras para evitar que los ataques ocurran.*

### 3. Detectar (DE)
Identificar rápidamente actividad sospechosa: monitoreo, detección de anomalías, análisis de eventos, alertas.
👉 *Detectar rápido significa reducir el daño.*

### 4. Responder (RS)
Se activa cuando el incidente ya ocurrió: planes de respuesta, análisis del ataque, comunicación interna y externa, contención, mejora de procesos.
👉 *Cuando ocurre un ataque hay que actuar rápido y con un plan.*

### 5. Recuperar (RC)
Restaurar sistemas y operaciones: restauración de servicios, recuperación de datos, continuidad del negocio, lecciones aprendidas. Su meta es la **ciberresiliencia**.
👉 *No basta con defenderse; también hay que poder recuperarse.*

### 6. Gobernar (GV) — añadido en CSF 2.0 (2024)
Estrategia de ciberseguridad, gestión organizacional del riesgo, políticas y responsabilidades, supervisión y cumplimiento.
👉 *La ciberseguridad debe ser parte de la estrategia del negocio.*

## Niveles de implementación (madurez)

| Nivel | Nombre | Característica | Idea |
|---|---|---|---|
| 1 | Parcial | Gestión informal, procesos no documentados, aplicación reactiva | Seguridad improvisada |
| 2 | Informado por el riesgo | Reconoce los riesgos, algunas prácticas existen, sin formalizar | Empiezan a tomarlo en serio |
| 3 | Repetible | Procesos documentados, gestión aplicada en toda la organización, planes definidos | Seguridad organizada y consistente |
| 4 | Adaptativo | Alta ciberresiliencia, aprende de incidentes, anticipa amenazas | Seguridad madura y proactiva |

## Pasos para implementarlo

1. **Priorizar y definir alcance** — objetivos, sistemas a proteger, procesos involucrados
2. **Orientar** — evaluación inicial: activos, sistemas, amenazas, regulaciones aplicables
3. **Crear el perfil actual** — estado presente de la ciberseguridad
4. **Evaluación de riesgos** — amenazas, vulnerabilidades, impacto
5. **Crear el perfil objetivo** — nivel de seguridad deseado y controles a implementar
6. **Analizar brechas** — perfil actual vs. objetivo, y de ahí el plan de mejora

## Relacionadas

- [[Estandares de seguridad]] — el panorama donde encaja, junto a ISO 27001, los controles CIS y PCI DSS
- [[Gestion de incidentes y reportes]] — el NIST también define las fases de respuesta a incidentes
- [[La seguridad informatica como proceso]] — la misma idea, versión de primer semestre
