---
materia: Enrutamiento basico
semestre: 3
tipo: ejercicios
tags: [examen, parcial, subnetting, vlsm, recuperar]
---

# Ejercicios de «Recuperar» — sesión 4

Calentamiento de 10–15 min, **sin apuntes ni calculadora**, sobre las sesiones 2 y 3. Antes de resolver cada uno, di qué tipo de problema es. En los VLSM, el número de hosts de cada LAN ya incluye la interfaz del router. Lo que falles va al [[Temario primer parcial#Registro de fallos|registro de fallos]].

## Calentamiento (lo que pide el temario)

1. **165.42.219.77/19** → clase, red con clase, subred y porción de host.
2. VLSM de **192.168.25.0/24**: LANs de 14, 70 y 30 hosts, más 1 enlace punto a punto. Tabla completa: red, máscara, rango utilizable y broadcast. (Ojo con los números.)

## Reserva (solo si sobra tiempo o fallaste uno de arriba)

3. VLSM de **10.5.8.0/23**: LANs de 33, 120 y 100 hosts, más 1 enlace punto a punto. Tabla completa.
4. **45.117.200.3** con máscara **255.255.240.0** → clase, red con clase, subred y porción de host.

## Pendiente de la sesión 3

5. Explica en voz alta, sin mirar: una PC tiene IP 192.168.40.70, gateway 192.168.40.65 y máscara **255.255.255.0**, pero su LAN real es 192.168.40.64/27. ¿Por qué el ping al gateway funciona y el ping a 192.168.40.10 (otra LAN, detrás del mismo router) no?

---
---
---

## Soluciones

**1.** Clase B (128–191) → red con clase 165.42.0.0. /19 = 255.255.224.0. Tercer octeto: 219 = `11011011` AND `11100000` = `11000000` = 192 → **subred 165.42.192.0**. Host: 219 − 192 = 27 → **0.0.27.77**.

**2.** Ordena de mayor a menor: 70, 30, 14. La trampa es la contraria a la de la sesión 3: 30 **sí** cabe en /27 (2⁵ − 2 = 30) y 14 **sí** cabe en /28 (2⁴ − 2 = 14). No hace falta subir de bloque.

| LAN | Hosts | Red | Máscara | Rango | Broadcast |
|---|---|---|---|---|---|
| 70 | 126 | 192.168.25.0/25 | 255.255.255.128 | .1 – .126 | .127 |
| 30 | 30 | 192.168.25.128/27 | 255.255.255.224 | .129 – .158 | .159 |
| 14 | 14 | 192.168.25.160/28 | 255.255.255.240 | .161 – .174 | .175 |
| Enlace | 2 | 192.168.25.176/30 | 255.255.255.252 | .177 – .178 | .179 |

Libre desde 192.168.25.180.

**3.** La /23 va de 10.5.8.0 a 10.5.9.255. Ordena: 120, 100, 33. Las dos primeras son /25 (126); 33 no cabe en /27 (30), así que va en /26.

| LAN | Hosts | Red | Máscara | Rango | Broadcast |
|---|---|---|---|---|---|
| 120 | 126 | 10.5.8.0/25 | 255.255.255.128 | 10.5.8.1 – 10.5.8.126 | 10.5.8.127 |
| 100 | 126 | 10.5.8.128/25 | 255.255.255.128 | 10.5.8.129 – 10.5.8.254 | 10.5.8.255 |
| 33 | 62 | 10.5.9.0/26 | 255.255.255.192 | 10.5.9.1 – 10.5.9.62 | 10.5.9.63 |
| Enlace | 2 | 10.5.9.64/30 | 255.255.255.252 | 10.5.9.65 – 10.5.9.66 | 10.5.9.67 |

Libre desde 10.5.9.68. Que la red base sea de clase A no cambia nada: en VLSM solo importa el bloque que te dan (/23).

**4.** Clase A (1–126) → red con clase 45.0.0.0. 255.255.240.0 = /20. El segundo octeto queda entero (117). Tercer octeto: 200 = `11001000` AND `11110000` = `11000000` = 192 → **subred 45.117.192.0**. Host: 200 − 192 = 8 → **0.0.8.3**.

**5.** Con /24, la PC cree que todo 192.168.40.x es local.
- Ping al gateway (.65): **sí.** Está en su LAN real; ARP responde.
- Ping a 192.168.40.10: **no.** La PC lo ve como local, así que hace ARP en vez de mandarlo al gateway, y nadie en su LAN real tiene esa IP.
- Debería tener **255.255.255.224 (/27)**.
- *Recuerda la excepción:* con `ip proxy-arp` (activado por defecto en Cisco) el router puede contestar ese ARP y el ping funcionaría. En el examen, la respuesta esperada es la de arriba.

> Índice de la materia: [[Enrutamiento basico (materia)]]
