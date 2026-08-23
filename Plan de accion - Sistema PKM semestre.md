# Plan de acción — Sistema de estudio (Obsidian + NotebookLM)

> Semestre 3, cierra ~30 de noviembre de 2026
> Materias activas: Enrutamiento básico, Sistemas Operativos, Aspectos sociales de la ciberseguridad, Administración de redes

---

## Bloque 1 — Setup (una sola vez) ✅ completado

- [x] Instalar plugins: Spaced Repetition, Heatmap Calendar, Dataview
- [x] Crear los 6 MOCs (uno por hilo transversal), cada uno como nota separada solo con enlaces
- [x] Convertir el archivo original de las 6 listas en portada `MOC - Índice de hilos.md`, enlazando a los 6 MOCs
- [x] Sincronizar el vault a Drive (rclone) para que NotebookLM pueda leer notas y PDFs
- [x] Crear un notebook en NotebookLM por materia activa, con su PDF correspondiente (Silberschatz en SO, Tanenbaum en redes)
- [x] Crear `_recuperacion.md` con el checklist de 3 pasos
- [x] Actualizar `_convenciones.md`: "se procesa cada materia en su parcial, el fin de semestre solo consolida"

---

## Bloque 2 — Ritmo semanal (el 80% del tiempo)

**En clase:**
- Captura en `Notas en curso.md` de la materia, bajo encabezado con fecha, sin pensar en estructura
- Un símbolo para "viene en el examen" (⭐), otro para "no entendí" (❓)
- Grabar audio de la clase como respaldo — no depender de la memoria para marcar en tiempo real

**Entre clases (cosecha distribuida):**
- 2-3 sesiones cortas por semana (15-25 min), **una materia por sesión**
- Priorizar la materia con el parcial más próximo, no la que da más pereza
- Cosechar con Note Composer (Ctrl+P → Extraer selección actual)
- Criterio para nota propia: se cita desde otra materia / se buscaría suelto / tiene estructura interna
- Si algo cruza con otra materia ya vista, actualizar el MOC correspondiente en el momento
- Si algo no cuajó, preguntar al notebook de esa materia en NotebookLM

**Repaso espaciado (hábito nuevo, diario, 5-10 min):**
- Etiqueta review
![[Recording 20260822013833.m4a]]

![[Recording 20260822013840.m4a]]
 en notas completas (no flashcards)
- Abrir la cola del día (ícono de repaso o barra de estado "Review: N note(s)")
- Intentar recordar antes de abrir la nota
- Calificar Easy / Good / Hard según qué tan bien salió
- Qué entra a la cola: los 6 MOCs desde el inicio; después, notas que costaron al cosecharlas o que se fallaron en examen

**Quiz semanal (opcional, sin presión):**
- Sin horario fijo ni obligación — se hace cuando se acuerde y tenga ganas
- Si se hace: subir lo cosechado esa semana al notebook correspondiente, pedir un quiz corto (5-8 preguntas)

---

## Bloque 3 — Semana de parcial(es)

Ajustado al patrón real de exámenes corridos (martes, miércoles, jueves, lunes siguiente — fin de semana libre):

- La semana previa se reparte **por día según el orden real de los exámenes**, no por preferencia
- 2-3 días antes de cada examen: casi toda la cosecha se concentra en esa materia
- En cuanto pasa un examen, se brinca de inmediato a la materia del siguiente día — no revisar dos materias en paralelo
- Resolver pendientes ⚠️ de esa materia en este momento (ni antes ni después)
- Generar un simulacro de examen con NotebookLM (PDF + notas cosechadas) unos días antes — usarlo para autoevaluarse, no para releer
- Opcional: escuchar el Audio Overview (podcast) de NotebookLM los últimos 2-3 días como repaso pasivo adicional

**Justo después de cada examen:**
- Marcar `#review` de inmediato lo que se falló, mientras está fresco
- Si algún concepto cruzó materias de forma nueva, anotarlo para actualizar el MOC (aunque sea "revisar MOC de X" para hacerlo el fin de semana si no hay tiempo entre examen y examen)

---

## Plan de recuperación (para cuando se pierda el ritmo)

Regla: nunca fallar dos veces seguidas. Sin sesión de culpa, sin intentar ponerse al día con todo el backlog de golpe.

`_recuperacion.md`:
```
1. Abrir Notas en curso de la materia con el parcial más cercano
2. Cosechar UN concepto
3. Cerrar
```

Eso es la versión mínima viable — protege el hábito, no la meta original.

---

## Cierre de semestre (~fin de noviembre)

Como el procesamiento ya se hizo por parcial durante el semestre, esta pasada es ligera:

- Resolver pendientes que queden
- Actualizar los 6 MOCs con los conceptos nuevos del semestre
- Verificar enlaces rotos
- Archivar `Notas en curso.md` del semestre y crear las vacías del siguiente
- Retrospectiva de 15 min: qué hilo transversal creció, qué materia quedó débil

---

## Recordatorios rápidos

- **Puente NotebookLM → Obsidian:** destilar con tus palabras al cosechar, nunca copiar-pegar masivo. Lo único que se pega literal: diagramas, tablas, citas textuales de página del libro
- **MOC nuevo:** solo cuando un concepto ya se repitió en contextos distintos (regla práctica: la tercera vez), nunca "por si acaso"
- **Nota-cajón vs. notas separadas:** separadas por defecto; juntar solo cuando comparar entre sí es el punto (como `Puertos y conectores`)
