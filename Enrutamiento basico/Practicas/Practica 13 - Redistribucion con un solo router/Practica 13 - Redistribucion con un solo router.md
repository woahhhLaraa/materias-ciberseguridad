---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, rip, eigrp, redistribucion, md5]
---

# Practica 13 - Redistribucion con un solo router

> ⚠️ Pendiente: solo el enunciado, sin resolver.
> Enunciado: ![[Practica 13 - Redistribucion con un solo router (enunciado).docx]] (titulo original: «Practica 13 Enrutamiento con doble protocolo V2»)

Cinco routers con mascaras /24. R0 y R1 en RIPv2, R3 y R4 en EIGRP 100, y **R2 corre los dos protocolos** y hace toda la redistribucion.

## Tareas

1. Tabla de direccionamiento (5 routers, 5 PCs)
2. Capturas de configuracion de los cinco routers
3. RIPv2 en R0 y R1
4. EIGRP 100 en R3 y R4
5. R2 con RIP (anuncia 192.1.10.0 y 192.1.2.0) y con EIGRP (solo 192.1.20.0); comprobar con `ping` que cada zona se ve por dentro pero no entre si
6. En R2, redistribuir EIGRP en RIP (`redistribute eigrp 100 metric n`, n tipicamente 2) y anunciar en RIP las redes EIGRP conectadas
7. En R2, redistribuir RIP en EIGRP con la metrica leida de `show interfaces` en la serial 192.1.20.1
8. Tabla de `ping` y conclusion
9. Autenticacion MD5 en los tres routers EIGRP con `key chain`

> ⚠️ El enunciado trae erratas en los comandos de la tarea 9: «MD%» por MD5, `Key-string` y `ip autehentication mode eigrp 100 EIGRP_KEY`. Lo correcto en IOS es `ip authentication mode eigrp 100 md5` y `ip authentication key-chain eigrp 100 EIGRP_KEY`, ambos en la interfaz.

## Relacionadas

- [[Practica 12 - Redistribucion RIP y EIGRP]] — la version con dos routers frontera
