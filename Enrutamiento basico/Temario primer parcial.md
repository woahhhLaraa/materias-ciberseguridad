---
materia: Enrutamiento basico
semestre: 3
tipo: temario
fecha-examen: 2026-10-08
tags: [examen, parcial, redes, enrutamiento]
---

# Temario — primer parcial de Enrutamiento básico

**Examen: jueves 8 de octubre de 2026.**

Abarca hasta la [[Practica 5 - Rutas estaticas flotantes|Práctica 5]] (dicho por el profesor Balderas). Armado a partir de las prácticas 1–5, las tareas, las notas de clase y las presentaciones 0, 1 y 2.

## Temario oficial (entregado el 3 de octubre)

| Bloque oficial | Subtema | Dónde está aquí | Estado |
|---|---|---|---|
| **Subredes** | Ventajas de la creación de subredes | Tema 3 | Nuevo, añadido |
| | Creación de subredes | Tema 3 | Cubierto |
| | CIDR y VLSM | Tema 3 | Cubierto |
| **Routers** | Funciones de los routers | Tema 4 | Nuevo, añadido |
| | Tipos de routers | Tema 4 | ⚠️ Tarea sin material |
| | Sistema operativo de dispositivos de red | Tema 4 | Cubierto |
| | Configuración de acceso remoto seguro | Tema 4 | Nuevo: SSH |
| | Archivos imagen y de configuración | Tema 4 | Configuración cubierta; imagen, nueva |
| **Conceptos de FHRP** | FHRP, opciones de FHRP, HSRP | Tema 7 | Sube de peso: un tercio del examen |

**No figuran en el oficial:** clases IPv4 (tema 2, base de subredes), rutas estáticas (tema 5), distancia administrativa y flotantes (tema 6), CDP. Como el profesor dijo «hasta la Práctica 5», se mantienen en versión compacta hasta confirmarlo.

**Material 2025** (carpeta `Material 2025/`, recibido el 3 de octubre): `Enrutamiento básico1 Examen.pptx` es la misma Presentación 1, y `Enrutamiento básico2.pptx` es la misma Presentación 2. Lo único nuevo son `2025_3 Protocolo ARP.docx` y `2025_4 MAC_IP.docx` (tema 8).

## 1. Fundamentos de enrutamiento

Ver [[Conceptos fundamentales de enrutamiento]].

- Paquete, enrutamiento salto a salto, tabla de ruteo.
- Estático vs dinámico; protocolos dinámicos: RIP, EIGRP, OSPF, IS-IS, BGP.
- Protocolos *enrutados* vs *de enrutamiento*.
- Sistema Autónomo: una sola administración, número 1–65535.
- Redes directamente conectadas vs remotas; salto (hop); métrica (RIP usa conteo de saltos).

## 2. Direccionamiento IPv4 con clases

Ver [[Funcionamiento de IPv4]] y [[Direccionamiento IP con clases]].

| Clase | 1er octeto | Bits iniciales | Máscara | Hosts |
|---|---|---|---|---|
| A | 1–126 | `0` | /8 | 16 777 214 |
| B | 128–191 | `10` | /16 | 65 534 |
| C | 192–223 | `110` | /24 | 254 |
| D | 224–239 | `1110` | — | multicast |
| E | 240–255 | `1111` | — | experimental |

127.x.x.x reservado para loopback.

Ejercicios tipo [[Tarea 1 - Separar red y host|Tarea 1]] y [[Tarea 2 - Clases IP y direcciones de red|Tarea 2]]: separar red y host, pasar a binario/hex, identificar la clase por bits, dirección de red con la máscara por defecto.

## 3. Subnetting, CIDR y VLSM

Ver [[Enmascaramiento y subnetting]] y [[CIDR y VLSM]].

- **Ventajas (oficial), según la Presentación 1:**
  - **Subnetting:** mejora la organización, la seguridad y la eficiencia en el uso de las IP, porque **reduce el tamaño de los dominios de broadcast** y limita el desperdicio de direcciones. Su limitación es que todas las subredes salen del mismo tamaño.
  - **VLSM:** aprovecha mucho mejor las direcciones cuando las subredes necesitan tamaños distintos. Requiere un protocolo que soporte VLSM (OSPF, EIGRP, RIPv2).
  - **CIDR:** da escalabilidad (enrutamiento más eficiente en Internet) y flexibilidad (elimina las clases), y permite la agregación (la sumarización reduce las entradas de la tabla).

- **Subredes:** 2ⁿ ≥ subredes requeridas (n = bits prestados).
- **Hosts utilizables:** 2ʰ − 2 (se restan red y broadcast).
- **Tarea 3:** dado el nº de subredes → máscara y hosts por subred. Ej.: clase B, 300 subredes → /25 → 126 hosts.
- **Ejercicio 2:** IP + máscara → clase, red, subred (AND lógico) y host. Ej.: 178.224.123.5/20 → subred 178.224.112.0, host 0.0.11.5.
- **Subnetting vs VLSM vs CIDR:** subnetting clásico = subredes iguales; VLSM = máscara según tamaño; CIDR = notación sin clases y sumarización.
- **VLSM ([[Practica 3 - VLSM|Práctica 3]]):** asignar de mayor a menor; enlaces punto a punto con /30. Ej.: 192.168.40.0/24 con LANs de 100/40/22/10/5 hosts → /25, /26, /27, /28, /29.
- Entender por qué una máscara mal puesta en una PC deja funcionar el ping a su gateway pero rompe el tráfico hacia otras subredes (cree que el destino es local y hace ARP en vez de enviarlo al gateway).

## 4. Cisco IOS y configuración inicial (prácticas 1 y 2)

Ver [[Sistema operativo IOS de cisco]], [[Practica 1 - Configuracion inicial del router|Práctica 1]] y [[Practica 2 - Router fisico Cisco 2514|Práctica 2]].

- **Modos:** EXEC usuario → EXEC privilegiado → config global → config de línea / de interfaz. Navegación: `enable`, `configure terminal`, `exit`, `end`.
- **Configuración básica:**
  - `hostname`
  - `line console 0` → `password` + `login` (sin `login` no pide contraseña)
  - `line vty 0 4`
  - `enable password` / `enable secret`
  - `service password-encryption`
  - `banner motd` (aviso legal, nunca "welcome")
- **Memorias:** `running-config` (RAM) vs `startup-config` (NVRAM); guardar con `copy run start`; flash = imagen IOS (el `.bin` más grande).
- **Verificación:** `show running-config`, `show ip interface brief`, `show ip route`, `show flash`.
- **Arranque:** POST → bootstrap → IOS de flash a RAM → startup-config (o modo setup).
- ⭐ **Cisco 2514:** no tiene FastEthernet, sus puertos LAN son Ethernet AUI de 10 Mbps. Si el examen pregunta cuántas FastEthernet tiene → **0**, y justificarlo.

### Lo añadido por el temario oficial

- **Funciones (oficial):**
  - **Del router:** determinar la mejor ruta (tabla de ruteo) y **reenviar** el paquete. Reenviar implica volver a encapsularlo y sacarlo por la interfaz correcta. Ver [[Enrutamiento basico/Notas en curso|Notas en curso]] y el tema 8.
  - **Del IOS** (diapositiva 36 de la Presentación 1): seguridad, enrutamiento, QoS, direccionamiento, administración de recursos e interfaz. La imagen de esa diapositiva dice «Orientación» en lugar de «Enrutamiento»; parece una mala traducción de *routing*.
  - **Partes del sistema operativo:** shell (usuario, CLI o GUI), núcleo (hardware) y hardware.
- ⚠️ **Tipos de routers:** la diapositiva 70 dice solo «tarea: Tipos de enrutadores», sin contenido. Hay que investigarlo y redactarlo (pendiente abajo).
- **Acceso remoto seguro (oficial):**
  - **Métodos de acceso:** consola (fuera de banda, para la configuración inicial), auxiliar (fuera de banda, por línea telefónica; los switches Catalyst no tienen puerto auxiliar) y terminal virtual (Telnet o SSH).
  - **SSH frente a Telnet:** SSH cifra los datos y autentica de forma más segura; Telnet viaja en texto plano.
  - **Configuración de SSH** (no viene en las presentaciones; es el estándar de Cisco):
    ```
    ip domain-name ejemplo.com
    crypto key generate rsa        ! 1024 bits o más
    username admin secret <clave>
    ip ssh version 2
    line vty 0 4
     login local
     transport input ssh            ! bloquea Telnet
    ```
- **Archivos imagen (oficial):**
  - Se ven con `show flash`.
  - Nomenclatura, por ejemplo `c1900-universalk9-mz.SPA.152-4.M3.bin`:
    - `c1900` = hardware.
    - `universalk9` = imagen universal con criptografía; `universalk9_npe` = sin criptografía fuerte, para países que la prohíben.
    - `m` = se ejecuta en RAM (f flash, r ROM, l reubicable).
    - `z` = comprimida con zip (x = mzip).
    - `SPA` = firmada digitalmente por Cisco.
    - `152-4.M3` = versión 15.2, nuevas funciones 4, mantenimiento extendido 3.
    - `.bin` = binario ejecutable.
  - **ISR G2** (1900, 2900 y 3900): traen una sola imagen universal y las funciones se activan con licencia (PAK).
  - **Requisitos:** los 1900 y 2900 piden 256 MB de flash y 512 MB de RAM; el 3900, 256 MB de flash y 1 GB de RAM.
  - **Trenes de IOS:** EM (mantenimiento extendido, para despliegues largos) y T (las funciones más recientes).
- **Archivos de configuración:** running-config en RAM y startup-config en NVRAM; `copy running-config startup-config`; el arranque la copia de NVRAM a RAM.

## 5. Rutas estáticas ([[Practica 4 - Rutas estaticas|Práctica 4]])

> No figura en el temario oficial. Se queda en versión compacta hasta que el profesor lo confirme.

- Sintaxis: `ip route <red> <máscara> {<ip-siguiente-salto> | <interfaz-salida>}`
- Siguiente salto vs interfaz de salida. En la tabla: `S` estática, `C` conectada, `L` local.
- **Sumarización:** 172.16.1.0, .2.0 y .3.0 /24 → `ip route 172.16.0.0 255.255.252.0 192.168.1.2` (/22).
- **Ruta por defecto:** `ip route 0.0.0.0 0.0.0.0 <ip|interfaz>`
- `clock rate 64000` solo en el extremo DCE del serial.
- `show cdp neighbors` / `show cdp neighbors detail`.

## 6. Distancia administrativa y rutas flotantes ([[Practica 5 - Rutas estaticas flotantes|Práctica 5]])

> No figura en el temario oficial. Se queda en versión compacta hasta que el profesor lo confirme.

- AD: valor de 0 a 255; el router prefiere la menor; si empatan, decide la métrica. Es local (no se anuncia) y ajustable.

| Origen de la ruta | AD |
|---|---|
| Directamente conectada | 0 |
| Estática | 1 |
| EIGRP | 90 |
| OSPF | 110 |
| RIP | 120 |
| Desconocida / inválida | 255 |

- **Ruta flotante:** `ip route <red> <máscara> <salto> <AD>`, con AD mayor que la principal (en la práctica, entre 95 y 150). No aparece en la tabla mientras la principal está activa.
- Ejemplo del profesor: si la principal es EIGRP (AD 90), la flotante lleva AD 95.

## 7. FHRP (oficial: un tercio del examen)

Visto el 17 de septiembre junto con la distancia administrativa (ver [[Enrutamiento basico/Notas en curso|Notas en curso]]) y en la Presentación 2 (diapositivas 7–23). Ninguna práctica hasta la 5 lo usa.

- **Problema:** si falla el único gateway, los hosts quedan aislados.
- **Solución:** un **router virtual** con IP y MAC virtuales compartidas. Las PCs usan la IP virtual como gateway. Si cae el router que reenvía, el de reserva asume la IP y la MAC virtuales, y los hosts no notan el cambio.
- **Opciones de FHRP** (las 7 de la presentación):

| Opción | En una línea |
|---|---|
| HSRP | De Cisco: un router activo y uno de reserva |
| HSRP para IPv6 | Lo mismo que HSRP, en IPv6 |
| VRRPv2 | Estándar abierto, solo IPv4; elige un router maestro |
| VRRPv3 | Estándar abierto, IPv4 e IPv6; más escalable y multiproveedor |
| GLBP | De Cisco: redundancia más **balanceo de carga** |
| GLBP para IPv6 | Lo mismo que GLBP, en IPv6 |
| IRDP | Heredado (RFC 1256); los hosts descubren los routers por ICMP |

- **HSRP:**
  - Prioridad por defecto **100**, rango **0–255**; gana la más alta. Si empatan, gana la IP más alta.
  - **Preempt:** sin `standby preempt`, un router con más prioridad que vuelve a arrancar **no** recupera el rol de activo.
  - Ejemplo de la presentación: R1 con 150 y preempt, R2 con 100. R1 es el activo; si cae y vuelve, recupera el rol.
  - **Temporizadores:** Hello cada 3 s y Hold de 10 s. No bajar de 1 s y 4 s.
  - **Estados:** Initial → Learn → Listen → Speak → Standby → Active.
  - **Configuración** (en la interfaz LAN):
    ```
    standby 1 ip 192.168.1.254
    standby 1 priority 150
    standby 1 preempt
    ```
    Se verifica con `show standby brief`.

## 8. ARP y MAC/IP (material nuevo; no figura en el oficial)

Viene de `Material 2025/2025_3 Protocolo ARP.docx` y `2025_4 MAC_IP.docx`. Sirve de apoyo para «funciones de los routers». Peso bajo hasta que el profesor confirme si entra.

- **MAC e IP salto a salto:** las IP de origen y destino **no cambian** de extremo a extremo. Las MAC **cambian en cada salto**: la MAC de origen es la de la interfaz que envía y la de destino, la del siguiente salto.
- **ARP:**
  - Resuelve IPv4 → MAC con una solicitud por broadcast a `FF-FF-FF-FF-FF-FF` y una respuesta unicast. En la trama Ethernet, el tipo es `0x806`.
  - La tabla vive **en RAM** y es temporal (Windows borra una entrada entre 15 y 45 s después de su último uso). Las entradas estáticas no caducan.
  - Comandos: `show ip arp` en el router y `arp -a` en la PC.
  - En IPv6 se usa ICMPv6 ND.
- **Problemas:**
  - Los broadcasts ARP saturan la red.
  - **ARP spoofing / envenenamiento:** el atacante responde con su MAC haciéndose pasar por el gateway. Se mitiga con DAI, que queda fuera del curso.
- **Autoevaluación del documento:** las 5 preguntas de «Verifica tu comprensión».
  - Respuestas: resuelve IPv4→MAC y mantiene la tabla IPv4–MAC; se guarda en RAM; las entradas son temporales; `show ip arp`; envenenamiento ARP.

## ⭐ Pregunta marcada por el profesor como "de examen"

> ¿Cuál es la diferencia entre `enable secret` y `service password-encryption`?

- `enable secret` protege el modo privilegiado con un hash fuerte que no se puede revertir, y tiene prioridad sobre `enable password`.
- `service password-encryption` cifra con tipo 7 (débil y reversible) las contraseñas que estaban en texto plano en la configuración: consola, vty y `enable password`.

## Pendientes antes del examen

- [ ] Resolver la [[Practica 4 - Rutas estaticas|Práctica 4]] en Packet Tracer (rutas estáticas y sumarización).
- [ ] Resolver la [[Practica 5 - Rutas estaticas flotantes|Práctica 5]]; en el paso 8, observar con `ping -t` cómo entra la ruta flotante.
- [ ] Práctica 1: el `.md` y la hoja de respuestas entregada no coinciden en el número de interfaces. Vale la de la hoja entregada (Cisco 1941: 4 FastEthernet, 2 GigabitEthernet, 2 Serial).
- [ ] Repetir los cálculos de las Tareas 1–3 y el Ejercicio 2 (resueltos en `Tareas/`).
- [ ] **Preguntar al profesor:** ¿entran las rutas estáticas, la AD, las flotantes y CDP (no están en el temario oficial, pero él dijo «hasta la Práctica 5»)? ¿Entran ARP y MAC/IP?
- [ ] **Tarea «Tipos de enrutadores»** (diapositiva 70, sin material): investigar y redactar media página.

## Roadmap de estudio

Ocho sesiones de 1–2 h, en orden: cada una usa lo de la anterior (sin subnetting no hay sumarización; sin rutas estáticas no hay flotantes). El plan sigue tres principios con respaldo experimental: **ponerse a prueba** en vez de releer, **volver a cada tema** a los 1–4 días de verlo y **mezclar tipos de ejercicio** (Dunlosky et al. 2013; Cepeda et al. 2008; Rohrer).

**Cómo va cada sesión:**
1. **Calentamiento (10–15 min, sin apuntes):** contestar las preguntas de «Recuperar» sobre sesiones anteriores. Lo que falles, anótalo en el [[#Registro de fallos]].
2. **Tema nuevo:** primero intenta explicarlo o resolverlo sin mirar; después comprueba con la nota. No empieces releyendo.
3. **Cierre:** la prueba «listo si». Si no la pasas, se repite en el siguiente colchón.

| Fecha         | Tema nuevo                               | Recuperar (calentamiento) |
| ------------- | ---------------------------------------- | ------------------------- |
| Lun 28 sep    | Sesión 1: binario y clases               | —                         |
| Mar 29 sep    | Sesión 2: subnetting                     | Sesión 1                  |
| Mié 30 sep    | Sesión 3: VLSM y CIDR                    | Sesiones 1 y 2            |
| Jue 1 oct     | Sesión 4: Cisco IOS                      | Sesiones 2 y 3            |
| Vie 2 oct     | Colchón A: serie mezclada 1–4            | Registro de fallos        |
| Sáb 3 oct     | Sesión 5: estáticas (compacta) + SSH     | Sesiones 3 y 4            |
| Dom 4 oct     | Sesión 6: teoría de routers + AD compacta | Sesiones 4 y 5           |
| Lun 5 oct     | Sesión 7: FHRP a fondo                   | Sesiones 5 y 6            |
| Mar 6 oct     | Colchón B: pendientes + serie mezclada 1–7 | Registro de fallos      |
| Mié 7 oct     | Sesión 8: simulacro con el peso oficial  | —                         |
| **Jue 8 oct** | **Examen**                               |                           |

> Ajustado el 3 de octubre con el temario oficial: FHRP sube de peso; entran SSH, archivos imagen, funciones y tipos de routers, y ventajas de subredes; estáticas y AD bajan a versión compacta. El domingo deja de ser descanso y absorbe la teoría de routers y la AD, para aligerar el sábado, el lunes y el colchón B.

Si te atrasas, usa los colchones para terminar la sesión pendiente, pero haz al menos la mitad de la serie mezclada. Si aun así no alcanza, junta sesiones de las 1–4; no recortes las sesiones 5–7 ni el simulacro. Dormir 7–9 h **toda la semana** cuenta más que la noche anterior: nada de desvelos para recuperar sesiones.

### Sesión 1 (lun 28 sep) — Base: binario y clases (temas 1 y 2)
- [x] Explicar en voz alta, sin notas: salto a salto, estático vs dinámico, enrutado vs de enrutamiento, AS. Después comprobar con [[Conceptos fundamentales de enrutamiento]].
- [x] Practicar conversión decimal ↔ binario de octetos hasta hacerla de cabeza (128, 192, 224, 240, 248, 252, 254, 255).
- [x] Rehacer en papel la [[Tarea 1 - Separar red y host|Tarea 1]] y la [[Tarea 2 - Clases IP y direcciones de red|Tarea 2]] sin mirar la solución.
- **Listo si:** dada cualquier IP, dices clase, máscara por defecto y dirección de red en menos de 1 min.

### Sesión 2 (mar 29 sep) — Subnetting clásico (tema 3, primera mitad)
- [x] **Recuperar:** 3 IPs inventadas → clase, máscara por defecto y red; pasar 2 octetos a binario; ¿qué es un AS y qué rango tiene?
- [x] Escribir de memoria 2ⁿ subredes, 2ʰ − 2 hosts y cómo se hace el AND lógico; comprobar con [[Enmascaramiento y subnetting]].
- [x] Rehacer la Tarea 3 (clase B, 300 subredes → /25, 126 hosts) y el Ejercicio 2 (178.224.123.5/20 → subred 178.224.112.0, host 0.0.11.5).
- [x] Inventar 3 ejercicios más de cada tipo y resolverlos **alternando** Tarea 3 / Ejercicio 2, no todos los de un tipo seguidos.
- **Listo si:** resuelves un ejercicio tipo Ejercicio 2 sin calculadora y sin errores.

### Sesión 3 (mié 30 sep) — VLSM y CIDR (tema 3, segunda mitad)
- [x] **Recuperar:** 1 ejercicio tipo Ejercicio 2, 1 tipo Tarea 3 y 1 IP → clase y red.
- [x] Explicar sin mirar la diferencia subnetting / VLSM / CIDR; comprobar con [[CIDR y VLSM]].
- [x] Rehacer la [[Practica 3 - VLSM|Práctica 3]] desde cero: 192.168.40.0/24 con 100/40/22/10/5 hosts → /25, /26, /27, /28, /29, más los /30 de los enlaces.
- [ ] Explicar en voz alta el caso de la máscara mal puesta (ping al gateway sí, a otras subredes no, por ARP).
- **Listo si:** armas la tabla VLSM completa (red, máscara, rango, broadcast) sin solapamientos.

### Sesión 4 (jue 1 oct) — Cisco IOS (tema 4 y pregunta ⭐)
- [x] **Recuperar:** un VLSM corto inventado (3 LANs y 1 enlace /30) y 1 ejercicio tipo Ejercicio 2.
- [x] Escribir de memoria los modos de IOS y la configuración básica; comprobar con [[Sistema operativo IOS de cisco]], [[Practica 1 - Configuracion inicial del router|Práctica 1]] y [[Practica 2 - Router fisico Cisco 2514|Práctica 2]].
- [x] En Packet Tracer, configurar un router desde cero sin apuntes: hostname, consola, vty, `enable secret`, `service password-encryption`, banner, guardar.
- [x] Recitar el arranque (POST → bootstrap → IOS → startup-config) y qué vive en RAM, NVRAM y flash.
- [x] Contestar por escrito la pregunta ⭐ de `enable secret` vs `service password-encryption`, y la del 2514 (0 FastEthernet, porque sus puertos son Ethernet AUI de 10 Mbps).
- **Listo si:** la configuración básica sale de memoria y `show running-config` muestra todo cifrado.

### Colchón A (vie 2 oct) — Serie mezclada de las sesiones 1–4
- [x] Primero, lo pendiente: terminar una sesión atrasada o repetir un «listo si» fallido.
- [x] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [x] Serie mezclada de 45 min, en orden aleatorio: 2 IP → clase y red, 2 tipo Ejercicio 2, 1 tipo Tarea 3, 1 VLSM, pregunta ⭐, arranque del router y 5 comandos IOS con su modo. Antes de resolver cada uno, di qué tipo de pro blema es.

### Sesión 5 (sáb 3 oct) — Rutas estáticas compactas + acceso remoto seguro (temas 4 y 5)
- **Recuperar:**
  - [x] 1 VLSM corto (172.31.50.0/24: 62/31/6 + enlace). Sin errores.
  - [x] Configuración básica de un router, escrita de memoria.
  - [x] Pregunta ⭐.
- [ ] [[Practica 4 - Rutas estaticas|Práctica 4]] en Packet Tracer, versión compacta (~1 h): rutas por siguiente salto, una por interfaz de salida (comparar `show ip route`), sumarización a /22, ruta por defecto y `clock rate` solo en el DCE.
- [ ] **SSH (oficial):** en el mismo router, configurar `ip domain-name`, `crypto key generate rsa`, `username … secret`, `ip ssh version 2`, y en `line vty 0 4` poner `login local` y `transport input ssh`. Probar desde una PC con `ssh -l <usuario> <ip>` y comprobar que Telnet queda rechazado.
- **Listo si:** hay ping extremo a extremo, sabes leer cada línea `S`, `C` y `L`, y entras por SSH pero no por Telnet.

### Sesión 6 (dom 4 oct) — Teoría de routers + AD compacta (temas 3, 4 y 6)
- [ ] **Recuperar:** los comandos de SSH de memoria; 1 ruta estática, 1 por defecto y 1 sumarización de 4 redes /24; qué hay en RAM, NVRAM y flash.
- [ ] Ventajas de las subredes: explicarlas sin mirar (subnetting, VLSM y CIDR); después comprobar con el tema 3.
- [ ] Funciones del router (mejor ruta + reenvío; MAC por salto, IP de extremo a extremo) y del IOS (seguridad, enrutamiento, QoS, direccionamiento, administración de recursos, interfaz): primero sin mirar, después comprobar con el tema 4.
- [ ] Archivos imagen: descifrar `c1900-universalk9-mz.SPA.152-4.M3.bin` parte por parte; diferencia entre `universalk9` y `universalk9_npe`; trenes EM y T; requisitos de memoria del ISR G2.
- [ ] **Tarea «Tipos de enrutadores»:** investigar y redactar media página (cierra el pendiente de arriba).
- [ ] AD compacta (30 min): la tabla de memoria (0, 1, 90, 110, 120, 255) y una flotante. La [[Practica 5 - Rutas estaticas flotantes|Práctica 5]] completa, solo si el profesor confirma que entra.
- **Listo si:** descifras un nombre de imagen IOS sin mirar y escribes la tabla de AD completa dos veces seguidas.

### Sesión 7 (lun 5 oct) — FHRP a fondo (tema 7)
- [ ] **Recuperar:** la tabla de AD y 1 ruta flotante (principal OSPF); 1 nombre de imagen IOS; las funciones del IOS; las ventajas de las subredes.
- [ ] FHRP sin mirar: el problema que resuelve, el router virtual (IP y MAC), los pasos de la conmutación por error y las **7 opciones** en una línea cada una. Después, comprobar con el tema 7.
- [ ] HSRP: prioridad (100, 0–255, desempate por IP más alta), preempt, Hello 3 s / Hold 10 s (mínimos 1 s / 4 s) y estados. Resolver el caso R1=150 con preempt / R2=100: ¿quién es el activo y qué pasa si R1 cae y vuelve? ¿Y sin preempt?
- [ ] HSRP en Packet Tracer: 2 routers en la misma LAN, `standby 1 ip`, `priority`, `preempt`, `show standby brief`, y apagar el activo con `ping -t` corriendo.
- **Listo si:** listas las 7 opciones de FHRP y explicas preempt con el caso R1/R2 sin mirar.

### Colchón B (mar 6 oct) — Pendientes + serie mezclada 1–7
- [ ] Primero, lo pendiente: terminar una sesión atrasada o repetir un «listo si» fallido.
- [ ] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [ ] ARP (20 min, peso bajo): las 5 preguntas de «Verifica tu comprensión» del tema 8.
- [ ] Serie mezclada de 45 min, en orden aleatorio:
  - 1 VLSM y 1 ejercicio tipo Ejercicio 2.
  - Ventajas de las subredes.
  - 1 nombre de imagen IOS, la configuración de SSH y los tipos de routers.
  - La pregunta ⭐.
  - 2 de FHRP (opciones; prioridad y preempt).
  - 1 ruta estática o flotante.

### Sesión 8 (mié 7 oct) — Simulacro con el peso del temario oficial
- [ ] Sin apuntes, 60 min, **mezclados, no por tema**:
  - **Un tercio de subredes:** 1 VLSM, 1 ejercicio de subnetting y las ventajas.
  - **Un tercio de routers:** configuración básica + SSH, 1 nombre de imagen, funciones y tipos, y la pregunta ⭐.
  - **Un tercio de FHRP:** opciones, HSRP con caso de prioridad y preempt, y estados.
  - Además, 1 ruta estática + flotante.
- [ ] Corregir con este temario y volver solo a lo que fallaste.
- [ ] Repaso final de 15 min: volver a contestar sin mirar solo lo que fallaste hoy y lo que quede en el registro. Y a dormir temprano.

### Registro de fallos

Anota aquí cada pregunta o ejercicio que falles en un calentamiento, un «listo si» o el simulacro. Los colchones empiezan rehaciéndolos; borra una línea cuando te salga bien en dos días distintos.

- 

> Índice de la materia: [[Enrutamiento basico (materia)]]
