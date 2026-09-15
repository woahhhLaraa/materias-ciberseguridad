---
materia: Enrutamiento basico
semestre: 3
tipo: practica
tags: [practica, cisco, ios, switch, laboratorio, consola-serial]
---

# Practica 1 - Adaptacion a switch fisico

Guion de laboratorio: la secuencia de [[Practica 1 - Configuracion inicial del router]] llevada a un **switch Cisco fisico**, conectado por consola serial en vez de Packet Tracer.

Conexión: `picocom -b 9600 /dev/ttyUSB0`   (salir: Ctrl+A, Ctrl+X)
Si no aparece nada, presiona ENTER un par de veces.

## Parte 1 — Verificar configuración por defecto
    Switch> enable
    Switch# show running-config
    Switch# show startup-config

Anotar para el reporte:
- hostname del equipo
- cuántas interfaces FastEthernet
- cuántas interfaces GigabitEthernet
- interfaces Serial (en switch de acceso: normalmente 0 — justificarlo)
- rango de líneas vty (típico: 0 4, o 0 15)
- por qué startup-config no está presente

## Parte 2 — Configuración inicial
    Switch# configure terminal
    Switch(config)# hostname R1
    R1(config)# enable password cisco
    R1(config)# enable secret itsasecret
    R1(config)# line console 0
    R1(config-line)# password letmein
    R1(config-line)# login
    R1(config-line)# exit
    R1(config)# service password-encryption
    R1(config)# banner motd #Unauthorized access is strictly prohibited.#
    R1(config)# end

Verificar:
    R1# show running-config

Probar el banner y el password de consola:
    R1# exit
    (ENTER -> debe pedir Password: letmein)
    R1> enable        -> pide itsasecret (el secret gana sobre enable password)

## Parte 3 — Guardar
    R1# copy running-config startup-config
    (versión más corta e inequívoca: `copy run start`)
    R1# show flash
    R1# copy startup-config flash

## Restaurar el equipo al terminar (si el laboratorio lo pide)
    R1# erase startup-config
    R1# reload      (responder "no" a guardar)

> ⚠️ En un switch de acceso lo normal es tener **0 interfaces Serial**: son puertos WAN de router, no de switch. Hay que justificarlo asi en el reporte, no dejarlo en blanco.

## Relacionadas

- [[Practica 1 - Configuracion inicial del router]] — la version en Packet Tracer; aqui solo cambia el equipo y la conexion por consola
- [[Practica 2 - Router fisico Cisco 2514]] — la otra practica sobre hardware real, con su propio inventario de interfaces
- [[Sistema operativo IOS de cisco]] — los modos de CLI y el orden `enable` → `configure terminal` que se usa aqui
