---
tipo: meta
tags: [meta, mantenimiento, historia-del-vault]
---

# Migración de apuntes a Obsidian — resumen de la sesión

**Fecha:** 21 de agosto de 2026
**Vault:** `/home/larita/Documentos/Materias ciberseguridad`

---

## 1. La pregunta original

> Tengo mis apuntes de 3 semestres de ciberseguridad en `.odt`, más algunos PDFs que son libros enteros (esos no los quiero pasar, quizás solo referencias). ¿Deberíamos convertir todo a `.md` y pasarlo a Obsidian? ¿Cuál es el mejor acercamiento, obteniendo la mejor base y gastando la menor cantidad de tokens?

## 2. Diagnóstico inicial

| Qué | Cuánto | Decisión |
|---|---|---|
| Apuntes reales (`.odt`) | 19 archivos, ~600 KB de texto | Convertir a `.md` |
| Libros PDF | 4 (Silberschatz, Tanenbaum ×2, Presentación) — 98 de los 110 MB | **No** convertir, solo enlazar |
| PDFs que duplican un `.odt` propio | 5 | Ignorar, ya existe el original editable |
| Programas de estudio (PE) en PDF | 4 | Enlazar como referencia |
| Binarios (`.pkt`, `.mp4`, `.pptx`, `.docx`) | 5 | Dejar como adjuntos |
| `misApuntes/` | Vault de Obsidian **vacío** | Reubicar |

Hallazgos del diagnóstico:
- `Administracion de redes.odt` estaba **vacío (0 bytes)**
- Había un lock file huérfano de LibreOffice en Probabilidad

## 3. Decisión clave sobre el enfoque

**La conversión no la debe hacer un LLM.**

`pandoc` convierte ODT → Markdown de forma determinista, conservando encabezados, listas, tablas y extrayendo las imágenes incrustadas. Coste: **cero tokens**, y más fiel que una transcripción manual.

Pasar 600 KB de texto a un modelo solo para "convertirlo" habría sido ~200k tokens de puro desperdicio, con riesgo de alterar el contenido.

El modelo solo aporta valor **después**, en lo que pandoc no puede hacer: títulos, frontmatter, enlaces entre notas y detección de conexiones entre materias.

## 4. Decisión sobre la ubicación del vault

En lugar de mover los apuntes *dentro* de `misApuntes/`, se hizo que **`Materias ciberseguridad` entera fuera el vault** (moviendo `.obsidian/` a la raíz).

**Ventaja:** los PDFs quedan dentro del vault y se enlazan con `![[libro.pdf]]` — Obsidian los abre nativamente — sin duplicar 98 MB ni convertir libros enteros a Markdown ilegible.

## 5. Decisiones tomadas por el usuario

| Pregunta | Elección |
|---|---|
| ¿Qué hacer con los `.odt` originales? | **Conservarlos donde están** (nada se borra) |
| ¿Cómo organizar las materias? | **Dejar las carpetas como están**, semestre en el frontmatter |
| ¿Nivel de curación? | **Curación profunda** (reescribir, reestructurar, enlazar entre conceptos) |

El usuario confirmó después: *"son exámenes que ya pasaron, incluso si mejoras alguna que otra definición tampoco está mal"*.

## 6. Ejecución

1. **Respaldo** de los 28 archivos fuente → `~/Documentos/respaldo-apuntes-20260821.tar.gz` (777 KB)
2. **Vault montado en la raíz**: `.obsidian/` movido, `misApuntes/` eliminada, lock file borrado
3. **Instalación de pandoc** (`sudo apt install -y pandoc`) — hecha por el usuario, requería contraseña
4. **Conversión**: 19 `.odt` → `.md` con `--extract-media`, ~137 KB de Markdown
5. **Imágenes**: 4 extraídas, aplanadas a `_adjuntos/` con nombres descriptivos
6. **Curación profunda**: 96 notas enlazadas

## 7. Resultado final

**96 notas**, **423 enlaces `[[ ]]`**, **cero enlaces rotos**. Los 20 `.odt` originales intactos.

| Materia | Notas | Semestre |
|---|---|---|
| Marco legal y ético | 18 | 2 |
| Introducción a las redes de cómputo | 12 | 2 |
| Organización de computadoras | 11 | 1 |
| Introducción a la ciberseguridad | 10 | 1 |
| Arquitectura de redes | 8 | 2 |
| Matemáticas discretas | 8 | 1 |
| Enrutamiento básico | 7 | 3 |
| Sistemas Operativos | 4 | 3 |
| Aspectos sociales de la ciberseguridad | 4 | 3 |
| Probabilidad y estadística | 4 | 2 |
| Desarrollo de Habilidades Informativas | 2 | 2 |
| Administración de redes | 1 | 2 |

### Los seis hilos transversales

El mayor valor de la curación: los apuntes repetían los mismos conceptos en tres vocabularios distintos sin saberlo. En `00 - Indice.md` quedaron mapeados:

1. **Tríada CIA** — Triada CIA (s1) → Servicios de seguridad (s1) → ISO/IEC 27001 (s2) → Redes confiables (s2)
2. **Ciclo de gestión de seguridad** — La seguridad como proceso (s1) → PDCA (s2) → NIST CSF (s2) → PDIOO (s2)
3. **Factor humano** — Planos de actuación (s1) → Tipos de atacantes (s1) → Riesgo humano (s2) → Comportamiento y conducta (s3)
4. **Direccionamiento IP** — Sistemas numéricos (s1) → Capa de red IPv4/IPv6 (s2) → Direccionamiento con clases (s3) → CIDR y VLSM (s3)
5. **Hardware → SO** — Generaciones de computadoras (s1) → Jerarquía de memoria (s1) → Técnicas de E/S (s1) → Generaciones de SO (s3)
6. **Matemáticas → redes** — Teoría de grafos (s1) → Relaciones de equivalencia (s1) → Topologías de red (s2)

## 8. Errores encontrados y corregidos

Esto fue lo que la curación profunda aportó más allá de convertir:

1. **Archivo mal ubicado** — `Probabilidad y estadistica/2.odt` no era de probabilidad: eran ejercicios de clases de direcciones IP. Movido a Enrutamiento básico como *Tarea 2*, con nota en ambos extremos.

2. **Error aritmético en Tarea 1** — de las 13 filas de conversión binario/hexadecimal, la primera tenía `84 = 0100 1010 = 4A`. Pero 4A hexadecimal es **74** decimal, no 84. Correcto: `84 = 0101 0100 = 0x54`. Las otras doce estaban bien.

3. **Error conceptual en Matemáticas discretas** — los apuntes definían "relación simétrica" como la que cumple las tres propiedades. Esa es la **relación de equivalencia**.

4. **"Preposición" → "proposición"** en lógica proposicional (son cosas distintas).

5. **Condición de Euler** — dictada como "valencia paralelos", corregida a **valencia par**.

6. **`Administracion de redes.odt` vacío** — nota índice que lo advierte, por si hay que buscar en la papelera.

## 9. Cómo tomar notas de aquí en adelante

**La regla: no crear una nota por concepto durante la clase.** Sería contraproducente — obliga a decidir la estructura antes de entender el tema.

| Fase | Cuándo | Qué se hace |
|---|---|---|
| **Captura** | En clase | Todo a `Notas en curso.md` de la materia, bajo un encabezado con la fecha. Sin pensar en estructura. |
| **Cosecha** | Al estudiar para el parcial | Dividir ese archivo en notas por concepto |

**La fase 2 es estudiar.** Decidir "esto es un concepto, esto se conecta con aquello" es el trabajo de comprensión que harías igual antes del examen.

### El mecanismo (Note Composer, ya activo)

1. Seleccionar el bloque del concepto en `Notas en curso.md`
2. `Ctrl+P` → **"Extraer selección actual"**
3. Obsidian crea la nota, mueve el texto y deja un `[[enlace]]` en su lugar

Tres segundos por concepto. Conviene asignarle un atajo de teclado.

### Cuándo algo merece nota propia

- ✅ Se cita desde otra materia (criterio más fuerte)
- ✅ Lo buscarías suelto en el buscador
- ✅ Tiene estructura interna (subtítulos, tablas)
- ❌ Una definición de dos líneas que solo tiene sentido dentro de su tema

Ejemplo de agrupación deliberada: `Puertos y conectores` reúne diez conectores en una sola nota porque solo se entienden comparándose entre sí.

### Qué capturar sí o sí

Lo único que no se puede reconstruir después:

- **La fecha de cada clase**
- **Cuando el profesor diga "esto viene en el examen"** (se marca con ⭐)
- **Cuando algo suene raro o no se entienda, escribirlo así** — un "no entendí esta parte" es señal útil

Faltas de ortografía, frases a medias y viñetas sueltas dan igual: eso se arregla en la pasada.

## 10. Andamiaje montado

- **`Notas en curso.md`** en las tres materias del semestre activo, enlazadas desde el índice de su materia
- **`_plantillas/`** con `Concepto.md` (frontmatter + sección "Relacionadas") y `Clase.md` (encabezado con fecha)
- **`_convenciones.md`** — documento de mantenimiento del vault: frontmatter, criterio de separación, estilo y el procedimiento de 7 pasos de la pasada de cierre
- **Adjuntos** configurados a `_adjuntos/`

## 11. Acuerdo de trabajo

**El usuario captura en crudo durante el semestre; la reorganización general se hace al cerrar cada semestre.**

Basta con decir *"toca la pasada de fin de semestre"*. Las convenciones están en `_convenciones.md` dentro del vault, así que la pasada no empieza de cero.

Semestre 3 termina alrededor del **30 de noviembre de 2026**.

### Dos advertencias

- **Los parciales llegan antes que el fin de semestre.** Si hay examen en octubre, procesar esa materia entonces: ese trabajo *es* el repaso. Aplazarlo hasta diciembre pierde el beneficio de estudio.
- **Los pendientes ⚠️ son del usuario**, no se pueden completar sin clase o libro.

## 12. Pendientes marcados en el vault

Listados al final de `00 - Indice.md`:

- **Sistemas de protección eléctrica** — pregunta de examen, en `Normas de seguridad fisica`
- **COSO y COBIT** — explicación incompleta en `Estandares de seguridad`
- **Ejercicios de conversión de bases** sin resolver en `Conversion entre bases`
- **Temas de SO sin desarrollar**: capas, E/S, concurrencia, instalación

---

## Referencia rápida de rutas

| Qué | Dónde |
|---|---|
| Vault | `~/Documentos/Materias ciberseguridad` |
| Índice maestro | `~/Documentos/Materias ciberseguridad/00 - Indice.md` |
| Convenciones | `~/Documentos/Materias ciberseguridad/_convenciones.md` |
| Respaldo pre-migración | `~/Documentos/respaldo-apuntes-20260821.tar.gz` |

## Relacionadas

- [[_convenciones]] — las convenciones que salieron de esta migración y que rigen el vault hoy
- [[Plan de accion - Sistema PKM semestre]] — el plan de estudio que se montó sobre el vault ya migrado
