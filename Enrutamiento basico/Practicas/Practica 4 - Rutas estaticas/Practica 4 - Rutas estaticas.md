---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, rutas-estaticas, sumarizacion, enrutamiento]
---

# Practica 4 - Rutas estaticas

> ⚠️ Nota pendiente de desarrollar: solo esta cargado el enunciado, todavia sin resolver ni capturas.
> Enunciado original en esta misma carpeta: ![[Practica 4 - Rutas estaticas.docx]]

Practica de laboratorio sobre configuracion de **rutas estaticas** en una topologia de tres routers, cerrando con **sumarizacion**. Es la continuacion natural de [[Practica 1 - Configuracion inicial del router]]: una vez que el router tiene nombre, contrasenas y direccionamiento, lo siguiente es ensenarle rutas que no conoce.

## Objetivos

- Configurar la informacion IP en routers y PCs
- Configurar rutas estaticas en los routers para garantizar la conectividad
- Verificar la configuracion de las rutas y la conectividad
- Configurar rutas estaticas con sumarizacion

## Topologia y direccionamiento

Tres routers en serie (R1 — R2 — R3), cada uno con una PC en su segmento Ethernet.

| Dispositivo | Interfaz | Direccion IP | Mascara | Gateway |
|---|---|---|---|---|
| R1 | Fa0/0 | 172.16.3.1 | 255.255.255.0 | N/A |
| R1 | S0/0/0 | 172.16.2.1 | 255.255.255.0 | N/A |
| R2 | Fa0/0 | 172.16.1.1 | 255.255.255.0 | N/A |
| R2 | S0/0/0 | 172.16.2.2 | 255.255.255.0 | N/A |
| R2 | S0/0/1 | 192.168.1.2 | 255.255.255.0 | N/A |
| R3 | Fa0/0 | 192.168.2.1 | 255.255.255.0 | N/A |
| R3 | S0/0/1 | 192.168.1.1 | 255.255.255.0 | N/A |
| PC1 | NIC | 172.16.3.10 | 255.255.255.0 | 172.16.3.1 |
| PC2 | NIC | 172.16.1.10 | 255.255.255.0 | 172.16.1.1 |
| PC3 | NIC | 192.168.2.10 | 255.255.255.0 | 192.168.2.1 |

## Entregables

1. Capturas de `show ip route` con las rutas estaticas configuradas
2. Tabla de ping entre PC1, PC2 y PC3
3. Sumarizacion en R3: sustituir todas sus rutas estaticas por `ip route 172.16.0.0 255.255.252.0 192.168.1.2`
4. Capturas de `show ip route` y tabla de ping despues de sumarizar
5. Conclusiones

⭐ La mascara `255.255.252.0` de la ruta sumarizada es el punto del ejercicio: agrupa 172.16.0.0 — 172.16.3.255 en una sola entrada. Ver [[Enmascaramiento y subnetting]] para el calculo.

## Relacionadas

- [[Conceptos fundamentales de enrutamiento]] — la ruta estatica frente a la dinamica, y por que un router solo conoce sus redes conectadas
- [[Enmascaramiento y subnetting]] — el calculo que sustenta la ruta sumarizada
- [[Practica 5 - Rutas estaticas flotantes]] — continua con la misma tecnica, anadiendo distancia administrativa para tener una ruta de respaldo
- [[Enrutamiento basico (materia)]] — indice de la materia a la que pertenece esta practica
