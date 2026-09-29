---
materia: Sistemas Operativos
semestre: 3
tipo: concepto
tags:
  - sistemas-operativos
  - fundamentos
sr-due: 2026-11-07
sr-interval: 40
sr-ease: 274
---
#review 
# Definición y funciones del sistema operativo

## Tres definiciones

| Fuente | Definición |
|---|---|
| **Tanenbaum** | Software que actúa como intermediario entre el usuario y el hardware, *gestionando los recursos de los equipos* |
| **Silberschatz** | Programa que administra los recursos y *proporciona servicios para facilitar la ejecución de los programas de aplicación* |
| **El profesor** | Programa que administra la ejecución de otros programas y gestiona los recursos del dispositivo |

Las tres coinciden en el núcleo: **administrar recursos**. Difieren en el énfasis — Tanenbaum en la intermediación, Silberschatz en el servicio a las aplicaciones.

## Funciones principales (Escenciales de un sistema)

- Administrar la CPU
- Gestionar memoria
- Gestionar archivos
- Gestionar dispositivos
- Gestionar procesos
- Proporcionar interfaz de usuario
- **Proteger recursos** — de accesos de usuarios y de otros programas a los recursos del sistema


## Características

- **Facilidad de uso** (usabilidad) — las GUI son las más sencillas
- **Gestión de recursos**
- **Multitarea**
- **Seguridad**
- **Estabilidad**
- **Eficiencia**
- **Capacidad de evolución**
- **Portabilidad** — adaptarse a diferentes tipos de dispositivos o hardware

## Componentes
Un OS lo conforma
- Un kernel, en nucleo, su elemento mas importante que se encuentra en la capa inferior, la mas alejada de la interfaz del usuario, pero en contacto directo con el hardware
- La capa de usuario: donde se encuentra su interfaz ya sea en GUI o una CLI, se encuentran su aplicaciones, sus librerias
- El hardware

- **Shell** — la interfaz de usuario, tipo CLI o GUI
- **Kernel** — establece la comunicación entre hardware y software
- **Hardware** — la parte física, incluida la electrónica subyacente

## Relacionadas

- [[Generaciones de sistemas operativos]] — cómo fueron apareciendo estas funciones, generación por generación
- [[Tipos de sistemas operativos]] — las mismas funciones repartidas según el sistema: servidor, escritorio, móvil
- [[Jerarquia de memoria]] — cómo el SO gestiona la memoria a nivel hardware
- [[Capas de un sistema operativo]] — el detalle de estas funciones repartido en los ocho subsistemas del SO
