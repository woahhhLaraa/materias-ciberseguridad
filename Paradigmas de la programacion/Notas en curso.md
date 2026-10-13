---
materia: Paradigmas de la programacion
semestre: 3
tipo: captura
tags: [captura, sin-procesar, programacion]
---

# Paradigmas de la programacion — notas en curso
Paradigma procedural (caso de estudio de C)

Identificadores, tipos de datos, variables y constantes

Un identificador es el nombre que le das a una variable o funcion, una etiqueta que se refiere a alago de manera unica, no son palabras reservadas.
En C.
- Pueden contener letra numeros y guion bajo
- El primer caracter debe ser letra o guion bajo
- No puede ser palabra reservada
- C es sensible a mayusculas y minisculas

Tipos de datos:
Le dice al compilador la cantidad de memoria que debe reservar  y como interpretar la informacion que almacena

Tipos de datos fundamentales
- char
- int
- float
- double
- void

los datos pueden ser alterados con modificadores de tipos
- short int
- long int
- unsigned int
- long long int


8 de octubre
Ciclo de vida de desarrollo de software
Planificar
	Entender y documentar que debe hacer un software
		Reuniones, entrevistas
Analizar
Diseño
Implementacion
Pruebas e implementacion
Mantenimiento y documentacion


Programacion orientada a objetos
Paradigma de programacion mas usado
Basado en abstraer objetos como si fueran del mundo real a sus atributos, estados y funciones mas simples

Abstraccion, el pilar de la programacion orientada a objetos, implica enfocarse en los aspectos escenciales de un objeto.

Encapsulamiento: Ocultar las caracteristicas anteriomente abstraidas exponiendo solo lo necesario para uso externo

Herencia: Heredar de una clase mas arriba las abstracciones que tuvieron.

Polimorfismo: Usar un meto instanciado a una clase, de forma distinta dependiendo del objeto

Atributos
	Variables que pertenecen a una clase y describen sus propiedas o caracteristicas. Sustantivo o adjetivo que definen a cuaquier objeto de esa clase.

Metodos:
	Lo que el objeto puede hacer, ademas existiendo los metodos que modifican las propiedades y caracteristicas de ese objeto (getters y setters).


Diagrama de clases UML
![[Pasted image 20261008074954.png]]

![[Pasted image 20261008075415.png]]