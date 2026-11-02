---
tipo: meta
semestre: 3
actualizado: 2026-11-02
tags: [meta, pendientes]
---

# Pendientes — semestre 3 (corte al 2 de noviembre de 2026)

Ya pasaron los primeros parciales de las cuatro materias (Enrutamiento el 8 oct, Aspectos sociales el 16 oct y Sistemas Operativos el 22 oct). Ninguna nota del vault tiene la fecha del 2.º parcial ni la de entrega del proyecto final. El cierre de semestre del [[Plan de accion - Sistema PKM semestre|plan PKM]] es el **~30 de noviembre**.

## 🔴 Entregables (cuentan para calificación)

### Enrutamiento básico — las prácticas valen 50 %
- [ ] **Práctica 8 – Protocolo RIP:** ya existe `(resuelta).docx/pdf`, pero su nota sigue diciendo «solo enunciado» y queda un lock de LibreOffice del 30 oct. Confirmar si ya la entregaste y actualizar la nota. → [[Practica 8 - Protocolo RIP]]
- [ ] **Práctica 9 – Subredes y RIP básico** (solo hay enunciado) → [[Practica 9 - Subredes y RIP basico]]
- [ ] **Práctica 10 – RIPv2 con VLSM** (solo hay enunciado) → [[Practica 10 - RIPv2 con VLSM]]
- [ ] **Práctica 11 – EIGRP básico** (enunciado + `.pka`; se vio en clase el 28 oct) → [[Practica 11 - Configuracion basica de EIGRP]]
- [ ] **Práctica 12 – Redistribución RIP y EIGRP** (solo hay enunciado) → [[Practica 12 - Redistribucion RIP y EIGRP]]
- [ ] **Práctica 13 – Redistribución con un solo router** (solo hay enunciado) → [[Practica 13 - Redistribucion con un solo router]]

### Aspectos sociales de la ciberseguridad — el proyecto final vale 50 %
- [ ] **Proyecto final: concienciación sobre deepfakes en una secundaria.** El documento va en `Borrador_v3_Deepfakes_Secundaria.docx` (13 oct), que parece completo. Falta el **producto final** (tríptico, infografía, video, juego…) y confirmar la fecha de entrega. Planteamiento en [[Aspectos sociales de la ciberseguridad/Notas en curso|Notas en curso]] (11 sep).
- [ ] **Comparativa de 3 IAM y 3 NAC (Unidad 2):** en `Alternativas IAM.pdf` están las 3 IAM, pero solo 1 de las 3 NAC (Cisco ISE). Faltan 2 NAC, si todavía no la entregaste.
- [ ] Confirmar si entregaste «Elegir 3 de los 50 sesgos», «Sector población» y «Actividad 2 – Actor escuela secundaria»: hay archivos, pero ninguna nota registra la entrega.

### Paradigmas de la programación
- [ ] **Examen parcial 1 (programa en C):** `Tareas/Examen_Parcial_1.pdf`, con struct `Persona`, `procesarBono`, `modificarDatos` y `main`. No hay ningún `.c` resuelto en el vault.
- [ ] **Ejercicios de apuntadores:** «motor de juego» (`otorgarPuntos`/`recibirDaño`) y reasignación de animales con `char**`. Están en `Tareas/Sin título 2.odt` (conviene renombrarlo) y no tienen solución.

## 🟡 Preguntar o conseguir material

### Sistemas Operativos
- [ ] Pedir la teoría de «Consideraciones para la instalación» (tema 5): apuntes o diapositivas.
- [ ] Capturar la teoría del 12 oct (operaciones con archivos en C): en [[Sistemas Operativos/Notas en curso|Notas en curso]] solo está el encabezado.
- [ ] Confirmar si hubo clase el 5 y el 8 de octubre.
- [ ] Ubicar en qué unidad va `Arquitecturas de sistemas.mp4`.

### Enrutamiento básico
- [ ] Presentación 4 (RIP): el profesor no la ha entregado y se está usando `6.4 Protocolo RIP.docx` en su lugar.

### Aspectos sociales
- [ ] Terminar el apunte del 28 oct: [[Aspectos sociales de la ciberseguridad/Notas en curso|Notas en curso]] se corta en «Sistemas operativos / P».
- [ ] Hacer la nota de la lectura «Bridging the Gap in Computer Security Warnings».

## 🔵 Cosecha de Notas en curso

Según el [[_Plan recuperacion|plan de recuperación]]: abrir la Notas en curso de la materia con el parcial más cercano, cosechar **un** concepto y cerrar. Están en orden de prioridad dentro de cada materia. Los marcados con ⚠️ **solo existen en Notas en curso**: no están ni en el temario, así que se pierden si no se cosechan. El resto ya está elaborado en el «Temario primer parcial» de la materia, que sirve como segunda fuente.

### Sistemas Operativos — [[Sistemas Operativos/Notas en curso|Notas en curso]]
- [ ] ⚠️ **Estados y ciclo de vida de un proceso** (5 estados, PCB, padre/hijo, zombie, huérfano, `fork`/`exec`): ampliar [[Gestion de procesos]] o crear una nota nueva. ← L588-634
- [ ] **Gestión de permisos en Linux** (rwx, octal, `chmod`, `chown`; meter aquí el apunte casi vacío de «Inicio de sesión»). ← L131-205
- [ ] **Protección de archivos y control de acceso** (DAC/MAC/RBAC, ACL, `setfacl`, dominios de protección). ← L538-586
- [ ] **Sistema de archivos** (definición, exFAT/FAT32/NTFS/ext4/APFS, capas, local/red/virtual). ← L209-404
- [ ] **Gestión de espacio y almacenamiento** (bloques, fragmentación, asignación contigua/enlazada/indexada, mapa de bits). ← L456-537
- [ ] **Sistemas de archivos en red** (SMB/Samba, NFS, SSHFS), o fusionarla con la anterior. ← L407-446
- [ ] **Usuarios y grupos:** al unificar [[Usuarios y gestion de usuarios]] con [[Usuarios y su gestion]], añadir los comandos (`useradd`, `usermod`, `userdel`, `groupadd`…), los archivos `passwd`/`shadow`/`group` y las funciones del SO. ← L10-129
- [ ] Antes de cosechar: desde la L449 los bloques no tienen encabezado `##`. Ponérselo a Operaciones con archivos en C, Gestión de espacio, Protección y Procesos para que funcione «Extraer selección».

### Enrutamiento básico — [[Enrutamiento basico/Notas en curso|Notas en curso]]
- [ ] ⚠️ **EIGRP** (parámetros de métrica; apoyarse en la Presentación 5 y la Práctica 11). ← L80-85
- [ ] ⚠️ **Redistribución de rutas** (RIP↔EIGRP; los comandos ya están en las prácticas 12 y 13). ← L88-93
- [ ] **FHRP / HSRP**: fue un tercio del 1.er parcial y no tiene nota propia. ← L25-33
- [ ] **Distancia administrativa** ← L10-23
- [ ] ⚠️ **Protocolos de enrutamiento dinámico: componentes, criterios y métricas** (convergencia, saltos, BW, carga, retardo…): ampliar [[Conceptos fundamentales de enrutamiento]]. ← L45-77
- [ ] Responder las preguntas abiertas del 28 oct (MD5 en routers, secuencia de un enrutador). MD5 ya está resuelto en la Práctica 13. ← L95-96
- [ ] Los bloques del 24 sep y del 1 oct están vacíos: completarlos o anotar por qué.

### Aspectos sociales — [[Aspectos sociales de la ciberseguridad/Notas en curso|Notas en curso]]
Nada está cosechado: las únicas notas de concepto, [[Comportamiento y conducta]] y [[CyBOK]], vienen de otra fuente.
- [ ] ⚠️ **Ingeniería social** (Mitnick, etapas del ataque, clasificación clásica y moderna; clase del 28 oct). ← L336-405
- [ ] **Sesgos cognitivos en ciberseguridad**: nunca se capturaron en Notas en curso; la fuente es el temario §7 y el PDF de la carpeta.
- [ ] **Modelos mentales de seguridad** (con la corrección del profesor al modelo económico). ← L9-55
- [ ] **IAM y gestión de identidad** (tipos de identidad, pilares, ciclo JML; en el apunte aparece mal como «JLM»). ← L69-150
- [ ] **Autenticación de personas** (factores, passwordless, FIDO2/passkeys, biometría, TOTP/HOTP, fatiga MFA). ← L152-247
- [ ] **NAC e identidad de dispositivos** (el temario §11 añade X.509, TPM y mTLS). ← L250-258
- [ ] **Zero Trust** ← L260-298
- [ ] **Servicios de directorio y federación** (LDAP, AD, Kerberos, Entra ID, OAuth/OIDC). ← L300-311
- [ ] **Vectores de ataque a la identidad y mitigación** (SIM swapping, credential stuffing, APT, RBAC/ABAC, ISPM). ← L315-334

### Paradigmas de la programación — [[Paradigmas de la programacion/Notas en curso|Notas en curso]]
La materia no tiene ninguna nota de concepto; todo lo que sigue es ⚠️.
- [ ] **Identificadores, tipos de datos y variables en C** (apoyarse en `Codigo/tipos-datos_identificadores_variables_alcance.c`). ← L8-34
- [ ] **Programación orientada a objetos** (abstracción, encapsulamiento, herencia, polimorfismo). ← L49-65
- [ ] **Diagrama de clases UML** (en el apunte solo hay 2 imágenes; el diagrama del zoológico sirve de ejemplo). ← L68-71
- [ ] **Ciclo de vida del desarrollo de software**: el apunte es mínimo, conviene completarlo con material de clase. ← L37-46

## 🟢 Mantenimiento del vault

- [ ] Aspectos sociales: dar nota de cierre a la matriz IAM (`Matriz_Final`) y al proyecto de deepfakes. Ninguno aparece en el índice de la materia.
- [ ] Enrutamiento: la Tarea 3 no tiene nota propia, aunque viene en el PDF combinado.
- [ ] Repaso espaciado vencido: [[Tipos de sistemas operativos]] (5 oct), [[Gestion de procesos]] (24 oct) y [[Dispositivos de entrada y salida]] (26 oct). Próximos: [[Definicion y funciones del sistema operativo]] (7 nov), [[Gestion de memoria]] (9 nov) y [[Capas de un sistema operativo]] (10 nov).
- [ ] Actualizar la lista de «Materias activas» del [[Plan de accion - Sistema PKM semestre|plan PKM]]: no incluye Paradigmas.
- [ ] Cierre de semestre (~30 nov): actualizar los MOCs, revisar enlaces rotos y archivar las Notas en curso.

### Archivos sobrantes (revisar antes de borrar)
- `Lo que no se ve WRITEUP 1.md`: duplicado exacto de [[Lo que no se ve WRITEUP]].
- Notas vacías: `Enrutamiento basico/Sin título.md` y `Paradigmas de la programacion/Sin título.md`.
- Locks de LibreOffice: `.~lock.*#` en Práctica 8 y en `Enrutamiento basico/Tareas/`.
- Duplicados en Actividades de Aspectos sociales: `Borrador_v3_…(1).docx`, `Matriz Final` frente a `Matriz_Final`, `Alternativas de soluciones IAM y…` (versión anterior a `Alternativas IAM.pdf`), `Documento sin título.pdf` y `Actividad2_…(1).pdf/.xml`.
- `Practica 3 VLSM.docx/.pdf`, que duplica `Practica 3 - VLSM.docx`.

## ⚪ Ya no aplica (para descartar)

- Todos los checklists de repaso del 1.er parcial en los tres «Temario primer parcial»: esos exámenes ya pasaron.
- Las preguntas al profesor sobre qué entraba en esos exámenes.
- [[Examen segundo parcial - Redes]]: es material del examen de junio de 2026, del semestre pasado.
- [[Proyecto final - Lineamientos]] de Probabilidad: es del semestre 2.
- [[Lo que no se ve WRITEUP]]: el CTF está resuelto y la flag fue aceptada.

## 📅 Plan de la semana (lunes 2 – domingo 8 de noviembre)

**Reglas**
- **Cosecha justo antes de practicar:** EIGRP antes de la Práctica 11, redistribución antes de la 12 y la 13, tipos en C antes del examen de Paradigmas. Así cada nota sirve en el momento.
- **Una sesión, un concepto** (20–25 min), como pide el plan de recuperación. Los 3–4 conceptos de cada día son sesiones separadas, no un bloque seguido.
- **Fechas:** si un profesor da una fecha de entrega más cercana, ese bloque se adelanta y se reacomoda lo demás.
- **Si se atrasa,** lo que puede esperar a la semana siguiente son las cosechas sin ⚠️ (ya están en los temarios) y el mantenimiento. Los entregables y los ⚠️ no.

### Lunes 2 (hoy, ~1 h)
- [ ] Mandar 4 mensajes:
  - Enrutamiento: fecha del 2.º parcial y Presentación 4.
  - Aspectos: fecha del proyecto final y del 2.º parcial.
  - Paradigmas: fecha del examen en C y de los ejercicios de apuntadores.
  - SO: diapositivas del tema 5, si hubo clase el 5 y el 8 oct, y fecha del 2.º parcial.
- [ ] Práctica 8: confirmar que está entregada, actualizar su nota y borrar el lock.
- [ ] Limpiar los archivos sobrantes (15 min).
- [ ] Cosecha ⚠️ **Ingeniería social**

### Martes 3 (~3 h) — RIP y C
- [ ] Cosecha ⚠️ **Protocolos dinámicos: componentes y métricas** → luego **Práctica 9**
- [ ] Cosecha ⚠️ **Identificadores, tipos y variables en C** → luego empezar el **examen parcial 1 de Paradigmas** (struct `Persona`, `procesarBono`)
- [ ] SO: poner los `##` que faltan en Notas en curso → cosecha ⚠️ **Estados y ciclo de vida de un proceso**
- [ ] Cosecha **Gestión de permisos en Linux**

### Miércoles 4 (~3 h)
- [ ] **Práctica 10** (RIPv2 + VLSM)
- [ ] Terminar el **examen de Paradigmas** (`modificarDatos`, `main`, compilar y probar)
- [ ] De paso con el C: escribir la teoría del 12 oct (operaciones con archivos) a partir de `operacionesArchivos.c` y el temario
- [ ] Cosechas: ⚠️ **POO**, **Distancia administrativa**, **Protección de archivos**, **Modelos mentales**
- [ ] Repaso espaciado vencido: [[Tipos de sistemas operativos]], [[Gestion de procesos]], [[Dispositivos de entrada y salida]] (20 min)

### Jueves 5 (~3 h) — EIGRP y apuntadores
- [ ] Cosecha ⚠️ **EIGRP** → luego **Práctica 11** (`.pka`)
- [ ] **Ejercicios de apuntadores** (motor de juego y zoológico con `char**`); renombrar `Sin título 2.odt`
- [ ] Cosechas: ⚠️ **Diagrama de clases UML**, **Sistema de archivos**, **IAM y gestión de identidad**

### Viernes 6 (~3–4 h) — redistribución y NAC
- [ ] Cosecha ⚠️ **Redistribución de rutas** → luego **Práctica 12** y **Práctica 13** (es el mismo tema)
- [ ] Responder las preguntas abiertas del 28 oct (MD5, secuencia de un enrutador)
- [ ] Cosecha **NAC** → con eso, añadir las **2 soluciones NAC** que faltan a la comparativa IAM/NAC
- [ ] Cosechas: **FHRP / HSRP**, **Gestión de espacio y almacenamiento**

### Sábado 7 (~4–5 h) — proyecto final de Aspectos
- [ ] Releer el `Borrador_v3`, elegir el formato del producto final y **hacerlo** (3 h). La nota de ingeniería social del lunes sirve como base.
- [ ] Notas de cierre: proyecto de deepfakes y matriz IAM; confirmar las entregas de Sesgos, Sector población y Actividad 2
- [ ] Terminar el apunte cortado del 28 oct y hacer la nota de «Bridging the Gap»
- [ ] Cosechas: **Sesgos cognitivos**, **Autenticación de personas**, ⚠️ **Ciclo de vida del software**
- [ ] Repaso espaciado: [[Definicion y funciones del sistema operativo]]

### Domingo 8 (~3 h) — cierre
- [ ] Cosechas: **Zero Trust**, **Servicios de directorio y federación**, **Vectores de ataque a la identidad**, **Sistemas de archivos en red**
- [ ] Unificar las dos notas de usuarios y cosechar en ellas **Usuarios y grupos**
- [ ] Actualizar los índices de las 4 materias (prácticas 8–13, notas nuevas) y las «Materias activas» del plan PKM
- [ ] Repasar esta nota: marcar lo hecho, pasar lo que quede a la semana siguiente y respaldar el vault en git
- [ ] *Si sobra tiempo:* nota de la Tarea 3, ver `Arquitecturas de sistemas.mp4`
