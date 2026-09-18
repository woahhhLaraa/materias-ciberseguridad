---
materia: Enrutamiento basico
semestre: 3
tipo: practica
tags: [practica, cisco, ios, rommon, recuperacion-de-password, laboratorio]
---

# Practica 6 - Recuperacion ROMMON

Recuperar el control de un router Cisco cuyo password de acceso se desconoce, forzando el arranque en **modo ROMMON** para interrumpir la carga normal del IOS mediante una senal de *break*.

Enunciado: ![[Practica 6 - Recuperacion ROMMON.docx]] · Reporte entregado el 18 de septiembre de 2026: ![[Practica 6 - Recuperacion ROMMON (entregada).pdf]]

## Idea de fondo

El password vive en `startup-config`, en la NVRAM. ROMMON es el monitor de arranque que corre **antes** de que el IOS lea ese archivo, asi que desde ahi se puede decirle al router que ignore la NVRAM al arrancar, entrar sin password y recuperar la configuracion.

## Requisitos

- Emulador de terminal por consola: `minicom` o `screen` en Debian, PuTTY en Windows
- Adaptador serial (o serial-USB) conectado al puerto de consola del router

> ⚠️ Esta es una tecnica de recuperacion con acceso fisico al equipo. Implica que **la seguridad fisica del router es parte de su seguridad logica**: quien alcanza el puerto de consola puede saltarse el password.

## Procedimiento realizado

Equipo del laboratorio: **Cisco 2901/K9** (IOS 15.2(4)M4, ROMMON 15.0(1r)M16). Consola desde Debian con `picocom -b 9600 /dev/ttyUSB0`.

| Paso | Dónde | Comando | Qué hace |
|---|---|---|---|
| 1 | IOS | `show version` | Anotar el registro de configuración original (`0x2102`) |
| 2 | Arranque | *break* durante la carga del IOS | Entrar a `rommon 1 >` |
| 3 | ROMMON | `confreg 0x2142` | Bit 6 encendido: al arrancar se ignora la NVRAM |
| 4 | ROMMON | `reset` | Reinicia; el IOS carga sin `startup-config` |
| 5 | IOS | `n` al diálogo inicial · `enable` | Entra a privilegiado sin password |
| 6 | IOS | `copy startup-config running-config` | Recupera la configuración vieja (sin activar el password) |
| 7 | IOS | `enable secret nuevoPassword` | Nuevo password |
| 8 | IOS | `config-register 0x2102` | Restaurar el registro para que vuelva a leer la NVRAM |
| 9 | IOS | `copy running-config startup-config` · `reload` | Guardar y reiniciar con el nuevo password |

> ⭐ El registro `0x2142` no borra nada: solo hace que el arranque **ignore** `startup-config`. Por eso el paso 6 puede recuperar la configuración completa y luego solo se sobreescribe el password. Si se omite el paso 8, el router seguirá ignorando la NVRAM en cada reinicio.

### Evidencia

![[practica-6-rommon-1-confreg.png]]
*picocom conectado por consola; `confreg 0x2142` en ROMMON*

![[practica-6-rommon-2-reset.png]]
*`reset` y arranque del bootstrap: se identifica el modelo (CISCO2901/K9, 512 MB)*

![[practica-6-rommon-3-arranque.png]]
*Descompresión de la imagen del IOS*

![[practica-6-rommon-4-dialogo-inicial.png]]
*Inventario del hardware y diálogo de configuración inicial (se responde `no`)*

![[practica-6-rommon-5-config-ignorada.png]]
*Mensaje `%SYS-6-STARTUP_CONFIG_IGNORED`: la NVRAM se ignoró por el registro*

![[practica-6-rommon-6-nuevo-password.png]]
*`enable secret`, `config-register 0x2102`, `copy running-config startup-config` y `reload`*

## Relacionadas

- [[Sistema operativo IOS de cisco]] — secuencia de arranque, NVRAM y `startup-config`, que es lo que ROMMON esquiva
- [[Practica 2 - Router fisico Cisco 2514]] — la otra practica sobre equipo fisico del laboratorio, misma conexion por consola
- [[Normas de seguridad fisica]] — por que el acceso fisico al equipo derrumba el control logico
