---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, eigrp, enrutamiento-dinamico]
---

# Practica 11 - Configuracion basica de EIGRP

> ⚠️ Pendiente: solo el enunciado, sin resolver.
> Enunciado: ![[Practica 11 - Configuracion basica de EIGRP (enunciado).pdf]] (es la practica de laboratorio 9.6.1 de Cisco CCNA Exploration)
> Actividad de Packet Tracer: `Practica 11 - Configuracion basica de EIGRP.pka`, en esta misma carpeta.
> Teoria de respaldo: ![[Presentacion 5 - EIGRP.pptx]]

Tres routers (R1, R2, R3) con LANs en 172.16.1.0/24, 172.16.2.0/24 y 192.168.1.0/24, enlaces seriales /30 y una loopback en R2 (10.1.1.1/30) que simula el ISP.

## Tareas

1. Preparar la red y borrar configuraciones previas
2. Configuracion basica (hostname, sin busqueda DNS, contrasenas, MOTD)
3. Direccionar interfaces seriales y Ethernet; verificar con `show ip interface brief`
4. EIGRP en R1: `router eigrp 1`, `network 172.16.0.0`
5. EIGRP en R2 y R3
6. Verificar vecinos y operacion de EIGRP
7. Examinar las rutas EIGRP en las tablas de enrutamiento
8. Configurar las metricas EIGRP
9. Sucesores y distancias factibles
10. Determinar si R1 es sucesor factible para una ruta de R2
11. Examinar la tabla de topologia
12. Desactivar el resumen automatico (`no auto-summary`)
13. Configurar el resumen manual
14. Configurar y propagar una ruta estatica por defecto
15. Documentacion
16. Limpieza

## Relacionadas

- [[Practica 12 - Redistribucion RIP y EIGRP]] — la siguiente practica junta EIGRP con RIP
- [[Practica 5 - Rutas estaticas flotantes]] — la AD de EIGRP (90 interna, 170 externa) frente a las estaticas
