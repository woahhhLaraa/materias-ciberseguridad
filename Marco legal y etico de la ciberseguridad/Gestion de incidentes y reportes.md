---
materia: Marco legal y etico de la ciberseguridad
semestre: 2
tipo: concepto
tags: [normativa, incidentes, reportes]
equipo: 2
---

# Gestión de incidentes y reportes

> Exposición del Equipo 2

Generar reportes permite detectar amenazas, minimizar riesgos y cumplir obligaciones legales.

## Evento vs. incidente

La distinción más examinable del tema:

| | Definición | Ejemplos |
|---|---|---|
| **Evento de seguridad** | Actividad registrada en un sistema. **No es un riesgo por sí misma.** | Inicio de sesión, error de aplicación, intento fallido de acceso |
| **Incidente de seguridad** | Evento no deseado que **compromete la confidencialidad, integridad o disponibilidad** | Acceso no autorizado, ransomware, filtración de datos, pérdida de un dispositivo con datos sensibles |

El criterio que separa uno de otro es la [[Triada CIA]]. Un incidente no siempre implica daño inmediato — un intento de intrusión a la red ya lo es.

## Qué es un reporte

Mucho más que una lista de problemas técnicos: un documento que **debería entender cualquier persona de la organización**. Registra y analiza un incidente para dejar evidencia clara y estructurada, analizar causas y consecuencias, y proponer medidas correctivas.

### Normas para redactarlo

- Claro, completo y útil
- Preciso, sin lenguaje técnico innecesario
- **Sin opiniones personales** — descripción de hechos
- Estructura ordenada
- Veracidad
- Confidencialidad
- Con acciones recomendadas

### Contenido mínimo

1. Resumen ejecutivo
2. Información general
3. Detalle técnico
4. Impacto
5. Acciones
6. Recomendaciones

## Proceso de gestión de incidentes

Pasos organizados para identificar, analizar, responder y **aprender** de un incidente, minimizando su impacto y evitando recurrencias:

1. Identificación
2. Registro
3. Clasificación
4. Respuesta
5. Comunicación
6. Lecciones aprendidas

### Ejemplo práctico ante un ataque

Evento detectado → Clasificación del evento → Contención → Erradicación → Recuperación → Reporte final

### Las fases del NIST

El estándar más utilizado a nivel mundial:

1. Preparación
2. Detección y análisis
3. Contención, erradicación y recuperación
4. Actividad post-incidente

Ver [[NIST CSF]].

## Métricas

| Métrica | Qué mide |
|---|---|
| **MTTD** (Mean Time To Detect) | Desde el inicio del incidente hasta que la organización lo detecta |
| **MTTR** (Mean Time To Respond) | Desde la detección hasta la contención, remediación y retorno |
| **Downtime** | Valor total que la organización pierde durante el incidente |

Reducir el MTTD es donde más se gana: todo el daño se acumula mientras el ataque pasa inadvertido.

## Marco legal aplicable

- **Protección de datos**: GDPR / [[LFPDPPP - Ley de proteccion de datos]]
- **Sector financiero**: PCI DSS — ver [[Controles CIS y PCI DSS]]
- **Gestión general**: [[ISO-IEC 27001]]
- **Integridad de datos**: SHA-256 y la norma oficial mexicana sobre conservación de mensajes de datos y digitalización de documentos, que garantiza que los documentos electrónicos mantengan validez legal, integridad y valor probatorio en el tiempo (NOM-151-SCFI)

## Relacionadas

- [[Organismos reguladores en Mexico]] — a quién se reporta en México
- [[Caso Pemex - DoppelPaymer]] — un incidente real para aplicar este esquema
