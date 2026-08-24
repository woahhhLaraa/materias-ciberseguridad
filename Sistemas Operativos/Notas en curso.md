---
materia: Sistemas Operativos
semestre: 3
tipo: captura
tags: [captura, sin-procesar]
---

# Sistemas Operativos — notas en curso


24 agosto 2026
Mas tipos de sistemas operativos

Tipos embebidos

Diseñados para funcionar en dispositivos especializados, microondas, refrigeradores, dispositivos medicos, sistemas de control y otros. pensados para funciones especificas. Normalmente sobre microcontroladores (no microcontroladores) y en hardware sin mucha potencia

Normalmente se cargan en memorias flash o de poco almacenamiento (Como dentro de la placa), y no suelen ser cambiados una vez se cargan

Los tipos de sistemas operativos embebidos mas conocidos son
	Emebbeded linux: Routers, camaras, televisroes inteligentes, sistemas multimedia, ejecutados en un procesador
		Usado por Sony: en equipos multimedia
		Garmin: Dispositivos de navegacion nautica
		Cisco: Equipos de red y dispostivos de infraestructura
	OpenWRT: Basado en linux principalmente para routners y dispositivos de red
	TinyOS: Diseñado especialmente para IoT


Tipos en Tiempo Real

Muchos de estos tambien son embebidos pues se meten en microcontroladores, diseñados para responder en tiempo real, pueden trabajar con recursos limitados.

Utilizados en automoviles, robots, aeronaves, y equipos de control, etc.

Como en los RC cars de los que mandan a la luna o marte en la NASA

Son parte de un sistema mas grande (no son el sistema principal), pues solo se dedican a hacer una cosa en especifico

Clasificados en
	Tiempo real duro: Donde cumplir el limite de tiempo es OBLIGATORIO
	Tiempo real blando: donde se puede permitr un pequeño retraso


LynxOS: Arquitecturas 32 y 64 bits en microprocesadores 
	Orientado a plataformas que requieren determinados recursos de memoria y hardware, utilizaod en sistemas de aeronauticas y aeroespaciales en plataformas militares

FreeRTOS
	Ligero y deiseñado para microcontroladores y recursos limitados, su nuclero utiliza muy poca memoria y tambien es ampliamente utilizaod en IoT
	Lo creo Richard Barry en 2003 y fue comprado por Amazon en 2017
	Usado en chips ESP32



Tipos en las capacidades que ofrece al usuario
	Numero de usuarios
		Monousuario
			Solo puede ser utilizado por un solo usuario al mismo tiempo, sin importar el numero de procesadores que tenga, o el numero de tareas que pueda ejecutar a mismo tiempo.
				Windows xp,7,vista,8,10,11. (son multicuenta, no multiusuario)
		Multiusuario
			Puede ser utilizado por varios usuarios al mismo tiempo, ya sea por medio de varias terminales o sesiones remotas dentro de una red de comunicaciones(SSH, Por ejemplo), sin importar el numero de procesos o procesadores
				Servidores, windows server, algunas distribuciones linux y macOS
	Numero de tareas
		Monotarea
			Una sola tarea al mismo tiempo, cuando un programa o tarea se ejecuta, toma el control absoluto de la CPU. (MS DOS, APPLE MACINTOSH Y ATARI TOS)
		Multitarea
			Permite gestionar y realizar varias labaores simultaneamente. Y esto puede darse de maneara simulada (concurrencia) o de manera real (paralelismo). Los sistemas actuales (windows, distribuciones linux, macOS) son multitarea
	Numero de procesadores
		Monoprocesador
			Aquel capaz de manejar solamente un procesador de la computadora, si tuviera mas de uno, nisiquiera lo reconoce. (MS DOS, WINDOWS 3.1, 10 HOME Y 11 HOME)
		Multiprocesador
			Aquel capaz de manejar mas de un procesador y usarlos para distribuir su carga de trabajo, pudiendo trabajar con ellos de forma
				Simetrica
					El sistema toma todos los nucleos o procesadores fisicos (donde todos tienen acceso a memoria) y gestiona su carga en igualdad de condiciones
				Asimetrica
					El sistema toma un cpu o nucleo y lo designa como maestro, el maestro se encargara de gestionar a los demas (esclavos)
			(WINDOWS 10,11,macOS, LINUX, ANDROID e IOS)
		Ojo, no debe confundirse con multinucleos


 Teoricamente un sistema podria ser multiusuario y monotarea, pero cada vez que un usuario haga algo, tomaria el control absoluto del sistema, y solo pasaria al siguiente usuario hasta terminarla
 
Tiempo de CPU o Rafaga de CPU:
Los sistemas con multiprogramacion, llevaron a que un CPU pudiera ejecutar varias tareas de manera simultanea (mediante un cambio de contexto), lo comparten por tiempo quantums.

Quantums de tiempo:
La cantidad de milisegundos que un cpu puede dar a una tarea

Cambio de contexto:
El momento del cambio de una tarea a otra durante la multiprogramacion con tiempo de cpu, cuando vuelve a la misma tarea que dejo, la inicia desde el momento en que se quedo la ultima vez.

Paralelismo (buscar):


Multitarea real(Buscar):





> **Bandeja de entrada de la materia.** Todo lo de clase entra aquí, bajo el encabezado de la fecha, sin preocuparse por la estructura.
>
> Al estudiar para el parcial: selecciona cada bloque que sea un concepto y usa `Ctrl+P` → **Extraer selección actual**. Obsidian crea la nota y deja el enlace aquí. Cuando este archivo quede solo con enlaces, el parcial está repasado.
>
> Índice de la materia: [[Sistemas Operativos]]

