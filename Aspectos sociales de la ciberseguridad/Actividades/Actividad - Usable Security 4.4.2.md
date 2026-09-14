---
materia: Aspectos sociales de la ciberseguridad
semestre: 3
tipo: actividad
tags: [ciberseguridad, usable-security, usabilidad, factor-humano, desarrolladores]
---

# Actividad — Usable Security 4.4.2

> ⚠️ El numero de actividad esta sin confirmar: en esta carpeta ya hay una `Actividad2_Actor_Escuela_Secundaria`, asi que esta no es la 2.
> Entregables, en esta misma carpeta:
> ![[Actividad - Usable Security 4.4.2.docx]] · ![[Actividad - Usable Security 4.4.2.pdf]] — documento de respuestas
> ![[Presentacion - Usable Security 4.4.2.pptx]] · ![[Presentacion - Usable Security 4.4.2.pdf]] — presentacion
> ![[Actividad - Usable Security 4.4.2 - caracteristicas de los usuarios.docx]] — borrador suelto de la pregunta 2

Lectura y analisis por equipos de una seccion de la revision sistematica **Di Nocera, F.; Tempestini, G.; Orsini, M., "Usable Security: A Systematic Literature Review", *Information* 2023, 14(12), 641** (https://www.mdpi.com/2078-2489/14/12/641). La revision selecciona 55 estudios publicados entre 2005 y 2022 y los agrupa en cuatro clusteres.

**Seccion asignada: 4.4.2 — Ayudar a los desarrolladores de seguridad a mejorar la usabilidad** (7 articulos, aunque el texto solo desarrolla seis referencias: [42] a [47]).

La captura previa de la lectura esta en [[USABLE SECURITY A SYSTEMATIC LITERATURE REVIEW]]; este documento es la version entregada.

## El principio que gobierna la seccion

Cuanto mas seguros son los sistemas, menos usables resultan — y al reves. La seccion 4.4.2 se pregunta como cerrar esa brecha **desde el lado de quien construye el software**, no de quien lo usa. Es lo que la distingue de las otras tres secciones de la revision.

## Los seis estudios

| Ref. | Autores | Aporte |
|---|---|---|
| [42] | Flechais y Sasse | Diseno participativo de seguridad en plataformas de e-ciencia |
| [43] | Alsharnouby et al. | Por que el phishing sigue funcionando: estrategias del usuario |
| [44] | Roth et al. | Correo electronico seguro no intrusivo, con cifrado transparente |
| [45] | Gorski et al. | Informacion de seguridad dentro de la documentacion de APIs |
| [46] | Dhillon et al. | Objetivos basados en valores para equilibrar seguridad y usabilidad |
| [47] | Alemerien | Patrones de GUI para sitios de redes sociales |

## 1. Estrategias y mecanismos de seguridad usable

- **Ubicar la seguridad donde el desarrollador mira** [45] — incluir la informacion de seguridad en la documentacion de APIs y colocarla junto al codigo funcional, como comentarios que remitan al capitulo correspondiente
- **De "orientado al codigo" a "orientado a conceptos"** [45] — no pelear contra el habito de ir directo al ejemplo, sino aprovecharlo; el principio aplica a cualquier herramienta de desarrollo
- **Content Security Policy (CSP)** — politica del navegador que define que puede ejecutarse (scripts, estilos, imagenes, iframes, conexiones); es el mecanismo concreto sobre el que el estudio mide todo lo demas
- **Patrones y modelos de GUI con la seguridad como eje** [47] — la clave es la retroalimentacion adecuada, que la interfaz ayude a decidir de forma informada
- **Interfaces claras contra el phishing** [43] — ayudan, pero no son determinantes: el reconocimiento depende de la capacitacion previa
- **Correo seguro no intrusivo** [44] — cifrado automatico y transparente, evitando infraestructuras de clave publica y separando el intercambio de claves de su vinculacion a identidades
- **Diseno participativo con las partes interesadas** [42] — mecanismo organizativo, no tecnico: motivacion, responsabilidad, comunicacion y partes interesadas
- **Traducir conceptos abstractos en criterios medibles** [46] — cuatro objetivos: facilidad de uso, comunicacion, estandarizacion e integracion, y capacidad del sistema

## 2. Caracteristicas de los usuarios involucrados

**Desarrolladores.** No son un grupo homogeneo (web, navegadores, sistemas, correo, academia) ni tienen la misma experiencia — el estudio de Gorski et al. trabajo con 49 desarrolladores noveles. Van directo al codigo de ejemplo e ignoran comentarios y descripciones. Sin indicaciones visibles de seguridad tienden a **eliminar** el fragmento conflictivo en lugar de corregirlo. Perciben la usabilidad como secundaria y consultar a especialistas como perdida de tiempo. Su motivacion sube cuando se les asignan responsabilidades concretas.

**Usuarios finales.** Muestran interes genuino en proteger su informacion y prefieren interfaces con mas opciones de seguridad y privacidad. Priorizan satisfaccion, facilidad de aprendizaje y simplicidad. Son casi ciegos a los indicadores tecnicos (URLs incorrectas, direcciones IP en lugar de dominios) pero distinguen bien lo legitimo de lo sospechoso **por contexto**. Prefieren soluciones simples, automaticas y no intrusivas.

⭐ Esta es la conclusion transversal de la seccion: **los usuarios leen el contexto, no los indicadores tecnicos**. Se conecta directamente con [[Comportamiento y conducta]].

## 3. Parametros con que se mide la usabilidad

No existe un conjunto comun de metricas — cada estudio definio las suyas, y esa dispersion es una de las criticas que el propio articulo formula.

- **Gorski et al. [45]** — tasa de exito en cuatro tareas de programacion, seguimiento ocular (eye-tracking), y calidad del producto final en dos ejes simultaneos (que el codigo funcione y que quede protegido con CSP), contra un grupo de control con la documentacion original de Google
- **Alemerien [47]** — cuatro tareas (solicitud de aplicacion, solicitud de amistad, compartir fotos, lista de amigos) y cinco factores por tarea (satisfaccion, facilidad de aprendizaje, actitudes, interactividad, privacidad) en escala Likert de 1 a 5, contra la interfaz real de Facebook

## 4. Resultados

Los datos de phishing de **Alsharnouby et al. [43]** son los mas ilustrativos:

| Escenario | Resultado |
|---|---|
| Sitio bancario falsificado con URL incorrecta | En general **no** reconocieron la URL |
| PayPal con direccion IP en lugar de URL | Solo el 38 % lo noto |
| Chrome falso | 62 % lo reconocio |
| Ventanas emergentes pidiendo credenciales | 38 % cayo |
| Ventanas emergentes superpuestas (doble URL) | 62 % lo reconocio |
| Fraude contextual ("Credit Card Checker") | 95 % lo reconocio |
| Sitios legitimos | Altas tasas de acierto |

Lectura general: **la interfaz ayuda; la capacitacion es la que decide.**

Los demas: Roth et al. [44] dejan abiertas tres lineas (verificacion de claves usable, mejores metricas de seguridad por interaccion, incentivos desde la propia interfaz). Flechais y Sasse [42] concluyen que asignar responsabilidades aumenta notablemente la motivacion y que los metodos basados en escenarios se ajustan mejor a como la gente habla de seguridad. Dhillon et al. [46] entregan sus cuatro objetivos como guia de implementacion.

## 5. Areas de oportunidad

- **Falta de una metodologia comun** — el problema central: sin ella no se pueden replicar los estudios ni estandarizar el enfoque
- **Recomendaciones sin respaldo empirico real** — varias se parecen mas a reflexiones organizativas (asignar responsabilidades, hacer el proceso participativo) que a hallazgos
- **Se confunde "facilidad de uso" con "usabilidad"** — se pide simplificar el diseno sin definir que significa en concreto
- **Ni las recomendaciones especificas se salvan** — las de Alsharnouby et al. tampoco derivan de trabajo empirico sistematico
- **El hallazgo de Gorski et al. esta subaprovechado** — se probo solo en documentacion de APIs y aplica a cualquier herramienta
- **La capacitacion del usuario queda fuera del alcance del diseno** — ningun estudio del grupo la aborda, pese a que los datos de phishing la senalan como determinante
- **Ausencia de requisitos de seguridad usable** en los contextos de desarrollo, lo que desincentiva las buenas practicas desde el inicio
- **Faltan metricas estandarizadas de "seguridad por interaccion"**, senalado por Roth et al.

## Relacionadas

- [[USABLE SECURITY A SYSTEMATIC LITERATURE REVIEW]] — la captura de lectura de la que salio esta entrega
- [[Comportamiento y conducta]] — el marco de la materia sobre por que la gente decide como decide frente a la seguridad
- [[Actividad 1 - Buenas practicas de ciberseguridad]] — la actividad anterior, sobre el mismo factor humano desde la experiencia propia
- [[Aspectos sociales de la ciberseguridad]] — indice de la materia
