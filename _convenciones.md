---
tipo: meta
tags: [meta, convenciones, mantenimiento]
---

# Convenciones del vault

Documento de mantenimiento. Su propósito es que una pasada de reorganización futura produzca notas coherentes con las existentes, sin tener que releer todo el vault para deducir el estilo.

## Estructura

```
Materias ciberseguridad/        <- raíz del vault
├── .obsidian/
├── 00 - Indice.md              <- MOC maestro: materias por semestre + hilos transversales
├── _convenciones.md            <- este archivo
├── _adjuntos/                  <- imágenes extraídas y adjuntos nuevos
├── _plantillas/                <- Concepto.md, Clase.md
└── <Materia>/
    ├── <Materia>.md            <- índice de la materia
    ├── Notas en curso.md       <- captura sin procesar (solo semestre activo)
    ├── <Concepto>.md
    └── originales .odt / .pdf  <- se conservan, nunca se borran
```

## Frontmatter

```yaml
---
materia: <nombre exacto de la carpeta>
semestre: 1 | 2 | 3
tipo: indice | concepto | referencia | tarea | trabajo | proyecto | caso | actividad | examen | practica | captura | meta
tags: [minúsculas, con-guiones]
---
```

Campos opcionales según el caso: `profesor`, `parcial`, `modulo`, `equipo`.

## Criterio para separar una nota

Merece nota propia si cumple **al menos uno**:

- Se cita desde otra materia (el criterio más fuerte)
- Lo buscarías suelto en el buscador
- Tiene estructura interna propia (subtítulos, tablas)

**No** merece nota propia una definición corta que solo tiene sentido dentro de su tema. Ejemplo de agrupación deliberada: `Puertos y conectores` reúne diez conectores porque solo se entienden comparándose entre sí.

## Estilo de las notas

- Título H1 igual al nombre del archivo
- Tablas comparativas siempre que haya dos o más cosas que se distinguen entre sí
- Bloques `>` para citas del profesor, advertencias y correcciones
- ⭐ marca lo señalado en clase como tema de examen
- ⚠️ marca errores corregidos, datos que necesitan verificación o pendientes
- Sección final **`## Relacionadas`** con enlaces `[[ ]]`, cada uno con una frase de por qué se relaciona
- Enlazar `[[ ]]` la primera vez que aparece un concepto que tiene nota propia
- Los PDFs y binarios se enlazan con `![[archivo.pdf]]`; Obsidian los abre nativamente

## Regla de contenido

**Corregir errores de hecho, conservar el contenido del curso.** Si el apunte contradice la realidad (un cálculo mal, un término confundido), se corrige y se deja constancia visible del cambio en un bloque `>`. No se sustituye la definición que dio el profesor por otra "mejor" si ambas son correctas — en el examen se califica la suya.

## Hilos transversales

Mantener actualizada la sección correspondiente de `00 - Indice.md`. Los hilos vivos son: tríada CIA, ciclo de gestión de seguridad, factor humano, direccionamiento IP, hardware→SO, matemáticas→redes. Cuando un tema nuevo se enganche a uno de ellos, añadirlo a la cadena.

## Procedimiento de la pasada de fin de semestre

1. Verificar que `Notas en curso.md` de cada materia esté vacío o solo con enlaces; procesar lo que quede
2. Dividir en notas por concepto según el criterio de arriba
3. Frontmatter y `## Relacionadas` en cada nota nueva
4. Enlazar hacia atrás: buscar conceptos de semestres anteriores que el material nuevo retome
5. Actualizar el índice de la materia y los hilos transversales de `00 - Indice.md`
6. Verificar que no haya enlaces `[[ ]]` rotos
7. Archivar `Notas en curso.md` de las materias que terminaron; crear el de las nuevas
