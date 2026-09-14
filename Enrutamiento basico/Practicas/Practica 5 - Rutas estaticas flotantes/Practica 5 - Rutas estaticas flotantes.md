---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, rutas-estaticas, rutas-flotantes, distancia-administrativa]
---

# Practica 5 - Rutas estaticas flotantes

> ⚠️ Nota pendiente de desarrollar: solo esta cargado el enunciado, todavia sin resolver ni capturas.
> Enunciado original en esta misma carpeta: ![[Practica 5 - Rutas estaticas flotantes.docx]]

Practica de laboratorio sobre **rutas estaticas flotantes**: rutas de respaldo que solo entran en la tabla de ruteo cuando la ruta principal cae. El mecanismo es la **distancia administrativa**: se le asigna a la ruta de respaldo un valor mas alto que el de la principal, y el router prefiere siempre la de distancia menor.

## Objetivos

- Configurar la informacion IP en las interfaces Ethernet y seriales (WAN) del router
- Configurar la informacion IP en las PC
- Configurar rutas estaticas
- Configurar rutas estaticas flotantes
- Verificar rutas de envio de paquetes

## Topologia

Cuatro routers (R0, R1, R2, R3) con dos caminos posibles entre PC0 y PC1: el directo por R0 — R1 — R2 y el alterno por R0 — R3 — R2. El direccionamiento es libre, a elegir entre 192.168.1.0/24 … 192.168.6.0/24.

## Desarrollo

1. Rutas estaticas en R0, R1 y R2 para comunicar PC0 con PC1 — **sin** asignar rutas a R3
2. Verificar con `ping`
3. Eliminar el enlace R1 — R2 y comprobar que se pierde la comunicacion
4. Configurar las rutas adicionales en R0, R3 y R2 con **distancia administrativa entre 95 y 150** en las de R0 y R2 (las flotantes)
5. Verificar con `ping` que la comunicacion se reestablece por el camino alterno
6. Restablecer el enlace R1 — R2 y comprobar con `ping -t` que la comunicacion se mantiene
7. Eliminar el enlace R2 — R3 para confirmar que el trafico volvio al camino principal
8. Restablecer R2 — R3, volver a eliminar R1 — R2 y observar el `ping -t` durante la conmutacion

⭐ El paso 8 es el que demuestra la idea: con la pantalla de PC0 a la vista se ve cuantos paquetes se pierden mientras el router descarta la ruta principal y promueve la flotante.

## Entregables

Tabla de comandos `ip route` (red destino, mascara, IP de salida o interfaz) para el escenario base y otra para el escenario flotante, con la columna de distancia administrativa, mas los resultados de cada `ping` y las conclusiones.

## Relacionadas

- [[Practica 4 - Rutas estaticas]] — la ruta estatica simple que esta practica convierte en respaldo
- [[Conceptos fundamentales de enrutamiento]] — la tabla de ruteo y el criterio con que el router elige una ruta sobre otra
- [[Enrutamiento basico (materia)]] — indice de la materia a la que pertenece esta practica
