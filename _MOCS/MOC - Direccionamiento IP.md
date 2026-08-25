---
tipo: moc
hilo: direccionamiento-ip
tags:
  - moc
  - redes
  - ip
  - binario
  - subnetting
semestres:
  - 1
  - 2
  - 3
sr-due: 2026-09-30
sr-interval: 39
sr-ease: 230
---
#review
# MOC — Direccionamiento IP

Documento de estudio corrido. Reúne el contenido completo de las notas del hilo, en orden cronológico de la carrera, para poder estudiarlo como una sola cosa.

**Cadena:** [[Sistemas numericos]] (sem. 1) → [[Capa de red - IPv4 e IPv6]] (sem. 2) → [[Direccionamiento IP con clases]] (sem. 3) → [[CIDR y VLSM]] (sem. 3)

> Las notas originales siguen vivas en sus carpetas de materia. Este archivo es una copia consolidada: si corriges algo aquí, corrígelo también en la nota fuente.

## El arco del hilo

El hilo más práctico de todos, y el que más se cae en examen si falta una pieza. La herramienta (binario y hexadecimal) llega un año y medio antes que su uso real. Después el arco es una sola historia: IPv4 se diseñó con sobrecarga baja y espacio limitado → las clases A/B/C repartieron ese espacio en bloques fijos → los bloques fijos desperdiciaban direcciones →  [[CIDR y VLSM]] quitaron las clases → e IPv6 resolvió el fondo del problema. Cada nota es un capítulo del agotamiento de IPv4.

---

## 1. Sistemas numéricos

*Fuente: [[Sistemas numericos]] — Organización de computadoras, sem. 1*

**Sistema numérico:** conjunto de símbolos llamados dígitos, más las operaciones que se pueden hacer entre ellos.

Los cuatro usados en ciberseguridad y tecnologías: **decimal, binario, octal y hexadecimal**.

### Tipos de representación

- **Posicional** — la posición de cada dígito indica su peso o relevancia. Cuanto más a la derecha, menos significativo.
- **Polinomial** — el valor del número expresado como suma de potencias de la base.

### Los cuatro sistemas

| Sistema | Base | Dígitos | Nota |
|---|---|---|---|
| **Decimal** | 10 | 0-9 | El habitual |
| **Binario** | 2 | 0, 1 (bits) | Presencia o ausencia de voltaje |
| **Octal** | 8 | 0-7 | Base = 2³ |
| **Hexadecimal** | 16 | 0-9, A-F | Base = 2⁴ |

### Por qué octal y hexadecimal

**Ambas son potencias exactas de 2**, y ahí está toda la razón de su existencia: reducen el número de dígitos necesarios para representar números binarios sin perder la correspondencia directa con los bits.

- Octal: 1 dígito = 3 bits
- Hexadecimal: 1 dígito = 4 bits

Por eso el hexadecimal se usa como **notación abreviada de números binarios**.

### Sobre el binario

- 1 byte = 8 bits
- 32 y 64 bits: cantidad de bits con los que puede trabajar un procesador
- Imágenes de 8 y 16 bits (profundidad de color)

Ver también [[Conversion entre bases]] y [[Aritmetica binaria]].

---

## 2. Capa de red — IPv4 e IPv6

*Fuente: [[Capa de red - IPv4 e IPv6]] — Introducción a las redes de cómputo, sem. 2 (módulo 8)*

> Módulo 8 — clase del 23/04/2026

También conocida como **capa 3**. El protocolo protagonista es **IP**, tanto IPv4 como IPv6.

### La analogía del sobre

La capa 3 es como ponerle a una carta la información de entrega: dirección, código postal, ciudad, remitente, receptor.

> **La capa 3 es el paquete en sí, no el contenido del paquete.**

### Funciones

Proporciona servicios para que los dispositivos finales intercambien datos:

- **Direccionamiento** de terminales
- **Encapsulamiento** — al bajar desde la capa de aplicación, los datos se encapsulan y se convierten a bits para ser transmitidos
- **Enrutamiento** (routing) — en IPv4 e IPv6
- **Desencapsulamiento** en el destino

La **capa 4** (transporte) es la encargada de que el paquete se entregue y de decidir qué medio se va a ocupar.

### Características de IP

IP está diseñado para tener una **sobrecarga baja**. Eso implica tres renuncias:

#### Sin conexión
No establece ninguna conexión con el destino antes de enviar el paquete.
- No se necesita información de control, sincronización ni confirmaciones
- El destino recibirá el paquete, pero IP no envía notificaciones previas

#### Mejor esfuerzo (*best effort*)
No garantiza la entrega del paquete, pero hará lo posible por entregarlo.
- **No es confiable**: no puede administrar ni corregir paquetes
- No puede retransmitir después de un error
- No puede reordenar paquetes fuera de secuencia
- **Depende de otros protocolos** (TCP) para esas funciones

#### Independencia de medios
No necesita saber por qué medio va a viajar; solamente pone la etiqueta. La capa de red establece una **unidad máxima de transmisión (MTU)**.

### Las tres limitaciones de IPv4

1. **No hay suficientes direcciones disponibles**
2. **Falta de conectividad de extremo a extremo** — para que IPv4 sobreviviera se crearon las direcciones privadas y **NAT**
3. Es en realidad una **solución temporal que nunca se fue**

### Por eso se inventó IPv6

- Mayor espacio de direcciones
- Manejo mejorado de paquetes
- **Elimina la necesidad de NAT**

---

## 3. Direccionamiento IP con clases

*Fuente: [[Direccionamiento IP con clases]] — Enrutamiento básico, sem. 3*

En **1981** se modificaron las clases de IPv4 para crear las tres clases de redes A, B y C. Esto se conoce como **direccionamiento IP con clase** (*classful*).

Cada clase tiene un **identificador único** en los bits iniciales.

### Las cinco clases

| Clase | Primer octeto | Bits iniciales | Uso |
|---|---|---|---|
| **A** | 1 – 126 | `0` | Redes muy grandes |
| **B** | 128 – 191 | `10` | Redes medianas |
| **C** | 192 – 223 | `110` | Redes pequeñas |
| **D** | 224 – 239 | `1110` | **Multicast** |
| **E** | 240 – 255 | `1111` | **Experimental** |

> Nota: el rango 127.x.x.x está reservado para *loopback*, por eso la clase A termina en 126.

### Máscaras por defecto

| Clase | Máscara | Porción de red |
|---|---|---|
| A | 255.0.0.0 | Primer octeto |
| B | 255.255.0.0 | Dos primeros octetos |
| C | 255.255.255.0 | Tres primeros octetos |

### Cómo identificar la clase rápido

Mirar el **primer octeto en decimal** y compararlo con la tabla. En binario, contar los bits `1` iniciales antes del primer `0`.

Ejercicios: [[Tarea 1 - Separar red y host]], [[Tarea 2 - Clases IP y direcciones de red]].

---

## 4. CIDR y VLSM

*Fuente: [[CIDR y VLSM]] — Enrutamiento básico, sem. 3*

### El problema

Con la reducción rápida de direcciones IP disponibles, el sistema de clases resultó insostenible: repartía bloques de tamaño fijo (A, B, C) que rara vez coincidían con lo que una organización necesitaba realmente.

### CIDR

**Classless Inter-Domain Routing** — enrutamiento entre dominios sin clase.

Nace una década después de los protocolos con clase. Permite subredes **sin clase** y jugar con más libertad con las direcciones IP, logrando un uso más eficiente del espacio de IPv4.

CIDR utiliza máscaras de longitud variable: **VLSM**.

### VLSM

**Variable Length Subnet Masking** — enmascaramiento para subredes de longitud variable.

Resuelve el problema del [[Enmascaramiento y subnetting|subnetting clásico]]: permite que cada subred tenga la máscara que le corresponde según su tamaño real, en lugar de imponer un tamaño único a todas.

### Consecuencia para los protocolos

Con CIDR, la clase ya no está implícita en la dirección. Por eso los protocolos de enrutamiento **classless** (RIPv2, OSPF, EIGRP, BGP) deben propagar **la máscara junto con la dirección de red**, algo que RIPv1 no hacía. Ver [[Conceptos fundamentales de enrutamiento]].

---

## Relacionadas

- [[00 - Indice]] — el índice maestro con todos los hilos
- [[Enmascaramiento y subnetting]] — la práctica del cálculo
- [[Conceptos fundamentales de enrutamiento]] — qué hace el router con la dirección una vez que sabe leerla: decidir el siguiente salto
- [[Protocolos y modelos]] — dónde encaja IP dentro del modelo por capas
- [[Examen segundo parcial - Redes]] — este hilo aplicado en el examen práctico: esquema de direccionamiento y configuración de routers
