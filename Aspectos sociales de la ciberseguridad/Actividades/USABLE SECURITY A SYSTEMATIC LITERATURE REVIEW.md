Seccion 4.4.2
Resumen del articulo:

La seguridad usable consiste en diseñar medidas de seguridad que se adapten a las necesidades y comportamientos de los usuarios. Equilibrar usabilidad y seguridad plantea desafíos: cuanto más seguros son los sistemas, menos usables resultan. Por el contrario, los sistemas más usables serán menos seguros. Numerosos estudios han abordado este equilibrio. Dichos estudios, que abarcan la psicología y las ciencias/ingeniería de la computación, aportan perspectivas diversas, lo que hace necesaria una revisión sistemática para comprender las estrategias y los hallazgos en este ámbito. Esta revisión sistemática de la literatura examinó artículos sobre seguridad usable publicados entre 2005 y 2022. Tras la evaluación, se seleccionaron un total de 55 estudios de investigación. Los estudios se han clasificado a grandes rasgos en cuatro grupos principales, cada uno de los cuales aborda aspectos distintos: (1) la usabilidad de los métodos de autenticación, (2) la ayuda a los desarrolladores de seguridad para mejorar la usabilidad, (3) las estrategias de diseño para influir en el comportamiento de seguridad del usuario y (4) los modelos formales para la evaluación de la seguridad usable. A partir de esta revisión, informamos que el estado actual del campo revela cierta inmadurez, con estudios que tienden a la comparación de sistemas en lugar de establecer directrices de diseño sólidas basadas en un análisis exhaustivo del comportamiento del usuario. Un marco teórico y metodológico común es una de las principales áreas de mejora en esta línea de investigación. Además, la ausencia de requisitos de seguridad usable en casi todos los contextos de desarrollo desincentiva enormemente la implementación de buenas prácticas desde las etapas más tempranas del desarrollo.

## 4.4.2. Ayudar a los desarrolladores de seguridad a mejorar la usabilidad (7 artículos)


### Cuales son las estrategias o mecanismos de seguridad usable que se presentan?
- analizan la importancia de incluir información relacionada con la seguridad en la documentación de las interfaces de programación de aplicaciones (API)
	- las cuales, aunque no esténdiseñadas explícitamente con fines de seguridad, pueden suponer un riesgo si no se utilizan correctamente 
		- ¿En qué medida influye la ubicación de la información relacionada con la seguridad en la documentación de la API en la transmisión de dicha información a los desarrolladores?
		- cómo leen esta documentación, centrándose en los elementos a los que prestan más atención mediante el uso del seguimiento ocular;
		- El impacto de la presencia de instrucciones de ciberseguridad en la documentación de la API sobre la funcionalidad y la seguridad del producto final.
- Un enfoque de desarrollo "orientado a conceptos" 
	- Mediante pruebas de desarrollo mediante apis (ver punto anterior), donde una API bien documentada sobre la seguridad de sus uso promueve la creacion de un software operativo y seguro.
	- Los autores promueven escribir esta parte de la documentacion, cerca de los codigos de ejemplo dentro de una documentacion (pues es lo primero que consulta un desarrollador cuando tiene dificultades), si bien esto fue aplicado a un contexto de apis, puede (y debe) ser utilizado en cualquier herramienta de desarrollo donde la seguridad tanto del usuario final como del propio codigo pueden quedar vulnerables por un mal uso esta.
- Uso de capa de seguridad CSP
	-  Politica de navegadores donde se decide que es lo que si y no puede ejecutar un navegador en una computadora (scripts, estilos, imágenes, iframes, conexiones, etc.) con el objetivo de reducir la superficie de ataque
- Uso de interfaces graficas claras, donde la seguridad de la informacion sea uno de los ejes centrales.
	- Ayudando al usuario a proteger su informacion con una retroalimentacion clara, sin dejar de ser facil de usar
- El uso de interfaces claras vuelve a aparecer en el momento de identificar sitios web y correos electronicos fraudulentos
	- Sin embargo, el reconocimiento por parte de los usuarios de estas situaciones, se ve directamente influenciada por su capacitacion en cuanto a temas de ciberseguridad. Por lo que una interfaz clara si bien ayuda, no es determinante si un usuario no ha recibido suficiente capacitacion con anterioridad.
- La traduccion de conceptos abstractos de la seguridad en criterios medibles y evaluables
	- Tras varias fases en las quese analizaron y redujeron los objetivos mediante entrevistas y análisis estadísticos, los autores identificaron cuatro objetivos finales: maximizar la facilidad de uso y mejorar la comunicación relacionada con el sistema, maximizar la estandarización y la integración, y maximizar la capacidad del sistema. Según los autores, estos objetivos resultan útiles para orientar la implementación y el desarrollo de software


La utilizacion de una metodologia comun que permita establecer un enfoque estandarizado sobre estsos criterios