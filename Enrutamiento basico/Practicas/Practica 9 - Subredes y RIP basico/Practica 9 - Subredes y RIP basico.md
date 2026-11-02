---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, rip, subnetting]
---

# Practica 9 - Subredes y RIP basico

> ⚠️ Pendiente: solo el enunciado, sin resolver.
> Enunciado: ![[Practica 9 - Subredes y RIP basico (enunciado).docx]] (nombre del archivo del profesor: «Practica 9 Evalucion RIP1»; titulo interno: «Division en subredes, configuracion de interfaces y configuracion basica de RIP»)

Tres routers (HQ, Branch 1, Branch 2) y cinco PCs. Hay que dividir 192.168.1.0/24 con **subneteo tradicional** (todas las subredes del mismo tamaño) y luego levantar RIP.

## Tareas

1. Calcular las subredes y llenar la tabla de direccionamiento
2. Armar la topologia en Packet Tracer con etiquetas de interfaz, IP y subred
3. Hostnames, MOTD y `enable` con contraseña «cisco»
4. Direccionar PCs e interfaces FastEthernet y seriales
5. `clock rate 64000` en las seriales DCE
6. RIP en los tres routers
7. Verificar con `show ip route`, `show ip protocols` y `ping`

> ⚠️ El MOTD que pide el enunciado dice «#Hola, esta es la practica numero 7#»: es un resto de una version anterior del documento. Confirmar con el profesor si se deja asi o con el 9.

## Relacionadas

- [[Practica 3 - VLSM]] y [[Enmascaramiento y subnetting]] — el calculo de subredes
- [[Practica 8 - Protocolo RIP]] — los comandos de RIP paso a paso
