---
tipo: moc
hilo: factor-humano
tags: [moc, factor-humano, riesgo, actores, psicologia]
semestres: [1, 2, 3]
---

# MOC — El factor humano

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[Planos de actuacion en ciberseguridad]] (sem. 1) → [[Tipos de atacantes]] (sem. 1) → [[Riesgo amenaza y vulnerabilidad|riesgo humano]] (sem. 2) → [[Comportamiento y conducta]] (sem. 3)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

## El arco del hilo

Es el único hilo que atraviesa los tres semestres, y va estrechando el foco: primero se afirma que existe un plano humano y que es el más vulnerable; luego se catalogan las personas que atacan; luego se formaliza el riesgo humano como categoría de riesgo; y finalmente, en tercer semestre, se explica el **mecanismo** — la estructura de tres pasos de la conducta, que es exactamente donde entra la ingeniería social. La respuesta a "¿por qué el plano humano es el más vulnerable?" tarda tres semestres en llegar.

---

## 1. Planos de actuación en ciberseguridad

*Fuente: [[Planos de actuacion en ciberseguridad]] — Introducción a la ciberseguridad, sem. 1*

La seguridad no se resuelve solo con tecnología. Actúa en cuatro planos simultáneos:

- **Plano humano** — toda la gente que trabaja con la información guardada. Aquí entra una cuestión ética y moral de cada persona. Es el plano más vulnerable, y por eso se insiste en capacitación y protocolos.
- **Plano técnico** — el soporte en la estructura de la organización.
- **Plano organizacional** — las políticas que establece la organización.
- **Plano legislativo** — está fuera del alcance del técnico, pero define bajo qué marco legal se cuida la información y qué pasa si hay una violación.

---

## 2. Tipos de atacantes

*Fuente: [[Tipos de atacantes]] — Introducción a la ciberseguridad, sem. 1*

Personas o grupos que intentan aprovechar vulnerabilidades para obtener una ganancia personal o financiera.

### Clasificación por origen y motivación

| Categoría | Quiénes | Motivación |
|---|---|---|
| **Externo** | Ciberdelincuentes, hackers (sombrero negro o aficionados), hacktivistas, APTs, terroristas, lobos solitarios, proveedores maliciosos | Económica, ideológica, política, experimentación |
| **Interno (malicioso)** | Empleados, contratistas o asociados que roban, sabotean o espían | Financiera, venganza, ideológica |
| **Interno (no intencional)** | Errores, negligencia, falta de formación | Ignorancia, descuido |
| **Credenciales robadas** | Externos que entran con acceso legítimo robado | Ocultamiento, bypass de seguridad |

La cuarta categoría es la incómoda: el atacante se ve como usuario válido, así que los controles de autenticación no lo detienen. Solo lo atrapa la [[Servicios de seguridad de la informacion|auditabilidad]].

### Nota sobre "hacker"

En los apuntes de clase se usa "hacker" como sinónimo de atacante. Técnicamente el término neutro es **actor de amenaza**; "hacker de sombrero negro" es el malicioso, "sombrero blanco" el que trabaja con autorización.

---

## 3. Riesgo, amenaza y vulnerabilidad

*Fuente: [[Riesgo amenaza y vulnerabilidad]] — Marco legal y ético de la ciberseguridad, sem. 2*

Tres términos que se confunden constantemente y que los exámenes separan.

| Término | Definición |
|---|---|
| **Riesgo** | Susceptibilidad hacia una situación no beneficiosa. Efecto de la incertidumbre sobre los objetivos. |
| **Amenaza** | Causa potencial e inminente de daño; un riesgo materializado o a punto de materializarse. |
| **Vulnerabilidad** | Debilidad que puede convertirse en la vía por la que una amenaza se concreta. |

### Las fórmulas

```
Riesgo = Probabilidad × Impacto
Amenaza × Vulnerabilidad = Consecuencia negativa
```

### La idea central del curso

> Un riesgo está presente en **todas** las actividades que se puedan realizar y que pudiesen ser interrumpidas. Los riesgos se asumen y se aceptan, minimizándolos al mínimo.

No existe el riesgo cero. Todo proceso de gestión de calidad y seguridad **empieza** por la gestión de riesgos: el punto de partida siempre es el riesgo.

### Riesgo humano

Amenazas que surgen de acciones, errores o conductas de las personas, intencionales o no. El factor humano es siempre uno de los puntos más vulnerables — de ahí la insistencia en capacitación, cumplimiento de protocolos y supervisión constante.

- Ingreso de personal no autorizado
- Suplantación de identidad
- Ingeniería social
- Webs maliciosas y phishing
- Redes inseguras o falsas
- Negligencia y malas prácticas

---

## 4. Comportamiento y conducta

*Fuente: [[Comportamiento y conducta]] — Aspectos sociales de la ciberseguridad, sem. 3*

Dos términos que se usan como sinónimos y que el curso distingue.

### Comportamiento

- Manera de comportarse
- Potencial y capacidad expresada para la actividad física, mental y social durante las fases de la vida humana
- Lo influyen **factores internos**
- Depende del contexto, tanto físico como social

### Conducta

- **Respuesta a una motivación**
- Proceso que incluye:
  1. La **elaboración o interpretación** del estímulo
  2. Procesos asociativos que **transforman e integran** la información recibida con la experiencia y situación del sujeto
  3. La **selección y ejecución** de acciones específicas

Toda conducta se concibe dentro de un contexto, tanto natural como construido.

### La distinción en una línea

El **comportamiento** es la capacidad y el patrón general; la **conducta** es la respuesta concreta a un estímulo concreto, y tiene una estructura de tres pasos.

### Por qué importa en ciberseguridad

Esa estructura de tres pasos es exactamente donde opera la **ingeniería social**: el atacante no rompe el sistema, interviene en el paso 1 —la interpretación del estímulo— presentando un estímulo falso que el sujeto integra con su experiencia previa y al que responde con la acción que el atacante quería.

Ver [[Guerra de los mundos - analisis de ciberseguridad]].

---

## Relacionadas

- [[00 - Indice]] — el índice maestro con todos los hilos
- [[MOC - El ciclo de gestion de seguridad]] — el riesgo humano como entrada del ciclo
- [[CyBOK]]
- [[Conciencia y trascendencia]] — el mismo problema desde la filosofía
- [[LFPDPPP - Ley de proteccion de datos]] — el plano legislativo en México
- [[Normas de seguridad fisica]]
- [[Caso Pemex - DoppelPaymer]] — un actor externo real, con nombre
- [[Actividad 1 - Buenas practicas de ciberseguridad]] — el caso propio: saber la buena práctica y no cumplirla
