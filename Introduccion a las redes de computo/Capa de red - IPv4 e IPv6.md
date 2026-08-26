---
materia: Introduccion a las redes de computo
semestre: 2
tipo: concepto
tags: [redes, capa-de-red, ip, ipv6]
modulo: 8
---

# Capa de red — IPv4 e IPv6

> Módulo 8 — clase del 23/04/2026

También conocida como **capa 3**. El protocolo protagonista es **IP**, tanto IPv4 como IPv6.

## La analogía del sobre

La capa 3 es como ponerle a una carta la información de entrega: dirección, código postal, ciudad, remitente, receptor.

> **La capa 3 es el paquete en sí, no el contenido del paquete.**

## Funciones

Proporciona servicios para que los dispositivos finales intercambien datos:

- **Direccionamiento** de terminales
- **Encapsulamiento** — al bajar desde la capa de aplicación, los datos se encapsulan y se convierten a bits para ser transmitidos
- **Enrutamiento** (routing) — en IPv4 e IPv6
- **Desencapsulamiento** en el destino

La **capa 4** (transporte) es la encargada de que el paquete se entregue y de decidir qué medio se va a ocupar.

## Características de IP

IP está diseñado para tener una **sobrecarga baja**. Eso implica tres renuncias:

### Sin conexión
No establece ninguna conexión con el destino antes de enviar el paquete.
- No se necesita información de control, sincronización ni confirmaciones
- El destino recibirá el paquete, pero IP no envía notificaciones previas

### Mejor esfuerzo (*best effort*)
No garantiza la entrega del paquete, pero hará lo posible por entregarlo.
- **No es confiable**: no puede administrar ni corregir paquetes
- No puede retransmitir después de un error
- No puede reordenar paquetes fuera de secuencia
- **Depende de otros protocolos** (TCP) para esas funciones

### Independencia de medios
No necesita saber por qué medio va a viajar; solamente pone la etiqueta. La capa de red establece una **unidad máxima de transmisión (MTU)**.

## Las tres limitaciones de IPv4

1. **No hay suficientes direcciones disponibles**
2. **Falta de conectividad de extremo a extremo** — para que IPv4 sobreviviera se crearon las direcciones privadas y **NAT**
3. Es en realidad una **solución temporal que nunca se fue**

## Por eso se inventó IPv6

- Mayor espacio de direcciones
- Manejo mejorado de paquetes
- **Elimina la necesidad de NAT**

## Relacionadas

- [[Protocolos y modelos]] — el encapsulamiento y el modelo por capas que esta nota da por sabidos
- [[Direccionamiento IP con clases]] — el detalle de IPv4, en [[Enrutamiento basico]]
- [[CIDR y VLSM]] — la respuesta intermedia al agotamiento de IPv4
