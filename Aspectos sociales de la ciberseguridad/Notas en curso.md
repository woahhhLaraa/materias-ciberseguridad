---
materia: Aspectos sociales de la ciberseguridad
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---

# Aspectos sociales de la ciberseguridad — notas en curso
MODELOS MENTALES 

Modelo de seguridad fisica
Se basa en conceptos fisicos como puertas, cerraduras, perimetros
Puertas, cerraduras y permitetros fisicos
Sus ataques requieren presencia fisica,
Limitaciones:
- No cubre la naturaleza dinamica y distibuida de las amenzasas digitales
	- Un calbe ethernet puede atrevesar pardes seguras, y la informacion digital puede ser copiada sin tener acceso fisico
	- el control fisico es local y requiere inversion individual y comunitaria

Modeo medico
- Considera los ataques informaticos como enfermedades infecciosas que se propagan en la red
	- El gusano "malo" y el gusano "bueno" el cual se propagaba para aplicar parches y curar sistmeas infectados
		- Destaca la importancia de la higiene digital (mantener un sistmea protegido para evitar ser fuente de infeccion)
		- Responsabilidad individual ycolectiva
		- Enfatiza que todos estan en riesgo, y las medidas de seguridad son cuidado preventivo

Modelo de guerra
- Considera la infromatica como conflicto bvelico como un enemigo persistennte
- necesidad de defender perimetros robustos, vigilancia ocntinua, inteligencia y _preparacion constante_
- No se trata de evitar ataques, sino responder activamente con multiples capas de defensa
- Puuede incitar miedo o terror, para motiviar a los usuarios a defenderse
	- limitaciones
		- Tiende a eliminar la responsabildiad individual, convenciendo a los usuarios de uqe los expertos deben encargarse completamente de la seguridad
		- Hace creer que el control debe ser centralizado, cerrado.

Modelo economico o de mercado
- Ve la seguridad como un problema de costos y beneficios, terceros implicados, contratos
- Con la idea de que la falta de seguridad puede provocar costos evitables, traduciendo a precios reales, datos, informacion, privacidad.
- Utiliza incentivos economicos para motiviar comportamientos seguros o castigos por negligencia
	- limitaciones
		- Paranoia (a la gente le preocupa demasiado el dinero)
		- desatencion de otros riesgos
		- dificultad a asignar costos reales en entornos compartidos


En cuanto a temsa de privacidad y segurdida hay recomendaciones
- Hay diferentes maneras de comunicar riesgos
- SImplificar demasiado o sol odar datos tecnicos no fucniona para que la gente tome las mejores decisiones

Entonces se propone:
- Usar la informacion previa de los atajos mentales para ayudar a la gente a comprender un riesgo
	- Por eso usamos los modelos de seguridad fisica anteriores

Cada modelo mental tiene ventajas y limitaciones, deben ser escogidos segun el usuario o grupo que se trate
Al final si se utilizan correctamente, puede hacer entender a los usuarios la importancia de la seguridad informatica.


11 de septiembre 2026
Presentacion del proyecto
Propuesta que contribuya a aumentar la conciencia en ciberseguridad, en el contexto de una secundaria mexicana

Un documento que describa toda la propuesta
Un producto final (triptico, infografia, video, tiktok, juego, presentacion)

Los mejores productos son presentados en escuela tecnica

18 de septiembre 2026

Red corporativa moderna
Una variedad de usuarios entidades que requieren acceso seguro desde distintas ubicaciones

Usuarios humanos
- Empleados internos
- Clientes externos
- Contratistas y terceros
Usuarios no humanos
- Agentes de ia
- Dispositivos IoT
- Endpoints corporativos
- Cargas de trabajo automatizadas

Gestion de identidad 
Disciplina de la ciberseguridad que se ocupa del aprovisionamiento y proteccion de identidades digitales y permisos de acceso a los usuarios de un sistema de TI
Pretende que
- Tengas acceso seguro
- Bloqueo de amenazas
	- Tanto externos como internos
- Herramientas IAM
	- Permiten a los organizaciones crear y eliminar de fomra segura identidades digitales, establcer y aplicar politicas de control de acceso

Que es la identidad digital?
- Combinacion de atributos y credenciales que representan a una perosna o entidad
- Conjunto de informacion vinculado a un usuario maquina u otra entidad especifica en un ecosistema de TI
	- Nombres
	- Direcciones
	- Datos biometricos
	- Historial de navegacion
	- perfiles en linea

Tipos de identidades
- Humana
	- La huella digital que deja un ser humano al usar internet
- Maquinas
	- Bots, ias, identificadores unicos, tokens
- Identidades federadas
	-  Permiten a las personas usar sus identidades en multiples sistemas y servicios
		- Logearse con google, o facebook en sitios que ofrecen un servicio distinto al suyo

Metodos de verificacion
- Credenciales
- Biometria
- Certificados
- Para prevenir robos de identidad y fraude

PILARES DE LA IAM

- Administracion
	- El proceso de crear mantener y eliminar las identidades de los usuarios
- Autenticacion
	- El usuario se identifica enviando crenciales, y el sistema IAM compara las credenciales con la base de datos
- Autorizacion
	- El sistema revisa que clase de permisos tiene el usuario anteriormente autenticado
	- Control de acceso basado en roles
- Auditoria
	- Garantiza que el sistema funciona correctamente
	- Monitoreo continuo de los usuarios


Ciclo de vida de la identidad del modelo JLM
- Joiner
	- Creacion de la identidad, aprovisionamiento de acceso y asignacion de roles para los nuevos empleados pasantes o contratistas
- Mover
	- Ajuste dpermisos cuando se cambian de puestos o equipos o responsabilidades
- Leaver
	- Revocacion de acceso, recuperacion de activos y generacion de registro de auditoria al abandonar la organizacion

30 de septiembre de 2026
Cuatro pilares de la gestion del ciclo de vida de la identidad
- Aprovisionamiento
	- Establece la identidad y otorga acceso basico
	- Creacion de cuenta definicion de rol inicial y asginacion de persmios
- Gestion y modificacion de accesos
	- Cambio de rol de una entidad 
	- adaptacion de permisos
	- revision y actualizacion cotinua de drechos de accesos de acuerdo con el principio de minimo privilegio
- Seguimiento y auditoria
	- Visibildiad continua de todas las actividades de la entidad y solicitudes de acceso
	- Auditorias periodicas 
- Desabastecimiento
	- Eliminacion sistemica del acceso a una entidad
------
Autenticacion de personas:
La autenticacion puede ser:
- Algo que sabes
- Algo que tienes
- Algo que eres
- Algo que haces



- Cualquier factor de autenticacion que se base en u nsecreto que el usuario conoce

Contraseñas
- Metodo mas coun de autenticacion
- Objeto de robo a traves de phishing
- Adivinables
- Filtradas
- el robo de cuentas validas fue uno de los vectores de ataque presentes en el 32% de los ataques

Preguntas de seguridad
- Descubribles mediante ingenieria social o espionaje en redes sociales.

Factores de autenticacion passwordless
Tokens de hardware
biometricos
etc

Claves de acceso (passkeys) y FIDO/FIDO2
Basadas en criptografia de clave publica
Implementadas de acuerdo con los estandares FIDO o FIDO2

FIDO (FAST IDENTITY ONLINE)
Conjunto de estandares abiertos para la autenticacion sin contrasñea para sitios web, aplicaciones, y servicios en linea
Reemplaza la cntrasña tradicional con claves criptograficas
Clave publica y privada
Una clave publica compartida con el servicio y una clave privada almacneada en el dispositivo del usuario
La clave privada no se comparte
La clave privada esta protegida mediante un pin o un metood de verificacion viometirca


Factores biometricos
Caracteristicas fisicas dle uusario
Su origen son intrinsiceos de la vida del usuario
	Estatico
		REconocimiento de huellsa
		lectura de mano
		lectura de iris
		retina
	DImanico
		Dinamica de dfirmas
		Reconocimiento del habla
Requisitos generales:
- Universalidad
	- Cada persona debe tener la caracteristica
- Singularidad
	- Dos personas no debn tener la misma caracteristica
- Permanencia
	- No dbee cambiar ni ser alterada
- Coleccionabilidad
	- La caracteristica deb ser medible
- Rendimiento
	- Debe poder medirse en terminos de precision, velocidad, robustez y recursos necesarios
- Aceptabilidad
	- La caracteristica deb ser aceptable por el publico
- Elusion
	- No debe ser facil de engañar

Contrasenas de un solo uso:
Se consideran factores se posesion, no de conocimiento
No son de larga duracion
Cada vez que se quiere iniciar sesion genera una nueva OTP


TOPT y HOTP
TOPT time based one time password
HOTP: Hash based one time password


Tokens de hardware
Dispositivos dedicadoes a menudo en forma de usb

Magic links
Enlaces especiales que contienen tokens de autenticacion

Notificaciones PUSH 

Funnciona similar a los enlaces magicos
El usuario debe tocar aprobar en la notificacion push para obtener el acceso
Susceptible a fatiga MFA
	Un actor de amenazas navega hsata el servicio, ingresa el id del usuario y solicita repetidamente autenticacion mediatne la notificacion de push

 codigos QR
 El usuario escanea el codigo, generalmente con una aplicacion de autenticacion o una aplicacion especifica del servicio al que esta accediendo

Autenticacion multi factor
Factor 1. Usario + contrasena
Factor 2. Algo que se tiene o se es






> **Bandeja de entrada de la materia.** Todo lo de clase entra aquí, bajo el encabezado de la fecha, sin preocuparse por la estructura.
>
> Al estudiar para el parcial: selecciona cada bloque que sea un concepto y usa `Ctrl+P` → **Extraer selección actual**. Obsidian crea la nota y deja el enlace aquí. Cuando este archivo quede solo con enlaces, el parcial está repasado.
>
> Índice de la materia: [[Aspectos sociales de la ciberseguridad]]

