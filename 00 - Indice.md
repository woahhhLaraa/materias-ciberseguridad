---
tipo: indice-maestro
tags: [moc, indice]
---

# Apuntes — Ciberseguridad UV

Vault de los tres semestres de la carrera. Cada materia tiene una nota índice con los datos del curso, la evaluación y los enlaces a sus temas.

## Semestre 1 — Ago–Dic 2025

- [[Introduccion a la ciberseguridad]]
- [[Organizacion de computadoras]]
- [[Matematicas discretas]]

## Semestre 2 — Feb–Jun 2026

- [[Marco legal y etico de la ciberseguridad]]
- [[Introduccion a las redes de computo]]
- [[Arquitectura de redes]]
- [[Probabilidad y estadistica]]
- [[Administracion de redes]] ⚠️ sin apuntes
- [[Desarrollo de Habilidades Informativas]]

## Semestre 3 — Ago–Dic 2026 (en curso)

- [[Sistemas Operativos (materia)]]
- [[Enrutamiento basico (materia)]]
- [[Aspectos sociales de la ciberseguridad]]

## MOCS

Estos conceptos reaparecen en distintos semestres con distinto nivel de detalle. Vale la pena estudiarlos como una sola cosa.

Cada hilo tiene además un **documento consolidado** en `_MOCS/` que reúne el contenido completo de sus notas en un solo archivo, para estudiarlo corrido. Las notas originales siguen siendo la fuente: si algo se corrige, se corrige en las dos.

### La tríada CIA
📄 [[MOC - La triada CIA]]

[[Triada CIA]] (sem. 1) → [[Servicios de seguridad de la informacion]] (sem. 1) → [[ISO-IEC 27001]] (sem. 2) → [[Redes confiables]] (sem. 2)

### El ciclo de gestión de seguridad
📄 [[MOC - El ciclo de gestion de seguridad]]

[[La seguridad informatica como proceso]] (sem. 1) → ciclo PDCA en [[Estandares de seguridad]] (sem. 2) → [[NIST CSF]] (sem. 2) → [[Metodologia de diseno de redes top-down|PDIOO]] (sem. 2)

### El factor humano
📄 [[MOC - El factor humano]]

[[Planos de actuacion en ciberseguridad]] (sem. 1) → [[Tipos de atacantes]] (sem. 1) → [[Riesgo amenaza y vulnerabilidad|riesgo humano]] (sem. 2) → [[Comportamiento y conducta]] (sem. 3)

### Direccionamiento IP
📄 [[MOC - Direccionamiento IP]]

[[Sistemas numericos]] (sem. 1) → [[Capa de red - IPv4 e IPv6]] (sem. 2) → [[Funcionamiento de IPv4]] (sem. 3) → [[Direccionamiento IP con clases]] (sem. 3) → [[Enmascaramiento y subnetting]] (sem. 3) → [[CIDR y VLSM]] (sem. 3)

### Hardware → sistema operativo
📄 [[MOC - Hardware a sistema operativo]]

[[Generaciones de computadoras]] (sem. 1) → [[Jerarquia de memoria]] (sem. 1) → [[Tecnicas de entrada y salida]] (sem. 1) → [[Generaciones de sistemas operativos]] (sem. 3) → [[Gestion de memoria]] (sem. 3) → [[Gestion de procesos]] (sem. 3)

### Estructura interna de un CPU
📄 [[MOC - Estructura interna de un CPU]] ⚠️ en construcción

[[Jerarquia de memoria]] (sem. 1)

### Matemáticas → redes
📄 [[MOC - Matematicas a redes]]

[[Teoria de grafos]] (sem. 1) → [[Relaciones de equivalencia y particiones]] (sem. 1) → [[Clasificacion de redes|topologías de red]] (sem. 2)

## Casos de estudio

- [[Caso Pemex - DoppelPaymer]] — ransomware en infraestructura crítica mexicana
- [[Guerra de los mundos - analisis de ciberseguridad]] — análisis sobre ficción

## Convenciones del vault

- Cada nota lleva frontmatter con `materia`, `semestre` y `tipo`
- `tipo`: `indice`, `concepto`, `referencia`, `tarea`, `trabajo`, `proyecto`, `caso`, `actividad`, `examen`, `practica`
- Los `.odt` originales se conservan junto a cada nota
- Los PDFs y binarios se enlazan con `![[nombre.pdf]]`; Obsidian los abre nativamente
- Imágenes extraídas de los documentos en `_adjuntos/`
- Los documentos consolidados de los hilos transversales viven en `_MOCS/`, con `tipo: moc`
