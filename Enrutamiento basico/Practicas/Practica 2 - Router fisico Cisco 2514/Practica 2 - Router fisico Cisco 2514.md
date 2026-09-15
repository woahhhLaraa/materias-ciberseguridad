---
materia: Enrutamiento basico
semestre: 3
tipo: practica
tags: [practica, cisco, ios, hardware, laboratorio]
---

# Practica 2 - Router fisico Cisco 2514

Misma secuencia que [[Practica 1 - Configuracion inicial del router]], pero sobre hardware real en el laboratorio en vez de Packet Tracer. El valor de la practica esta justo en las diferencias del inventario de interfaces.

## Diferencias frente al router virtual de la Practica 1

| | Cisco 1941 (Packet Tracer, Practica 1) | Cisco 2514 (fisico, Practica 2) |
|---|---|---|
| FastEthernet | 4 (modulo EtherSwitch) | 0 |
| GigabitEthernet | 2 (Gi0/0, Gi0/1) | 0 |
| Ethernet | — | 2 (Ethernet0, Ethernet1 — AUI, 10 Mbps) |
| Serial | 2 (Se0/0/0, Se0/0/1) | 2 (Serial0, Serial1) |
| Lineas vty | 0 4 | 0 4 |

> ⭐ El 2514 es de una generacion anterior: sus puertos LAN son Ethernet AUI de 10 Mbps, no FastEthernet. Si el examen pregunta "cuantas FastEthernet tiene", la respuesta en este equipo es **0**, y hay que justificarlo.

En los dos casos `startup-config` no esta presente al arrancar: nunca se ha guardado la configuracion en NVRAM con `copy running-config startup-config`.

## Entrega

- ![[Practica 2 - Respuestas.pdf]]
- ![[Practica 2 - Respuestas.docx]]

## Relacionadas

- [[Practica 1 - Configuracion inicial del router]] — la misma practica sobre el router virtual; esta nota solo documenta lo que cambia
- [[Practica 1 - Adaptacion a switch fisico]] — la otra adaptacion a equipo real, sobre un switch de acceso
- [[Sistema operativo IOS de cisco]] — los modos de CLI y los comandos que se usan aqui
- [[Sintaxis basica de comandos IOS]] — la sintaxis de los comandos, vista en semestre 2
