---
materia: Enrutamiento basico
semestre: 3
tipo: ejercicios
tags: [examen, parcial, subnetting, vlsm, practica]
---

# Ejercicios extra — sesión 3

Serie mezclada: 3 ejercicios de cada tipo de la sesión 3, sin etiquetar. Antes de resolver cada uno, di qué tipo de problema es. Sin calculadora. En los VLSM, el número de hosts de cada LAN ya incluye la interfaz del router.

1. **150.83.77.200/21** → clase, red con clase, subred y porción de host.
2. Red clase C que se divide en **6 subredes** → máscara (decimal y prefijo) y hosts utilizables por subred.
3. Una PC tiene IP 192.168.1.50, máscara **255.255.0.0** y gateway 192.168.1.1. La LAN real es 192.168.1.0/24; el router también tiene la LAN 192.168.5.0/24 y salida a internet. ¿Qué pings responden y por qué? a) 192.168.1.1 b) 192.168.1.77 c) 192.168.5.20 d) 8.8.8.8
4. `10111111.00000011.11111010.00010001` → pásala a decimal y di clase, máscara por defecto y dirección de red.
5. VLSM de **192.168.10.0/24**: LANs de 60, 25 y 12 hosts, más 2 enlaces punto a punto. Tabla completa: red, máscara, rango utilizable y broadcast.
6. **12.190.33.7** con máscara **255.248.0.0** → clase, red con clase, subred y porción de host.
7. **126.200.5.9** → clase, máscara por defecto y dirección de red.
8. Una PC tiene IP 172.16.10.70, máscara **255.255.255.224** y gateway 172.16.10.1. La LAN real es 172.16.10.0/24. ¿Qué pings responden? a) 172.16.10.1 b) 172.16.10.80 c) 172.16.10.200 d) 8.8.8.8
9. Red clase A que se divide en **1000 subredes** → máscara y hosts por subred.
10. VLSM de **192.168.77.0/24**: LANs de 31, 62, 15 y 6 hosts, más 1 enlace punto a punto. Tabla completa. (Ojo con los números.)
11. **233.14.6.1** → clase, máscara por defecto y dirección de red.
12. **199.77.14.93/28** → clase, red con clase, subred y porción de host.
13. PC-A tiene 192.168.40.130 y gateway 192.168.40.129; su LAN real es 192.168.40.128/26. Ping al gateway: sí. Ping a 10.1.1.1: sí. Ping a 192.168.40.20 (otra LAN, detrás del mismo router): **no**. ¿Qué máscara tiene mal puesta PC-A, probablemente? ¿Cuál debería tener?
14. Red clase B que se divide en **50 subredes** → máscara y hosts por subred.
15. VLSM de **172.20.0.0/22**: LANs de 500, 200, 100 y 50 hosts, más 3 enlaces punto a punto. Tabla completa.

---
---
---

## Soluciones

**1.** Clase B (128–191) → red con clase 150.83.0.0. /21 = 255.255.248.0. Tercer octeto: 77 = `01001101` AND `11111000` = `01001000` = 72 → **subred 150.83.72.0**. Host: 77 − 72 = 5 → **0.0.5.200**.

**2.** 2³ = 8 ≥ 6 → 3 bits prestados → **/27 = 255.255.255.224**. Hosts: 2⁵ − 2 = **30**.

**3.** Con /16, la PC cree que todo 192.168.x.x es local.
- a) **Sí.** El gateway está en su LAN real; ARP responde.
- b) **Sí.** Misma LAN real.
- c) **No.** La PC cree que 192.168.5.20 es local, así que hace ARP en vez de mandarlo al gateway, y nadie en su LAN tiene esa IP.
- d) **Sí.** 8.8.8.8 queda fuera de 192.168.0.0/16, así que lo manda al gateway con normalidad.
- La máscara demasiado ancha solo rompe los destinos que caen dentro del rango ampliado.
- *Nota:* los routers Cisco traen `ip proxy-arp` activado por defecto: el router puede contestar ese ARP con su MAC y el ping c) acabaría funcionando. Si en Packet Tracer te funciona, esa es la razón. En el examen, la respuesta esperada es la del temario (falla por ARP).

**4.** 191.3.250.17. Empieza por `10` → **clase B**, **/16 (255.255.0.0)**, red **191.3.0.0**.

**5.**

| LAN | Hosts | Red | Máscara | Rango | Broadcast |
|---|---|---|---|---|---|
| 60 | 62 | 192.168.10.0/26 | 255.255.255.192 | .1 – .62 | .63 |
| 25 | 30 | 192.168.10.64/27 | 255.255.255.224 | .65 – .94 | .95 |
| 12 | 14 | 192.168.10.96/28 | 255.255.255.240 | .97 – .110 | .111 |
| Enlace 1 | 2 | 192.168.10.112/30 | 255.255.255.252 | .113 – .114 | .115 |
| Enlace 2 | 2 | 192.168.10.116/30 | 255.255.255.252 | .117 – .118 | .119 |

Libre desde 192.168.10.120.

**6.** Clase A → red con clase 12.0.0.0. 255.248.0.0 = /13. Segundo octeto: 190 = `10111110` AND `11111000` = `10111000` = 184 → **subred 12.184.0.0**. Host: 190 − 184 = 6 → **0.6.33.7**.

**7.** **Clase A** (126 es la última de la A; 127 es loopback), **/8**, red **126.0.0.0**.

**8.** Con /27, la PC cree que su red es 172.16.10.64 – .95.
- a) **No.** El gateway .1 queda fuera de su "red", así que la PC no puede alcanzarlo: para ella el gateway no es local.
- b) **Sí.** .80 cae dentro de .64 – .95 y además está en la LAN real.
- c) **No.** .200 está en la LAN real, pero la PC lo ve como remoto y lo mandaría a un gateway que no alcanza.
- d) **No.** Por lo mismo.
- Es el caso contrario al 3: con una máscara demasiado estrecha **sí falla el ping al gateway**.

**9.** 2¹⁰ = 1024 ≥ 1000 → 10 bits prestados → **/18 = 255.255.192.0**. Hosts: 2¹⁴ − 2 = **16 382**.

**10.** Ordena de mayor a menor: 62, 31, 15, 6. La trampa: 31 no cabe en /27 (30) y 15 no cabe en /28 (14).

| LAN | Hosts | Red | Máscara | Rango | Broadcast |
|---|---|---|---|---|---|
| 62 | 62 | 192.168.77.0/26 | 255.255.255.192 | .1 – .62 | .63 |
| 31 | 62 | 192.168.77.64/26 | 255.255.255.192 | .65 – .126 | .127 |
| 15 | 30 | 192.168.77.128/27 | 255.255.255.224 | .129 – .158 | .159 |
| 6 | 6 | 192.168.77.160/29 | 255.255.255.248 | .161 – .166 | .167 |
| Enlace | 2 | 192.168.77.168/30 | 255.255.255.252 | .169 – .170 | .171 |

**11.** 233 = `11101001`, empieza por `1110` → **clase D (multicast)**. No tiene máscara por defecto ni se divide en red y host.

**12.** Clase C → red con clase 199.77.14.0. /28 = 255.255.255.240. Cuarto octeto: 93 = `01011101` AND `11110000` = `01010000` = 80 → **subred 199.77.14.80**. Host: 93 − 80 = **0.0.0.13**.

**13.** Debería tener **255.255.255.192 (/26)**. Probablemente tiene **255.255.255.0 (/24)**: así 192.168.40.20 le parece local, hace ARP en vez de mandarlo al gateway, y falla. El gateway (.129) sigue siendo local, así que ese ping funciona, y 10.1.1.1 sigue siendo remoto, así que se envía al gateway. Cualquier máscara de /24 o más corta produce el mismo síntoma; la /24 es la más probable porque es la de la red base de la Práctica 3.

**14.** 2⁶ = 64 ≥ 50 → 6 bits prestados → **/22 = 255.255.252.0**. Hosts: 2¹⁰ − 2 = **1022**.

**15.** La /22 va de 172.20.0.0 a 172.20.3.255.

| LAN | Hosts | Red | Máscara | Rango | Broadcast |
|---|---|---|---|---|---|
| 500 | 510 | 172.20.0.0/23 | 255.255.254.0 | 172.20.0.1 – 172.20.1.254 | 172.20.1.255 |
| 200 | 254 | 172.20.2.0/24 | 255.255.255.0 | 172.20.2.1 – 172.20.2.254 | 172.20.2.255 |
| 100 | 126 | 172.20.3.0/25 | 255.255.255.128 | 172.20.3.1 – 172.20.3.126 | 172.20.3.127 |
| 50 | 62 | 172.20.3.128/26 | 255.255.255.192 | 172.20.3.129 – 172.20.3.190 | 172.20.3.191 |
| Enlace 1 | 2 | 172.20.3.192/30 | 255.255.255.252 | .193 – .194 | .195 |
| Enlace 2 | 2 | 172.20.3.196/30 | 255.255.255.252 | .197 – .198 | .199 |
| Enlace 3 | 2 | 172.20.3.200/30 | 255.255.255.252 | .201 – .202 | .203 |

La /23 cruza del tercer octeto 0 al 1: el rango de hosts incluye 172.20.0.255 y 172.20.1.0, y **sí son utilizables**.

> Índice de la materia: [[Enrutamiento basico (materia)]]
