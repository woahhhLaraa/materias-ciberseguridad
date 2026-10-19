---
materia: Aspectos sociales de la ciberseguridad
semestre: 3
tipo: temario
fecha-examen: 2026-10-16
parcial: 1
tags: [examen, parcial, factor-humano, gestion-de-identidad]
---

# Temario — primer parcial de Aspectos sociales de la ciberseguridad

**Examen: viernes 16 de octubre de 2026.** Vale el 30 % de la materia. Se exenta con 7 si se tiene el 90 % de las actividades.

Abarca la **Unidad 1** (comportamiento humano) y la **Unidad 2** (gestión de identidad). Está armado con las dos presentaciones de la profesora Domínguez Bárcenas, la lectura de sesgos, el programa, las [[Aspectos sociales de la ciberseguridad/Notas en curso|Notas en curso]] y las actividades.

> ⚠️ **Alcance por confirmar.** El programa no divide los temas por parcial. Supongo que entran las Unidades 1 y 2 porque son las dos que se han visto en clase. La ingeniería social está en el programa, pero todavía no se ha dado; solo aparece como vector de ataque en la Unidad 2.

**Formato** (programa, sección 22): el examen tiene reactivos y **preguntas abiertas en las que se califica la argumentación**. Por eso no basta con memorizar listas. Hay que poder explicar *por qué* (por ejemplo, por qué falla una política o qué modelo mental conviene usar con qué público).

## Temario oficial (saberes del programa)

El programa no habla de unidades, solo de «saberes». Así encajan con este temario:

| Saber del programa | Unidad | Dónde está aquí |
|---|---|---|
| Introducción al comportamiento humano en ciberseguridad | 1 | Tema 1 |
| Contextos de comportamiento humano | 1 | Temas 1 y 3 |
| Seguridad usable | 1 | Temas 2 y 3 |
| Error humano | 1 | Tema 4 |
| Consciencia de ciberseguridad | 1 | Temas 5, 6 y 7 |
| Gestión de identidad | 2 | Temas 8 y 9 |
| Identificación y autenticación de personas y dispositivos | 2 | Temas 10 y 11 |
| Servicios de manejo de identidad | 2 | Temas 12 y 13 |
| Mitigación de riesgos | 2 | Tema 14 |

⭐ Uno de los saberes heurísticos dice **«explicar la diferencia entre identificación, autenticación y autorización»**. Tiene pinta de pregunta abierta. Está resuelto en el tema 10.

---

# Unidad 1 — Introducción al comportamiento humano en ciberseguridad

## 1. Punto de partida: CyBOK, comportamiento y conducta

Ver [[CyBOK]] y [[Comportamiento y conducta]].

- **CyBOK** (*Cyber Security Body of Knowledge*): «codificar los conocimientos fundamentales y generalmente reconocidos sobre ciberseguridad». Sirve de guía para diseñar programas educativos. Se basa en libros de texto, artículos, reportes técnicos, *white papers* y normas.
  - Define **21 áreas de conocimiento**, agrupadas en las **5 grandes categorías** de la clase: *systems*, *infrastructure*, *software and platform*, *human, organizational and regulatory aspects* y *attacks and defences*.
  - El curso trabaja la de factores humanos (Sasse y Rashid, *Human Factors*, el primer libro de la bibliografía).
- **Comportamiento:**
  - «Manera de comportarse». También: «conducta dentro de un espacio y un tiempo determinado» (UNIR).
  - Lerner et al. (2024): «potencial y capacidad expresada para la actividad física, mental y social durante las fases de la vida humana».
  - Lo influyen factores internos y depende del contexto.
- **Conducta:**
  - «Respuesta a una motivación» (UNIR).
  - Arnal (2020): un proceso de tres pasos.
    1. Interpretar el estímulo.
    2. Integrarlo con la experiencia y la situación del sujeto.
    3. Seleccionar y ejecutar acciones.
  - «Toda conducta se concibe dentro de un contexto, tanto natural como construido».
- **Contextos:** «para comprender por qué una persona se comporta de cierta manera, es necesario entender el contexto en el que se encuentra inmersa».
  - **Físico:** estímulos ambientales (anuncios, entornos verdes, contaminación, tráfico).
  - **Social:** la organización (roles, normas, valores, modelos) y los compañeros (personalidad, actitudes, motivación).
- **Definición de ciberseguridad** (diapositiva 10): protección de los sistemas de información (hardware, software e infraestructura), de sus datos y de sus servicios frente al acceso no autorizado, el daño o el uso indebido. **Incluye el daño intencional del operador y el accidental por incumplir procedimientos.** Esa última frase es la que mete al ser humano en la definición.

## 2. Principios de diseño y por qué no se adoptan las medidas

| Año | Autor | Principio |
|---|---|---|
| **1883** | Auguste Kerckhoffs | Un sistema seguro «debe ser fácil de usar y no debe exigir tensión mental ni el conocimiento de una larga serie de reglas» |
| **1975** | Saltzer y Schroeder | **Psicología:** mecanismos psicológicamente aceptables. **Factores humanos:** el menor número posible de mecanismos distintos. **Economía del crimen:** superar la medida debe costar más que lo que gana el atacante |

**¿Por qué no se adoptan las medidas de seguridad?** (diapositiva 12)
- Se trata a las personas como **componentes** que se controlan con políticas.
- El profesional de seguridad ve al usuario como alguien que no entiende o es «perezoso».
- El usuario vive una **disyuntiva**: hacer lo seguro o ser productivo.
- La respuesta habitual, concienciar y educar, es **«adaptar al ser humano a la tarea»**. La seguridad usable propone lo contrario: **«adaptar la tarea al ser humano»**.

## 3. Seguridad usable

Ver [[Actividad - Usable Security 4.4.2]].

- **Usabilidad** (**ISO 9241-11:2018**): «eficacia, eficiencia y satisfacción con la que usuarios específicos logran objetivos específicos en entornos particulares».

| Componente | Definición ISO |
|---|---|
| Eficacia | Exactitud e integridad con que se alcanzan los objetivos |
| Eficiencia | Recursos empleados en relación con esa exactitud e integridad |
| Satisfacción | Comodidad y aceptabilidad del sistema para los usuarios y los afectados |

- **Seguridad usable:**
  - NCSC (Reino Unido): «la forma de crear una seguridad que funcione es crear seguridad que funcione para las personas».
  - Di Nocera et al. (2023): medidas diseñadas según las necesidades, habilidades y comportamiento del usuario, para minimizar errores y aumentar el cumplimiento.
  - **Actores:** usuarios finales, administradores y desarrolladores.
  - **Metas:** adaptar la tarea al humano, reducir el error y reducir el tiempo invertido.
- ⭐ **Cuatro factores para adaptar la tarea al ser humano** (diapositiva 16). Organizan el resto de la unidad.

| Factor | Ideas clave |
|---|---|
| **Capacidades y limitaciones del usuario** | Atención a una tarea a la vez → **fatiga por alarma**. Memoria de corto plazo (OTP) y de largo plazo (lo frecuente y lo emocional se recuerda mejor). **El problema de las contraseñas:** demasiadas credenciales, reglas distintas y contraseñas viejas que compiten → contraseñas predecibles. **Necesidades adicionales:** niños, adultos mayores, discapacidad, daltonismo, epilepsia, cultura. **Caso CAPTCHA** (7 tipos: texto distorsionado, imágenes, rompecabezas, matemáticas, audio, invisibles, de comportamiento) |
| **Objetivos y tareas** | Tareas **primarias o de producción** vs **habilitadoras** (la seguridad es habilitadora). Tarea frecuente = automática; poco frecuente = consciente. **Fatiga de seguridad:** la tarea de seguridad pide más tiempo del que el usuario está dispuesto a dar → apunta contraseñas, guarda copias sin cifrar, usa un *mouse jiggler*. Remedio: **auditoría de la carga de trabajo** antes de elegir una medida |
| **Contexto físico y social** | Físico: luz (reflejos, cámaras de rostro o iris), ruido (voz), temperatura (sensores, guantes, sudor), contaminación (sensores, marcas en pantallas táctiles). Social: valores, normas y confianza. Se investiga con **indagación contextual**: observar, entrevistar, ver qué motiva |
| **Capacidades del dispositivo** | En el teclado del móvil, las contraseñas complejas cuestan → se eligen fáciles de teclear. Los tokens 2FA confunden: son pequeños y cada banco los nombra distinto. Tener en cuenta la **ergonomía** |

- **Ejemplos para argumentar:**
  - La empleada que vuelve de vacaciones y tarda 20 minutos en restablecer su contraseña: la tarea habilitadora interrumpe la de producción.
  - **Operación normal vs intervención puntual:** un solo inicio de sesión para el trabajo diario, y MFA solo ante algo inusual (red pública, descarga atípica).
- **Lectura Di Nocera et al. (2023):** revisión de 55 estudios publicados entre 2005 y 2022, agrupados en 4 clústeres:
  1. Usabilidad de la autenticación.
  2. Ayudar a los desarrolladores.
  3. Diseño para influir en el comportamiento.
  4. Modelos formales.
  - Tu sección (4.4.2) concluye que **los usuarios leen el contexto, no los indicadores técnicos**: la interfaz ayuda, pero lo que decide es la capacitación.

## 4. El error humano

- **James Reason:** «todos los errores que cometen las personas son predecibles».

| Tipo de fallo | Qué es | Ejemplo |
|---|---|---|
| **Latente** | Condiciones de la organización y del lugar de trabajo | Conflicto entre la tarea principal y la de seguridad |
| **Activo** | Violaciones de las personas | No seguir el procedimiento |

- ⭐ **Modelo del queso suizo:**
  - Las rebanadas son las **defensas** (mecanismos y políticas) y los agujeros, las **fallas latentes y activas**.
  - El incidente ocurre cuando los agujeros se alinean y la amenaza atraviesa todas las capas.
  - Quien hizo clic es solo el último eslabón: «este incidente ha estado precedido por varios otros fallos que han llevado a esa persona a una situación en la que lo que parecía ser la decisión correcta resultó ser la equivocada».
  - Hay que **notificar los cuasi accidentes**.
- **Daniel Kahneman:**
  - **Pensamiento rápido:** tareas frecuentes y automáticas, la mayoría. Necesita herramientas de apoyo, por ejemplo para distinguir el phishing.
  - **Pensamiento lento:** tareas nuevas o poco frecuentes, conscientes.
  - Frase de los expertos: «sin considerar la productividad, **modo lento = modo seguro**».
- **Fallos latentes que generan errores** (tabla de la diapositiva 39):

| Individuales | Humanos | De la tarea | Del ambiente de trabajo |
|---|---|---|---|
| Fatiga, inexperiencia, actitud de riesgo | Límites de memoria, hábitos, creencias compartidas («la seguridad es cosa de TI», «no tengo nada de valor») | Presión de tiempo, multitarea, carga alta, monotonía, roles poco claros | Interrupciones, equipo o información deficiente, cambio de normas |

## 5. Consciencia de ciberseguridad y cambio de comportamiento

- **Douglas MacArthur:** «nunca emitas una política de seguridad que no se pueda cumplir». Si no se cumple porque es imposible, se rediseña.
- **Ciberhigiene** (Irel, 2023): «conjunto de prácticas de las organizaciones y de las personas, realizadas regularmente para mantener la salud y seguridad de los usuarios, dispositivos, redes y datos», y para recuperarse de un ataque.
  - Las políticas imposibles generan duda, resentimiento y una actitud negativa hacia la seguridad y la organización.

| Estrategia | Qué busca |
|---|---|
| **Concienciación** | Captar la atención y convencer: riesgos reales y capacidad de actuar. Pide especialistas en comunicación |
| **Educación** | Informar de riesgos y medidas. Pide disposición a aprender |
| **Formación** | Adquirir habilidades con práctica: usar los mecanismos, reconocer y responder a un ataque, reflexionar sobre los propios sesgos |

- **Cambio de comportamiento:**
  - Saber qué hacer **no basta**: el comportamiento nuevo tiene que instalarse en la memoria de largo plazo y competir con el que ya existe.
  - Es gradual: uno o dos comportamientos a la vez, sin detener la producción.
- **Modelo RISCS (Reino Unido, 2015):** confianza en el compromiso del personal, asignación de roles (dar identidad a la seguridad) y cumplimiento en todos los niveles.
- ⭐ **Modelo de Fogg** (BJ Fogg, Stanford): **comportamiento = motivación + capacidad + disparador (*prompt*)**.
  - Ejemplo de disparador de motivación: el fondo de pantalla «¿Y si hay alguien mirándote?».
  - Ejemplo de disparador que facilita la acción: el botón «Sí, soy yo» del 2FA.
- **Estrategias de concienciación:**
  - **Simulaciones antiphishing:** miden y enseñan, pero pueden minar la confianza en la organización («auto ataque»).
  - **CTF**, para el personal técnico.
  - **Juegos de mesa:** Ctrl-Alt-Hack, dox3d!, Elevation of Privilege (Microsoft) y Decisions and Disruptions. Deben formar parte de un programa planificado.

## 6. Modelos mentales

- **Modelo mental** (UOC): «nuestros modelos conceptuales acerca de cómo funcionan los objetos, cómo tienen lugar los hechos o cómo se comporta la gente».
  - Pueden ser de **tarea y acción** (manejar) o **estructurales** (diagnosticar).
  - El usuario con un modelo inadecuado cree que su comportamiento no lo hace vulnerable, y no se esfuerza.
- **Camp (2009):** comunicar el riesgo exagerándolo o con puros datos técnicos no funciona. La propuesta es usar **metáforas** que aprovechen los atajos mentales que la gente ya tiene.

| Modelo | La idea | Ventaja | Limitación |
|---|---|---|---|
| **Seguridad física** | Puertas, cerraduras, perímetros | Intuitivo: motiva contraseñas fuertes y bloquear el equipo | Lo digital se copia sin presencia física y un cable atraviesa paredes. El control es local |
| **Médico** | El ataque es una enfermedad que se contagia. Ejemplo: el gusano **Blaster** y el «gusano bueno» **worm_blastMS**, que parchaba | **Higiene digital**; responsabilidad individual y colectiva; todos están en riesgo | Hay que respetar la autonomía (rechazar el «tratamiento»), aunque arriesgue a la comunidad |
| **Guerra** | Enemigo persistente: perímetro, vigilancia, inteligencia, defensa en capas | Prepara para una respuesta activa | Usa el miedo. **Quita la responsabilidad individual** («que se encarguen los expertos») y empuja a un control centralizado que choca con un internet abierto |
| **Económico o de mercado** | Costos, beneficios, terceros, contratos e incentivos o castigos | Pone precio a la negligencia (tu equipo vulnerable se usa para atacar a otros) | Atención excesiva a ciertas vulnerabilidades, desatención de otros riesgos y costos difíciles de asignar en entornos compartidos |

> ⚠️ Corrección a las notas de clase. En el modelo económico, la limitación anotada como «paranoia (a la gente le preocupa demasiado el dinero)» en la diapositiva es «**atención excesiva a ciertas vulnerabilidades**». Los gusanos del modelo médico tienen nombre: Blaster y worm_blastMS.

⭐ **Conclusión** (pregunta abierta probable): ningún modelo es mejor que los demás. Se **elige según el público** para que la gente actúe informada sin depender del todo de los expertos.

## 7. Sesgos cognitivos

- **Definición** (Clínica U. de Navarra): «tendencia sistemática de pensar de manera distorsionada debido a la interpretación sesgada de la información disponible».
  - García-Campos et al. (2022): también se llaman ilusiones cognitivas. Son procesamientos imprecisos y mayormente involuntarios.
- **Las 4 características de las ilusiones cognitivas:**
  - a) difieren de la realidad;
  - b) se desvían **sistemáticamente**, no al azar;
  - c) son **involuntarias**;
  - d) son **difíciles de evitar**.
- **Origen:**
  - El límite de información que podemos procesar (el conocimiento está en las comunidades, no en una sola cabeza).
  - «Aprender lleva tiempo, corregir requiere esfuerzo».
  - **Representatividad:** «estudió filosofía → es feminista».
  - **Frecuencia:** «la tercera es la vencida».
  - ⚠️ Los sesgos **no se eliminan con incentivos ni pidiendo atención; «no cambian con la educación»**. Por eso se diseñan controles a su alrededor.

**Los 10 de la presentación:**

| Sesgo | En ciberseguridad |
|---|---|
| Heurística afectiva | Si algo da buena impresión, se percibe de bajo riesgo |
| Anclaje | El directivo prioriza una amenaza y todos lo siguen sin ver el panorama |
| Heurística de disponibilidad | Se decide por lo que se recuerda o está de moda, no con método |
| Racionalidad limitada | Se busca «satisfacer», no optimizar: decisiones «suficientemente buenas» |
| Sobrecarga de opciones | El marketing de productos de seguridad confunde → se implanta la solución equivocada |
| Fatiga por toma de decisiones | Tantas alertas que se ignoran |
| Comportamiento gregario | Si un grupo pega contraseñas en *post-its*, se contagia |
| Efecto de la autoconfianza | «Ya destruí los documentos confidenciales» → luego hace clic en el phishing |
| Sesgo de optimismo | «A mí no me va a pasar» |
| Agotamiento del ego | La fuerza de voluntad se agota: sin recordatorios se pierde el hábito |

**Los 5 de la lectura** ([[Sesgos cognitivos en ciberseguridad.pdf]]):
- **Confirmación:** el analista decide que la alerta del SIEM es un falso positivo e ignora los IoC.
- **Autoridad:** BEC o *spear phishing* con un correo «del CEO».
- **Optimismo:** «nuestra red no es interesante» → VLAN plana y nada de Zero Trust.
- **Anclaje:** remediar solo el primer vector descubierto (RDP) e ignorar la persistencia.
- **Dunning-Kruger:** «soy demasiado listo para caer».

La lectura explica que los atacantes activan **urgencia, miedo, codicia y curiosidad** para «apagar» el pensamiento analítico.

**Cómo superarlos** (diapositiva 67): priorizar la **psicología sobre la tecnología**, **defensa en profundidad** (técnica + capacitación + procedimientos) y **comunicación y formación periódicas**.

---

# Unidad 2 — Gestión de identidad

## 8. IAM e identidad digital

- **Red corporativa moderna:**
  - **Usuarios humanos:** empleados, clientes, contratistas y terceros.
  - **Usuarios no humanos:** agentes de IA, IoT, *endpoints* y cargas de trabajo automatizadas.
- **IAM** (*Identity and Access Management*): «disciplina de ciberseguridad que se ocupa del aprovisionamiento y protección de identidades digitales y permisos de acceso a los usuarios de un sistema de TI».
  - Garantiza el acceso seguro.
  - Bloquea amenazas: atacantes externos, internos malintencionados e internos bienintencionados que abusan de sus derechos.
- **Identidad digital:** «combinación de atributos y credenciales que representan a una persona o entidad en el mundo digital».
  - Componentes: usuario y contraseña, correo, biometría, historial de navegación y perfiles.
  - Es la base de la autenticación y la autorización.

| Tipo de identidad | Qué es | Ejemplo |
|---|---|---|
| Humana | Atributos de una persona | Cuenta bancaria en línea |
| De máquina | Apps, bots, IoT; se autentican con certificados o tokens | Una app que consulta una base de datos en la nube |
| **Federada** | Una identidad para muchos servicios | «Iniciar sesión con Google» en Spotify o Canva |

- **Métodos de verificación:** credenciales, biometría y certificados. Reducen el fraude y el robo de identidad.
- **Casos de uso:** finanzas, salud, gobierno, comercio electrónico, viajes y educación, juegos en línea.

⭐ **Los 4 pilares de la IAM:**

| Pilar | Qué hace |
|---|---|
| **Administración** | Crear, mantener y eliminar identidades (el ciclo de vida) |
| **Autenticación** | Verificar que el usuario es quien dice ser, comparando sus factores con la base de datos |
| **Autorización** | Dar al usuario verificado el nivel de acceso adecuado: **RBAC** y **mínimo privilegio** (el analista junior ve, el administrador modifica, el CISO tiene todo) |
| **Auditoría** | Registrar qué hace cada quien con sus permisos |

## 9. Ciclo de vida de la identidad: JML

> ⚠️ En las notas aparece como «JLM». El orden correcto es **JML: Joiner, Mover, Leaver** (alta, cambio, baja).

| Fase | Pasos |
|---|---|
| **Joiner** (alta) | 1. Crear la identidad (datos de RH; SSO y MFA; tipo de trabajador). 2. *Preboarding*: paquete básico y dispositivos. 3. Asignar roles y grupos. 4. Aprovisionar. 5. Verificar y revisar accesos |
| **Mover** (cambio) | 1. Seguir la transferencia interna. 2. Asignar roles nuevos. 3. Aprobación según el riesgo. 4. **Quitar los accesos previos**, empezando por lo sensible. 5. Aprovisionar lo nuevo. 6. Recertificar |
| **Leaver** (baja) | 1. Disparar el evento de salida (RH → TI). 2. Desactivar cuentas y cerrar sesiones. 3. Revocar accesos, sobre todo los privilegiados. 4. Transferir la propiedad de los datos. 5. Recuperar hardware y licencias. 6. Generar el registro de auditoría. 7. Confirmar que no quede nada activo |

**Cuatro pilares de la gestión del ciclo de vida** (otra clasificación, más general):
1. **Aprovisionamiento.**
2. **Gestión y modificación de accesos**, con el principio de mínimo privilegio.
3. **Seguimiento y auditoría:** cuentas fantasma y usuarios inactivos con privilegios.
4. **Desabastecimiento** (desaprovisionamiento).

## 10. Autenticación de personas

⭐ **Identificación, autenticación y autorización** (saber del programa):
- **Identificación:** decir quién eres; por ejemplo, el nombre de usuario.
- **Autenticación:** demostrarlo con un factor.
- **Autorización:** qué se te permite hacer una vez verificado.
> Las diapositivas definen autenticación y autorización. La identificación no viene definida explícitamente; la del párrafo es la definición estándar.

| Factor | Es algo que… | Ejemplos |
|---|---|---|
| Conocimiento | sabes | Contraseña, preguntas de seguridad |
| Posesión | tienes | OTP, token, clave privada, *magic link* |
| Inherente | eres | Biometría estática |
| Comportamiento | haces | Patrón de escritura, mouse, firma, voz |

- **Contraseñas:** el método más común. Se roban (phishing, malware), se adivinan (fuerza bruta) o se filtran (*dark web*).
  - **Dato:** el robo de cuentas válidas estuvo en el **32 %** de los ataques (IBM X-Force 2025).
  - Las preguntas de seguridad se descubren con ingeniería social o en redes sociales.
- **Passwordless:** usa factores difíciles de robar o falsificar.
- **FIDO / FIDO2 y *passkeys***:
  - **FIDO** = *Fast Identity Online*: estándares abiertos de la FIDO Alliance (IBM, Apple, Amazon, Microsoft, PayPal).
  - La **clave pública** la tiene el servicio. La **privada** se queda en el dispositivo, nunca se comparte y se protege con un PIN o biometría.
  - **Flujo:**
    1. El servicio envía un desafío.
    2. El usuario desbloquea la clave privada y firma el desafío.
    3. El servicio verifica la firma con la clave pública.
    4. Se concede el acceso.
- **Biometría** (*bio* = vida, *metric* = medir):
  - **Estática:** huella, geometría de la mano, iris, retina.
  - **Dinámica:** firma, voz.
  - **Desafíos:** falsos positivos y negativos; si es muy estricta, rechaza a usuarios legítimos; si es muy laxa, acepta a impostores; las plantillas deben almacenarse de forma segura.
  - **Inhibidores:** privacidad, poca aceptación, miedo a la salud o a la higiene, rastreo, y que revele información (la retina puede delatar enfermedades cardiovasculares).
  - **Componentes:** sensores, software, almacenamiento y transmisión.
- ⭐ **Los 7 requisitos de un método biométrico:** universalidad, singularidad, permanencia, coleccionabilidad, rendimiento, aceptabilidad y elusión (que no sea fácil engañarlo).
- **OTP:**
  - Es factor de **posesión**, no de conocimiento: es de corta duración y se genera una nueva en cada inicio.
  - Se genera con un token de hardware, una app o un SMS.

| | TOTP (*time-based*) | HOTP (*hash-based*) |
|---|---|---|
| Se basa en | La hora actual y un secreto compartido (se recibe al escanear un QR) | Un **HMAC** y un contador de solicitudes |
| Cambia | Cada 30–60 s | Cada vez que se solicita |

> ⚠️ En las notas está escrito «TOPT». Es **TOTP**.

- **Otros métodos:**
  - **Token de hardware:** un *dongle* USB; es caro emitir uno por persona.
  - **Magic link:** un enlace con token de un solo uso, que prueba que se posee el correo.
  - **Push:** aprobar en el móvil. ⚠️ Es vulnerable a la **fatiga MFA** («bombardeo MFA»): el atacante pide la aprobación una y otra vez hasta que la víctima acepta por error o por cansancio.
  - **Código QR:** transferencia de sesión; el móvil ya autenticado aprueba la sesión pendiente.
- **MFA:** «sistema de seguridad de varias capas… **requiere al menos 2 factores**». Factor 1, conocimiento; factor 2, posesión o inherencia.

## 11. Identidad de dispositivos y NAC

- **Por qué importa:** IoT, **OT** (tecnología operativa: controla procesos físicos e industriales) y equipos con datos sensibles.
  - **Superficies de ataque:** puertos abiertos sin uso, intercambio de datos (MITM), servicios en la nube.

| Método | En una línea |
|---|---|
| **Identificador** | IMEI asociado a la SIM |
| **Certificado X.509** | Vincula un par de claves con una identidad. Lo emite una **CA** dentro de una **PKI** (hardware, software, políticas y estándares) |
| **TPM** | Chip criptográfico resistente a la manipulación: clave **RSA** grabada, mide la integridad del arranque y limita intentos (contra ataques de diccionario) |
| **mTLS** | TLS en el que **también el cliente** presenta certificado |

- **Componentes de un certificado:** entidad, clave pública, emisor y su firma, número de serie, vigencia y algoritmo. Lo firma la clave privada de la CA.
- **Tipos de certificado:**

| Tipo | Para qué | Ejemplo |
|---|---|---|
| TLS/SSL | Cifrar web (https y candado) | Banco en línea |
| — *Wildcard* | Todos los subdominios | `*.miempresa.com` |
| — SAN / multidominio | Dominios distintos | miempresa.com y tienda.miempresa.es |
| — EV | Validación rigurosa de la organización | Entidad financiera, gobierno |
| Firma de código | El software no fue alterado (se compara el hash) | Actualización de Windows |
| S/MIME | Firmar y cifrar correo | Correo corporativo confidencial |
| De cliente | Autenticar a un usuario o máquina ante el servidor | VPN empresarial |
| Educativo | Credencial firmada por la institución | Título universitario |

- **Handshake TLS:**
  1. El navegador pide la identidad.
  2. El servidor manda su certificado.
  3. El navegador lo comprueba contra sus CA de confianza.
  4. Crea una clave de sesión y la cifra con la clave pública del servidor.
  5. El servidor la descifra con su clave privada.
  6. Queda establecido el canal cifrado.
- **NAC** (control de acceso a la red): «proceso de restringir el acceso de usuarios y dispositivos no autorizados a una red informática corporativa».
  - Valida la identidad y el cumplimiento de la política. Después **concede, restringe (cuarentena) o bloquea**.
  - Es clave con **BYOD**.
  - Ejemplos: **Cisco ISE** y **Fortinet FortiNAC**.

## 12. Confianza cero (Zero Trust)

- **NIST SP 800-207.** Es un «conjunto de paradigmas de ciberseguridad en evolución».
  - No hay **confianza implícita** por la ubicación (LAN o Internet) ni por quién es dueño del activo.
  - ⭐ **«Nunca confíes, siempre verifica».**
  - **Por qué surge:** el trabajo remoto, BYOD y la nube rompieron el perímetro.
- **Cambio de enfoque:**
  - Proteger **recursos**, no segmentos de red.
  - Suponer que **el atacante ya está dentro**.
  - Evaluar el riesgo de forma continua.
  - Implantarlo **de forma gradual**.
- **Principios básicos (los de NIST):**
  1. Supervisar la integridad y la postura de todos los activos.
  2. Proteger toda comunicación, esté donde esté.
  3. Conceder el acceso **por sesión**.
  4. Política **dinámica**: estado de la identidad, de la aplicación y del activo solicitante.
  5. Autenticar y autorizar estrictamente **antes** de dar acceso.
  6. Recopilar toda la información posible para mejorar.

| Zero Trust basado en… | Herramientas |
|---|---|
| Identidad | IAM, MFA, mínimo privilegio |
| Red | NAC, microsegmentación, cortafuegos, VPN, IDS/IPS |
| Datos | Clasificación, DLP, cifrado en reposo, en tránsito y en uso |
| Aplicaciones | Protección en tiempo de ejecución, contenedores |
| Dispositivos | Protección de *endpoint*, cifrado, borrado remoto |

Están diseñados para **trabajar juntos**.

## 13. Servicios de directorio y federación

| Servicio | Lo esencial |
|---|---|
| **LDAP** | Protocolo para buscar, gestionar y autenticar usuarios, grupos y dispositivos de forma centralizada. Puertos **389** (sin cifrar) y **636** (LDAPS). Árbol de directorio con nombres distintivos. Se protege con ACL, políticas de contraseña, auditoría, respaldos y canales seguros |
| **Active Directory** | LDAP con extensiones de Microsoft para dominios Windows. **GPO** y autenticación **Kerberos**: tickets de duración limitada, así que la red expone tickets, no contraseñas. Concentra el riesgo en los controladores de dominio. Alternativa libre: **Samba** (SMB) |
| **Entra ID** (antes Azure AD) | Identidad en la nube con OAuth 2.0, SAML y OIDC. Passwordless, MFA y **acceso condicional** por riesgo (dispositivo, ubicación, comportamiento). Depende de Internet. Alternativas: Okta, JumpCloud, Keycloak, Authentik y Authelia |

- **Federación de identidades:** «sistema de confianza entre distintas organizaciones o dominios»; te autenticas en tu proveedor y usas otros servicios sin volver a registrarte.
  - **SSO:** autenticarse una vez para acceder a muchas aplicaciones. Es el mecanismo de la federación y reduce la proliferación de contraseñas.
- ⭐ **OAuth frente a OIDC:**

| | OAuth 2.0 | OpenID Connect (OIDC) |
|---|---|---|
| Sirve para | **Autorización:** qué puede hacer una app en tu nombre sin conocer tu contraseña | **Autenticación:** quién eres |
| Token clave | **Token de acceso** (lo valida el servidor de recursos) | **Token de identidad (ID)**: nombre, correo, vencimiento; firmado |
| Roles | Servidor de autorización (IdP), cliente, propietario del recurso, servidor de recursos | Proveedor de OpenID, parte dependiente (el cliente) y usuario final (el propietario) |
| Quién lo impulsa | Estándar abierto | OpenID Foundation (Microsoft, Google). **Va encima de OAuth 2.0** |

- **Tokens de OAuth:** de acceso, de identificador y de **actualización** (este último pide tokens nuevos sin volver a autenticar).
- **Registro de la aplicación:** la app se registra en el IdP, que le asigna un ID y una URI de redirección.
- **IdP dominantes:**
  - **Empresariales:** Entra ID, Okta, Ping, Google Workspace.
  - **De desarrollo:** Auth0, AWS Cognito.
  - **Sociales:** Google, Apple, Meta.

## 14. Mitigación de riesgos de identidad

- **Vectores de ataque a la identidad:**
  - Robo de contraseñas.
  - **Ingeniería social:** la principal, sobre todo por phishing.
  - MITM.
  - Malware que roba credenciales.
  - **SIM swapping:** el atacante suplanta a la víctima y pasa su número a otra SIM alegando robo o daño.
  - **Credential stuffing:** listas de credenciales filtradas que bots prueban en muchos sitios. Por eso reutilizar contraseñas es grave; ver [[Actividad 1 - Buenas practicas de ciberseguridad|Actividad 1]].
- **Vectores contra Zero Trust:**
  - **Movimiento lateral** con una identidad comprometida.
  - **Desviación de políticas:** excepciones bienintencionadas que abren huecos.
  - **Cadena de suministro:** muchos IdP y nubes forman relaciones de confianza que se pueden explotar.
- **APT** (amenaza persistente avanzada): «ciberataque oculto, prolongado y que permanece sin ser detectado por largo tiempo». Suele estar patrocinado por estados con fines de espionaje.
  - **Vishing** potenciado por IA generativa: el principal método de acceso inicial.
  - **Suplantación ante la mesa de ayuda:** para conseguir que restablezcan la contraseña o salten el MFA.
  - **Intermediarios de acceso:** venden credenciales robadas.
- **Recomendaciones:**
  - **Zero Trust.**
  - **RBAC:** acceso según el rol (el analista configura el firewall pero no ve clientes; ventas ve clientes pero no toca el firewall).
  - **ABAC:** acceso según atributos del **usuario** (puesto, antigüedad), del **recurso** (tipo, autor, confidencialidad) y del **entorno** (lugar, hora, fecha). Ejemplo: «no se trabaja los sábados» → hoy sábado nadie entra.
  - **MFA, pero no por SMS**, porque es vulnerable al SIM swapping (la diapositiva dice «SMS swapping», que parece una errata). Lo preferido son las ***passkeys* FIDO con llave física**.
  - **ISPM** (*Identity Security Posture Management*): monitoreo continuo de la identidad para detectar cuentas inactivas, administradores ocultos y credential stuffing. Se integra con IAM.

| RBAC | ABAC |
|---|---|
| Decide por el **rol** | Decide por **atributos** del usuario, del recurso y del entorno |
| Simple y estático | Fino y dinámico (encaja con Zero Trust) |

---

## Actividades que pueden reaparecer en el examen

- [[Actividad 1 - Buenas practicas de ciberseguridad|Actividad 1]]: buenas prácticas que no cumples y por qué. Sirve como ejemplo de fatiga de seguridad y de la distancia entre saber y hacer.
- Actividad de la diapositiva 21: población → capacidad o limitación → mecanismo → cómo influye. Ver ![[Actividad 1 - Sector poblacion.docx]].
- Actividad 2: actores de una secundaria mexicana y sus contextos físico y social. Ver ![[Actividad 2 - Actor escuela secundaria.docx]]. Es la base del proyecto final.
- [[Actividad - Usable Security 4.4.2]]: estrategias, características de los usuarios, métricas, resultados y áreas de oportunidad.
- «Bridging the Gap in Computer Security Warnings» (modelos mentales y advertencias). ⚠️ No hay nota en el vault.
- Elegir 3 de los 50 sesgos y justificarlos. ⚠️ No hay nota en el vault.
- Unidad 2: matriz JML de un empleado de TI, comparativa de 3 IAM y 3 NAC, y rendimiento de un método passwordless. ⚠️ No hay notas en el vault.

## Preguntas abiertas probables

Contéstalas en voz alta o por escrito **antes** de abrir la respuesta.

> [!question]- ¿Por qué un usuario que conoce una buena práctica no la cumple?
> Fatiga de seguridad: la tarea habilitadora compite con la de producción. Además, el cambio de comportamiento exige memoria de largo plazo y un disparador (Fogg: motivación + capacidad + *prompt*), y los sesgos (optimismo, agotamiento del ego) no se corrigen con educación. La solución es adaptar la tarea al humano, no al revés.

> [!question]- Explica el modelo del queso suizo con un caso de phishing
> El empleado que hizo clic es el fallo activo, pero antes hubo fallos latentes: presión de tiempo, capacitación sin práctica, un filtro de correo mal configurado y una política imposible de cumplir. Cada defensa tenía un agujero y se alinearon. Culpar solo al usuario no corrige nada; hay que notificar los cuasi accidentes.

> [!question]- ¿Qué modelo mental usarías para concienciar a alumnos de secundaria y por qué?
> El médico o el físico, porque se apoyan en experiencias que ya tienen (vacunarse, cerrar la puerta). El médico añade la responsabilidad colectiva (si te infectas, contagias). El de guerra no conviene: asusta y deja la responsabilidad en los expertos. Lo que se califica es la argumentación: elegir según el público.

> [!question]- Diferencia entre identificación, autenticación y autorización
> Identificación: decir quién eres (el usuario). Autenticación: demostrarlo con factores de conocimiento, posesión, inherencia o comportamiento. Autorización: qué permisos tienes después (RBAC o ABAC, mínimo privilegio).

> [!question]- ¿Por qué no se recomienda la MFA por SMS? ¿Qué se recomienda?
> El SMS no va cifrado y el SIM swapping permite recibir los códigos de la víctima. Se recomiendan *passkeys* FIDO con llave física: la clave privada nunca sale del dispositivo, y no hay nada que robar por phishing.

> [!question]- OAuth vs OIDC
> OAuth sirve para autorizar (token de acceso: qué puede hacer una app en tu nombre). OIDC sirve para autenticar (token de ID: quién eres) y se monta sobre OAuth 2.0.

> [!question]- ¿Qué es Zero Trust y en qué se diferencia del modelo perimetral?
> Es NIST SP 800-207: «nunca confíes, siempre verifica». No hay confianza implícita por estar dentro de la red; se protegen recursos, no segmentos; se asume que el atacante ya está dentro; el acceso se da por sesión con una política dinámica.

> [!question]- ¿Por qué los sesgos no se corrigen con capacitación? ¿Entonces qué se hace?
> Son sistemáticos, involuntarios y difíciles de evitar; no se eliminan ni con incentivos ni pidiendo atención. Se diseña alrededor de ellos: priorizar la psicología sobre la tecnología, defensa en profundidad y formación periódica que refuerce el hábito (contra el agotamiento del ego).

## Plan para esta noche

El examen es mañana: no hay tiempo para espaciar los repasos, así que el plan se apoya en **ponerse a prueba en vez de releer**. Son cuatro bloques de unos 40 minutos con descansos cortos, y luego a dormir. **Dormir 7–8 h rinde más que un quinto bloque.**

**Cómo va cada bloque:** primero escribe de memoria las listas del bloque, después compara con este temario y marca en el [[#Registro de fallos]] lo que se te olvidó.

### Bloque 1 — Unidad 1, primera mitad (temas 1–4)
- [ ] Definir de memoria comportamiento, conducta (los 3 pasos) y los 2 contextos.
- [ ] Kerckhoffs (1883) y los 3 principios de Saltzer y Schroeder (1975).
- [ ] La definición ISO de usabilidad con sus 3 componentes, y los **4 factores** para adaptar la tarea, con un ejemplo de cada uno.
- [ ] Fatiga por alarma vs fatiga de seguridad; tareas primarias vs habilitadoras.
- [ ] Fallo latente vs activo; queso suizo; rápido vs lento de Kahneman.
- **Listo si:** contestas sin mirar la pregunta abierta del queso suizo.

### Bloque 2 — Unidad 1, segunda mitad (temas 5–7)
- [ ] **Recuperar:** los 4 factores y la tabla de fallos latentes, sin mirar.
- [ ] Concienciación vs educación vs formación; RISCS y **Fogg** (los 3 elementos).
- [ ] Los **4 modelos mentales** con su limitación cada uno. Revisa la corrección del modelo económico.
- [ ] Las 4 características de los sesgos, y al menos 7 de los 10 sesgos con su ejemplo.
- **Listo si:** contestas sin mirar la de los alumnos de secundaria y la de por qué no se cumple una buena práctica.

### Bloque 3 — Unidad 2, primera mitad (temas 8–10)
- [ ] **Recuperar:** los 4 modelos mentales y 5 sesgos, sin mirar.
- [ ] Los 4 pilares de la IAM, los 3 tipos de identidad y JML (qué pasa en cada fase).
- [ ] Los 4 factores de autenticación; los 7 requisitos biométricos; TOTP vs HOTP; el flujo FIDO en 4 pasos; la fatiga MFA.
- **Listo si:** explicas identificación / autenticación / autorización y por qué no usar SMS.

### Bloque 4 — Unidad 2, segunda mitad (temas 11–14)
- [ ] **Recuperar:** los pilares de la IAM, los 4 factores y los 7 requisitos biométricos.
- [ ] Los 4 métodos de autenticación de dispositivos; los tipos de certificado; qué hace el NAC.
- [ ] Zero Trust: el lema, los 6 principios y los 5 tipos.
- [ ] LDAP (puertos), AD (Kerberos y GPO), Entra ID; OAuth vs OIDC.
- [ ] Vectores: SIM swapping, credential stuffing, APT; RBAC vs ABAC; ISPM.
- **Listo si:** respondes sin mirar todas las preguntas abiertas de arriba.

### Mañana antes del examen (15 min)
- [ ] Solo el registro de fallos y las tablas con ⭐. Nada nuevo.

### Registro de fallos

Anota aquí lo que se te olvide en cada bloque y repásalo mañana temprano.

-

## Relacionadas

- [[Aspectos sociales de la ciberseguridad]]: índice de la materia.
- [[Comportamiento y conducta]] y [[CyBOK]]: las dos notas de concepto que ya tiene la Unidad 1.
- [[MOC - El factor humano]]: el hilo transversal al que se engancha la Unidad 1.
- [[Actividad - Usable Security 4.4.2]]: el desarrollo completo de la lectura de seguridad usable.
