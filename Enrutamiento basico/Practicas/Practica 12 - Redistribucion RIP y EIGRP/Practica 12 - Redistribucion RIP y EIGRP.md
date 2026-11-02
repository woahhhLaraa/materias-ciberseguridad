---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, rip, eigrp, redistribucion]
---

# Practica 12 - Redistribucion RIP y EIGRP

> ⚠️ Pendiente: solo el enunciado, sin resolver.
> Enunciado: ![[Practica 12 - Redistribucion RIP y EIGRP (enunciado).docx]] (titulo original: «Practica 12 Enrutamiento con doble protocolo»)
> Habia una segunda copia del enunciado identica salvo el titulo, que decia por error «Practica 10 validacion de enrutamiento con RIP»; se desecho.

Cuatro routers con mascaras /24: R0 y R1 en RIPv2, R2 y R3 en EIGRP (AS 100, ID 2.2.2.2 y 3.3.3.3). Cada frontera redistribuye en un sentido.

## Tareas

1. Llenar la tabla de direccionamiento (4 routers, 4 PCs)
2. Capturas de configuracion de los cuatro routers
3. RIPv2 en R0 y R1
4. EIGRP 100 en R2 y R3
5. Redistribuir EIGRP en RIP desde R0: `redistribute eigrp 100 metric 2` (metrica en saltos, 1–16)
6. Redistribuir RIP en EIGRP desde R2: leer con `show interfaces serial x/x/x` el ancho de banda, retraso, carga, confiabilidad y MTU, y usarlos en `redistribute rip metric P1 P2 P3 P4 P5`
7. Tabla de `ping` entre todas las PCs y conclusion: ¿hay redistribucion?

## Relacionadas

- [[Practica 11 - Configuracion basica de EIGRP]] — base de EIGRP
- [[Practica 13 - Redistribucion con un solo router]] — la misma idea con un solo router frontera
