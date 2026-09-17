---
materia: Enrutamiento basico
semestre: 3
tipo: concepto
tags:
  - redes
  - ip
  - cidr
  - vlsm
sr-due: 2026-09-18
sr-interval: 2
sr-ease: 226
---
#review 

# CIDR y VLSM

## El problema

Con la reducción rápida de direcciones IP disponibles, el sistema de clases resultó insostenible: repartía bloques de tamaño fijo (A, B, C) que rara vez coincidían con lo que una organización necesitaba realmente.

## CIDR

**Classless Inter-Domain Routing** — enrutamiento entre dominios sin clase.

Nace una década después de los protocolos con clase. Permite subredes **sin clase** y jugar con más libertad con las direcciones IP, logrando un uso más eficiente del espacio de IPv4.

CIDR utiliza máscaras de longitud variable: **VLSM**.

## VLSM

**Variable Length Subnet Masking** — enmascaramiento para subredes de longitud variable.

Resuelve el problema del [[Enmascaramiento y subnetting|subnetting clásico]]: permite que cada subred tenga la máscara que le corresponde según su tamaño real, en lugar de imponer un tamaño único a todas.

## Consecuencia para los protocolos

Con CIDR, la clase ya no está implícita en la dirección. Por eso los protocolos de enrutamiento **classless** (RIPv2, OSPF, EIGRP, BGP) deben propagar **la máscara junto con la dirección de red**, algo que RIPv1 no hacía. Ver [[Conceptos fundamentales de enrutamiento]].



![[Pasted image 20260826095441.png]]


## En resumen
Básicamente **CIDR es la notación/regla del juego**, y **VLSM es la estrategia de aplicar esa regla con máscaras de distinto tamaño dentro de la misma red para no desperdiciar IPs**
## Relacionadas

- [[Capa de red - IPv4 e IPv6]] — CIDR y NAT como parches al agotamiento de IPv4
- [[Direccionamiento IP con clases]] — el sistema de bloques fijos A, B y C que CIDR vino a sustituir
