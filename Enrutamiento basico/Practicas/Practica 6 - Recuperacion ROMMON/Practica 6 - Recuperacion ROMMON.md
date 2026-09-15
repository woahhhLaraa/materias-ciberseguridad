---
materia: Enrutamiento basico
semestre: 3
tipo: practica
tags: [practica, cisco, ios, rommon, recuperacion-de-password, laboratorio]
---

# Practica 6 - Recuperacion ROMMON

Recuperar el control de un router Cisco cuyo password de acceso se desconoce, forzando el arranque en **modo ROMMON** para interrumpir la carga normal del IOS mediante una senal de *break*.

![[Practica 6 - Recuperacion ROMMON.docx]]

## Idea de fondo

El password vive en `startup-config`, en la NVRAM. ROMMON es el monitor de arranque que corre **antes** de que el IOS lea ese archivo, asi que desde ahi se puede decirle al router que ignore la NVRAM al arrancar, entrar sin password y recuperar la configuracion.

## Requisitos

- Emulador de terminal por consola: `minicom` o `screen` en Debian, PuTTY en Windows
- Adaptador serial (o serial-USB) conectado al puerto de consola del router

> ⚠️ Esta es una tecnica de recuperacion con acceso fisico al equipo. Implica que **la seguridad fisica del router es parte de su seguridad logica**: quien alcanza el puerto de consola puede saltarse el password.

## Relacionadas

- [[Sistema operativo IOS de cisco]] — secuencia de arranque, NVRAM y `startup-config`, que es lo que ROMMON esquiva
- [[Practica 2 - Router fisico Cisco 2514]] — la otra practica sobre equipo fisico del laboratorio, misma conexion por consola
- [[Normas de seguridad fisica]] — por que el acceso fisico al equipo derrumba el control logico
