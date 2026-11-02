---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, rip, enrutamiento-dinamico]
---

# Practica 8 - Protocolo RIP

> ⚠️ Pendiente: solo el enunciado, sin resolver.
> Enunciado: ![[Practica 8 - Protocolo RIP (enunciado).docx]] (adaptado de ccnadesdecero.es; las imagenes de topologia y direccionamiento son enlaces a ese sitio)
> Lectura de apoyo: ![[6.4 Protocolo RIP.docx]]

Tres routers (R1, R2, R3) con las redes 192.168.1.0 a 192.168.5.0, sin rutas estaticas. Se arranca con RIPv1 y se pasa a RIPv2. El reporte se arma con 13 actividades de capturas.

## Tareas

1. Configuracion inicial de la red; al menos una PC por LAN; `ping` de R1 a R3 (falla, aun no hay enrutamiento)
2. `router rip` en los tres routers; probar `no router rip` en R2 y volver a habilitarlo
3. Anunciar las redes conectadas con `network` (con clase)
4. Verificar con `show ip protocols`
5. Tablas de ruteo con `show ip route | begin Gateway`
6. `version 2` en R1 y luego en R2 y R3
7. Validar la sumarizacion automatica y quitarla con `no auto-summary`
8. Interfaces pasivas: `passive-interface g0/0` en los tres routers
9. Ruta por defecto en R1 hacia 209.165.200.224/27 y propagarla con `default-information originate`

## Relacionadas

- [[Practica 9 - Subredes y RIP basico]] — RIP sobre un direccionamiento que hay que calcular
- [[Practica 10 - RIPv2 con VLSM]] — RIPv2 con seis routers y VLSM
