---
materia: Enrutamiento basico
semestre: 3
profesor: Balderas
tipo: practica
tags: [packet-tracer, cisco, vlsm, subnetting, direccionamiento-ip, rip]
---

# Practica 3 - VLSM

> Practica de VLSM (Mascara de Subred de Longitud Variable). Originales en esta misma carpeta:
> ![[Practica 3 - VLSM.docx]] — enunciado del profesor
> ![[Practica 3 - VLSM (resuelta).pdf]] — entrega resuelta
> Objetivo: configurar y probar redes VLSM y practicar la asignacion de direcciones IP a las interfaces de un enrutador.

Aplicacion directa de [[CIDR y VLSM]]. La regla que gobierna toda la practica: **asignar las subredes de mayor a menor numero de hosts**. Si se asignan en desorden quedan huecos que ya no alcanzan para las redes grandes.

Recordatorio del calculo: una subred con `n` bits de host da `2^n` direcciones y `2^n - 2` utilizables (se restan la de red y la de broadcast). El router tambien consume una direccion utilizable por interfaz, por eso el profesor cuenta *hosts + 2 + 1*.

## Ejercicio 1

### Diagrama 1

![[practica3-vlsm-diagrama-1.png]]

Un router `Router-PT-Empty` con cinco interfaces Gigabit (`Gig0/0` a `Gig4/0`), cada una hacia un switch con dos PCs.

### Actividad 1 — Tabla VLSM de 192.168.40.0/24

Orden de asignacion por tamano: Red 4 (100) → Red 2 (40) → Red 5 (22) → Red 3 (10) → Red 1 (5).

| Red | Hosts pedidos | Necesarias (hosts+2+1) | Direccion de red / mascara | IP inicial | IP final | Broadcast |
|---|---|---|---|---|---|---|
| Red 4 | 100 | 103 | `192.168.40.0/25` — 255.255.255.128 | 192.168.40.1 | 192.168.40.126 | 192.168.40.127 |
| Red 2 | 40 | 43 | `192.168.40.128/26` — 255.255.255.192 | 192.168.40.129 | 192.168.40.190 | 192.168.40.191 |
| Red 5 | 22 | 25 | `192.168.40.192/27` — 255.255.255.224 | 192.168.40.193 | 192.168.40.222 | 192.168.40.223 |
| Red 3 | 10 | 13 | `192.168.40.224/28` — 255.255.255.240 | 192.168.40.225 | 192.168.40.238 | 192.168.40.239 |
| Red 1 | 5 | 8 | `192.168.40.240/29` — 255.255.255.248 | 192.168.40.241 | 192.168.40.246 | 192.168.40.247 |

Sobra el bloque `192.168.40.248/29` (.248 a .255) sin asignar.

> ⚠️ La Red 1 queda **justa**: /29 da 6 direcciones utilizables y se necesitan exactamente 6 (5 hosts + la interfaz del router). No cabe ni un dispositivo mas. Si el profesor pide margen de crecimiento, subir a /28 — pero entonces hay que rehacer la tabla desde la Red 3, porque el bloque siguiente se recorre.

Presentada en orden de diagrama (como suele pedirse en el reporte):

| Red | Total de host | Direccion de la red/mascara | IP inicial | IP final |
|---|---|---|---|---|
| Red 1 | 5 | 192.168.40.240/29 | 192.168.40.241 | 192.168.40.246 |
| Red 2 | 40 | 192.168.40.128/26 | 192.168.40.129 | 192.168.40.190 |
| Red 3 | 10 | 192.168.40.224/28 | 192.168.40.225 | 192.168.40.238 |
| Red 4 | 100 | 192.168.40.0/25 | 192.168.40.1 | 192.168.40.126 |
| Red 5 | 22 | 192.168.40.192/27 | 192.168.40.193 | 192.168.40.222 |

### Actividad 2 — Construccion y configuracion en Packet Tracer

Asignacion de interfaces (Red N → `Gig(N-1)/0`) y direcciones. Criterio: **la interfaz del router toma la primera IP utilizable** (gateway), la primera PC la segunda y la segunda PC la ultima del rango.

> ⚠️ La practica pide literalmente "una con la direccion inicial y otra con la direccion final". Aqui la inicial la ocupa el gateway, que es la convencion habitual. Si el profesor quiere la PC en la primera IP, mueve la interfaz del router a la **ultima** utilizable y recorre las PCs una posicion.

| Red | Interfaz | IP del router (gateway) | PC A | PC B | Mascara |
|---|---|---|---|---|---|
| Red 1 | Gig0/0 | 192.168.40.241 | 192.168.40.242 | 192.168.40.246 | 255.255.255.248 |
| Red 2 | Gig1/0 | 192.168.40.129 | 192.168.40.130 | 192.168.40.190 | 255.255.255.192 |
| Red 3 | Gig2/0 | 192.168.40.225 | 192.168.40.226 | 192.168.40.238 | 255.255.255.240 |
| Red 4 | Gig3/0 | 192.168.40.1 | 192.168.40.2 | 192.168.40.126 | 255.255.255.128 |
| Red 5 | Gig4/0 | 192.168.40.193 | 192.168.40.194 | 192.168.40.222 | 255.255.255.224 |

Cada PC lleva como **default gateway** la IP del router de su propia subred.

Configuracion del router (el bloque de nombre, contrasenas, cifrado y mensaje es el mismo de [[Practica 1 - Configuracion inicial del router]]):

```
enable
configure terminal

hostname R1

enable secret itsasecret
line console 0
 password letmein
 login
 exit
banner motd #Acceso no autorizado estrictamente prohibido.#
service password-encryption

interface GigabitEthernet0/0
 ip address 192.168.40.241 255.255.255.248
 no shutdown
 exit
interface GigabitEthernet1/0
 ip address 192.168.40.129 255.255.255.192
 no shutdown
 exit
interface GigabitEthernet2/0
 ip address 192.168.40.225 255.255.255.240
 no shutdown
 exit
interface GigabitEthernet3/0
 ip address 192.168.40.1 255.255.255.128
 no shutdown
 exit
interface GigabitEthernet4/0
 ip address 192.168.40.193 255.255.255.224
 no shutdown
 exit
end
copy running-config startup-config
```

> `no shutdown` es imprescindible: las interfaces de un router arrancan administrativamente apagadas. Sin el, `show ip interface brief` reporta `administratively down` y nada responde. Es el error mas comun de esta practica.

Captura para el reporte:

```
R1# show ip interface brief
```

Las cinco interfaces Gig deben aparecer con `Status: up` y `Protocol: up`.

### Actividad 3 — Pruebas de ping

Desde la PC A de la Red 2 (192.168.40.130):

| Destino | IP destino | Resultado esperado |
|---|---|---|
| Otra PC de la red 2 | 192.168.40.190 | ✅ Responde. Mismo segmento, se resuelve por ARP sin pasar por el router |
| Puerto ETH de la red 2 | 192.168.40.129 | ✅ Responde. Es su propio gateway, directamente conectado |
| Puerto ETH de la red 4 | 192.168.40.1 | ✅ Responde. Otra interfaz del mismo router, alcanzable por ruta conectada |
| Una PC de la red 4 | 192.168.40.2 | ✅ Responde. El router encamina entre sus redes directamente conectadas |

Todo funciona **sin protocolo de enrutamiento**: hay un solo router y todas las subredes estan directamente conectadas a el. Por eso la practica aclara que no se requiere configurar un protocolo de ruteo en este ejercicio.

> El primer ping puede fallar por el tiempo de la peticion ARP. Se cuenta el resultado a partir del segundo intento.

### Actividad 4 — Errores provocados

**Parte A: IP fuera de rango.** A la PC A de la Red 2 (que deberia ser 192.168.40.130/26) se le pone, por ejemplo, `192.168.40.200`.

| Ping | Resultado | Por que |
|---|---|---|
| A otra PC de su subred (.190) | ❌ Falla | Con la mascara /26, .200 pertenece a otro bloque. La PC cree que el destino es remoto y lo manda al gateway |
| Al default gateway (.129) | ❌ Falla | Y el gateway configurado tampoco cae dentro de su red aparente, asi que el paquete no tiene salida. Packet Tracer responde `Destination host unreachable` o `Request timed out` |

Ademas la IP .200 invade el rango de la Red 5, lo que puede generar un conflicto de direcciones.

**Parte B: IP correcta pero mascara /24.** Se restituye 192.168.40.130 y se cambia la mascara a 255.255.255.0.

| Ping | Resultado | Por que |
|---|---|---|
| Al gateway propio (.129) | ✅ Responde | Sigue estando dentro de lo que la PC considera local |
| A PCs de otras subredes (.2, .194...) | ❌ Falla | Con /24 la PC cree que **toda** 192.168.40.0/24 es su segmento local: en vez de entregar el paquete al router, envia un ARP directo al destino. Ese ARP no cruza el router y nadie contesta |
| A interfaces del router de otras redes (.1, .193...) | ❌ Falla | Por lo mismo: intenta ARP local en lugar de enrutar |

**Conclusion.** La mascara no es un adorno de la IP: es lo que le dice al host **que es local y que es remoto**, y por tanto cuando usar ARP y cuando usar el gateway. Una mascara mal puesta rompe la comunicacion entre subredes sin tocar una sola direccion IP, y el sintoma enganosa: el ping al propio gateway sigue funcionando, asi que "parece" que la red esta bien configurada. En VLSM esto es critico porque cada subred lleva mascara distinta y no se puede copiar la de al lado.

## Ejercicio 2

### Diagrama 2

![[practica3-vlsm-diagrama-2.png]]

Tres routers en triangulo. Red base: **192.168.1.0/24**.

| Router | Red LAN | Enlaces seriales |
|---|---|---|
| R1 | Red 1 (20 hosts) | Enlace A hacia R2, Enlace C hacia R3 |
| R2 | Red 3 (50 hosts) | Enlace A hacia R1, Enlace B hacia R3 |
| R3 | Red 2 (100 hosts) | Enlace B hacia R2, Enlace C hacia R1 |

### Actividad 5 — Tabla VLSM de 192.168.1.0/24

Orden de asignacion: Red 2 (100) → Red 3 (50) → Red 1 (20) → los tres enlaces seriales.

| Red | # de host | Necesarias | Direccion de la red/mascara | IP inicial | IP final | Broadcast |
|---|---|---|---|---|---|---|
| Red 2 | 100 | 103 | `192.168.1.0/25` — 255.255.255.128 | 192.168.1.1 | 192.168.1.126 | 192.168.1.127 |
| Red 3 | 50 | 53 | `192.168.1.128/26` — 255.255.255.192 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
| Red 1 | 20 | 23 | `192.168.1.192/27` — 255.255.255.224 | 192.168.1.193 | 192.168.1.222 | 192.168.1.223 |
| Enlace A | 2 | 4 | `192.168.1.224/30` — 255.255.255.252 | 192.168.1.225 | 192.168.1.226 | 192.168.1.227 |
| Enlace B | 2 | 4 | `192.168.1.228/30` — 255.255.255.252 | 192.168.1.229 | 192.168.1.230 | 192.168.1.231 |
| Enlace C | 2 | 4 | `192.168.1.232/30` — 255.255.255.252 | 192.168.1.233 | 192.168.1.234 | 192.168.1.235 |

Sobra `192.168.1.236` a `192.168.1.255` (20 direcciones).

> Los enlaces punto a punto entre routers llevan **/30**: 4 direcciones, 2 utilizables, exactamente las dos interfaces seriales. Usar /24 o /29 en un enlace serial desperdicia decenas de direcciones y es lo que la practica quiere que se evite.

### Actividad 6 — Construccion y configuracion

Direccionamiento (misma convencion: gateway en la primera utilizable):

| Segmento | Interfaz | IP | Mascara |
|---|---|---|---|
| Red 1 (R1) | Gig0/0 | 192.168.1.193 | 255.255.255.224 |
| Red 3 (R2) | Gig0/0 | 192.168.1.129 | 255.255.255.192 |
| Red 2 (R3) | Gig0/0 | 192.168.1.1 | 255.255.255.128 |
| Enlace A | R1 Se0/0/0 | 192.168.1.225 | 255.255.255.252 |
| Enlace A | R2 Se0/0/0 | 192.168.1.226 | 255.255.255.252 |
| Enlace B | R2 Se0/0/1 | 192.168.1.229 | 255.255.255.252 |
| Enlace B | R3 Se0/0/1 | 192.168.1.230 | 255.255.255.252 |
| Enlace C | R3 Se0/0/0 | 192.168.1.233 | 255.255.255.252 |
| Enlace C | R1 Se0/0/1 | 192.168.1.234 | 255.255.255.252 |

PCs: en Red 1, .194 y .222; en Red 3, .130 y .190; en Red 2, .2 y .126. Cada una con su gateway correspondiente.

**R1:**

```
enable
configure terminal
hostname R1
enable secret itsasecret
line console 0
 password letmein
 login
 exit
banner motd #Acceso no autorizado estrictamente prohibido.#
service password-encryption

interface GigabitEthernet0/0
 ip address 192.168.1.193 255.255.255.224
 no shutdown
 exit
interface Serial0/0/0
 ip address 192.168.1.225 255.255.255.252
 clock rate 64000
 no shutdown
 exit
interface Serial0/0/1
 ip address 192.168.1.234 255.255.255.252
 no shutdown
 exit
end
```

**R2:**

```
enable
configure terminal
hostname R2
enable secret itsasecret
line console 0
 password letmein
 login
 exit
banner motd #Acceso no autorizado estrictamente prohibido.#
service password-encryption

interface GigabitEthernet0/0
 ip address 192.168.1.129 255.255.255.192
 no shutdown
 exit
interface Serial0/0/0
 ip address 192.168.1.226 255.255.255.252
 no shutdown
 exit
interface Serial0/0/1
 ip address 192.168.1.229 255.255.255.252
 clock rate 64000
 no shutdown
 exit
end
```

**R3:**

```
enable
configure terminal
hostname R3
enable secret itsasecret
line console 0
 password letmein
 login
 exit
banner motd #Acceso no autorizado estrictamente prohibido.#
service password-encryption

interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.128
 no shutdown
 exit
interface Serial0/0/0
 ip address 192.168.1.233 255.255.255.252
 clock rate 64000
 no shutdown
 exit
interface Serial0/0/1
 ip address 192.168.1.230 255.255.255.252
 no shutdown
 exit
end
```

> `clock rate` va **solo en el extremo DCE** de cada enlace serial — el lado donde Packet Tracer dibuja el reloj en el cable. Si se pone en el equivocado o se omite, la linea queda `down` aunque las IPs esten bien. Verificar con `show controllers serial 0/0/0`, que indica si el extremo es DCE o DTE.

Captura para el reporte, en los tres routers:

```
R# show ip interface brief
```

### Actividad 7 — Pings **antes** de RIP

Desde una PC de la Red 2 (192.168.1.2, colgada de R3):

| Destino | IP destino | Resultado esperado |
|---|---|---|
| Otra PC de la red 2 | 192.168.1.126 | ✅ Responde. Mismo segmento |
| Puerto ETH de la red 2 | 192.168.1.1 | ✅ Responde. Su gateway, directamente conectado |
| Puerto ETH de la red 3 | 192.168.1.129 | ❌ Falla. Esta en R2; R3 no tiene ruta hacia esa red |
| Una PC de la red 3 | 192.168.1.130 | ❌ Falla. Por lo mismo |

**Por que.** Sin protocolo de enrutamiento cada router conoce unicamente sus redes **directamente conectadas** (las que aparecen con `C` en `show ip route`). R3 no sabe que existe 192.168.1.128/26 y descarta el paquete devolviendo `Destination host unreachable` desde el propio gateway. Esta es la diferencia con el Ejercicio 1, donde un unico router tenia todas las subredes conectadas.

### Actividad 8 — Errores provocados

Identica al Ejercicio 1 y con las mismas conclusiones:

- **IP fuera de rango:** falla el ping a la PC vecina y al gateway; con la mascara puesta, esa direccion pertenece a otro bloque y la PC intenta enrutar lo que era local.
- **Mascara a /24:** el ping al propio gateway sigue funcionando, pero se rompe todo lo que sale de la subred, porque la PC cree que 192.168.1.0/24 entero es local y hace ARP en vez de entregar al router.

La conclusion vale doble en este ejercicio: con VLSM conviven /25, /26, /27 y /30 sobre la **misma** red 192.168.1.0. Un host con /24 "ve" como locales las tres LAN y los tres enlaces a la vez, y por eso deja de funcionar todo salvo lo que tiene fisicamente al lado.

### Actividad 9 — Habilitar RIPv2 y repetir

En **cada uno** de los tres routers, anunciando las redes directamente conectadas:

**R1:**

```
configure terminal
router rip
 version 2
 no auto-summary
 network 192.168.1.192
 network 192.168.1.224
 network 192.168.1.232
 end
```

**R2:**

```
configure terminal
router rip
 version 2
 no auto-summary
 network 192.168.1.128
 network 192.168.1.224
 network 192.168.1.228
 end
```

**R3:**

```
configure terminal
router rip
 version 2
 no auto-summary
 network 192.168.1.0
 network 192.168.1.228
 network 192.168.1.232
 end
```

> ⭐ `version 2` y `no auto-summary` son **obligatorios** aqui. RIPv1 no transporta la mascara en sus actualizaciones y resumiria todo a la classful 192.168.1.0/24, con lo que el direccionamiento VLSM de la practica dejaria de funcionar. RIPv2 es *classless*: envia la mascara junto con cada red y por eso soporta subredes de longitud variable. Es exactamente la razon por la que la practica pide RIP **2** y no RIP.
>
> `network` se escribe con la direccion de red, no con la de la interfaz. IOS la ajusta sola al limite classful al mostrarla, lo cual es normal.

Pings **despues** de RIPv2, desde la misma PC de la Red 2 (192.168.1.2):

| Destino | IP destino | Resultado esperado |
|---|---|---|
| Otra PC de la red 2 | 192.168.1.126 | ✅ Responde (igual que antes) |
| Puerto ETH de la red 2 | 192.168.1.1 | ✅ Responde (igual que antes) |
| Puerto ETH de la red 3 | 192.168.1.129 | ✅ **Ahora si responde** |
| Una PC de la red 3 | 192.168.1.130 | ✅ **Ahora si responde** |

Comprobacion en el router:

```
R3# show ip route
R3# show ip protocols
```

En `show ip route` deben aparecer entradas marcadas con `R` (aprendidas por RIP) hacia las redes de los otros dos routers, ademas de las `C` y `L` locales.

> RIP tarda hasta 30 segundos en converger tras habilitarlo. Si el primer ping falla, esperar y repetir antes de dar por mala la configuracion.

**Conclusion del ejercicio.** VLSM resuelve el *reparto* eficiente del espacio de direcciones, pero no comunica nada por si solo: subredes bien calculadas y bien puestas siguen aisladas mientras cada router conozca solo lo que tiene enchufado. El protocolo de enrutamiento es la pieza que reparte ese conocimiento — y tiene que ser uno *classless* (RIPv2, no RIPv1) o deshace el trabajo de VLSM al resumir las mascaras.

## Entregables del reporte

1. Tabla de asignacion VLSM del Ejercicio 1 (Actividad 1)
2. Captura de `show ip interface brief` del router del Ejercicio 1 (Actividad 2)
3. Tabla de resultados de ping (Actividad 3)
4. Resultados y conclusiones de los errores provocados (Actividad 4)
5. Tabla de asignacion VLSM del Ejercicio 2 (Actividad 5)
6. Capturas de `show ip interface brief` de los tres routers (Actividad 6)
7. Tabla de ping antes de RIP (Actividad 7)
8. Resultados y conclusiones de los errores provocados (Actividad 8)
9. Tabla de ping despues de RIPv2 (Actividad 9)

## Relacionadas

- [[CIDR y VLSM]] — la teoria que esta practica aplica; el metodo de asignar de mayor a menor viene de ahi
- [[Enmascaramiento y subnetting]] — el calculo de mascaras y rangos que sustenta las dos tablas
- [[Practica 1 - Configuracion inicial del router]] — el bloque de nombre, contrasenas y banner que aqui se reutiliza
- [[Conceptos fundamentales de enrutamiento]] — por que un router solo conoce sus redes conectadas hasta que se habilita un protocolo como RIP
