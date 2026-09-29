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

## 5. Rutas estáticas ([[Practica 4 - Rutas estaticas|Práctica 4]])

- Sintaxis: `ip route <red> <máscara> {<ip-siguiente-salto> | <interfaz-salida>}`
- Siguiente salto vs interfaz de salida. En la tabla: `S` estática, `C` conectada, `L` local.
- **Sumarización:** 172.16.1.0, .2.0 y .3.0 /24 → `ip route 172.16.0.0 255.255.252.0 192.168.1.2` (/22).
- **Ruta por defecto:** `ip route 0.0.0.0 0.0.0.0 <ip|interfaz>`
- `clock rate 64000` solo en el extremo DCE del serial.
- `show cdp neighbors` / `show cdp neighbors detail`.

## 6. Distancia administrativa y rutas flotantes ([[Practica 5 - Rutas estaticas flotantes|Práctica 5]])

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

## 7. FHRP (probable, con menos peso)

Visto el 17 de septiembre junto con la distancia administrativa (ver [[Enrutamiento basico/Notas en curso|Notas en curso]]); ninguna práctica hasta la 5 lo usa.

- Problema: si falla el único gateway, los hosts quedan aislados. Solución: IP y MAC virtuales compartidas.
- **HSRP** (Cisco): un activo y uno de reserva; prioridad por defecto 100 (si empatan, gana la IP más alta); `standby <grupo> preempt`; Hello cada 3 s, timeout 10 s. Estados: Initial → Learn → Listen → Speak → Standby → Active.
- **VRRP:** estándar abierto; VRRPv3 soporta IPv4 e IPv6.
- **GLBP** (Cisco): redundancia más balanceo de carga.

## ⭐ Pregunta marcada por el profesor como "de examen"

> ¿Cuál es la diferencia entre `enable secret` y `service password-encryption`?

- `enable secret` protege el modo privilegiado con un hash fuerte que no se puede revertir, y tiene prioridad sobre `enable password`.
- `service password-encryption` cifra con tipo 7 (débil y reversible) las contraseñas que estaban en texto plano en la configuración: consola, vty y `enable password`.

## Pendientes antes del examen

- [ ] Resolver la [[Practica 4 - Rutas estaticas|Práctica 4]] en Packet Tracer (rutas estáticas y sumarización).
- [ ] Resolver la [[Practica 5 - Rutas estaticas flotantes|Práctica 5]]; en el paso 8, observar con `ping -t` cómo entra la ruta flotante.
- [ ] Práctica 1: el `.md` y la hoja de respuestas entregada no coinciden en el número de interfaces. Vale la de la hoja entregada (Cisco 1941: 4 FastEthernet, 2 GigabitEthernet, 2 Serial).
- [ ] Repetir los cálculos de las Tareas 1–3 y el Ejercicio 2 (resueltos en `Tareas/`).

## Roadmap de estudio

Siete sesiones de 1–2 h, en orden: cada una usa lo de la anterior (sin subnetting no hay sumarización; sin rutas estáticas no hay flotantes). El plan sigue tres principios con respaldo experimental: **ponerse a prueba** en vez de releer, **volver a cada tema** a los 1–4 días de verlo y **mezclar tipos de ejercicio** (Dunlosky et al. 2013; Cepeda et al. 2008; Rohrer).

**Cómo va cada sesión:**
1. **Calentamiento (10–15 min, sin apuntes):** contestar las preguntas de «Recuperar» sobre sesiones anteriores. Lo que falles, anótalo en el [[#Registro de fallos]].
2. **Tema nuevo:** primero intenta explicarlo o resolverlo sin mirar; después comprueba con la nota. No empieces releyendo.
3. **Cierre:** la prueba «listo si». Si no la pasas, se repite en el siguiente colchón.

| Fecha | Tema nuevo | Recuperar (calentamiento) |
|---|---|---|
| Lun 28 sep | Sesión 1: binario y clases | — |
| Mar 29 sep | Sesión 2: subnetting | Sesión 1 |
| Mié 30 sep | Sesión 3: VLSM y CIDR | Sesiones 1 y 2 |
| Jue 1 oct | Sesión 4: Cisco IOS | Sesiones 2 y 3 |
| Vie 2 oct | Colchón A: serie mezclada 1–4 | Registro de fallos |
| Sáb 3 oct | Sesión 5: rutas estáticas (la más larga) | Sesiones 3 y 4 |
| Dom 4 oct | Descanso | — |
| Lun 5 oct | Sesión 6: AD, flotantes y FHRP | Sesiones 4 y 5 |
| Mar 6 oct | Colchón B: serie mezclada 1–6 | Registro de fallos |
| Mié 7 oct | Sesión 7: simulacro | — |
| **Jue 8 oct** | **Examen** | |

Si te atrasas, usa los colchones para terminar la sesión pendiente, pero haz al menos la mitad de la serie mezclada. Si aun así no alcanza, junta sesiones de las 1–4; no recortes la 5, la 6 ni el simulacro. Dormir 7–9 h **toda la semana** cuenta más que la noche anterior: nada de desvelos para recuperar sesiones.

### Sesión 1 (lun 28 sep) — Base: binario y clases (temas 1 y 2)
- [x] Explicar en voz alta, sin notas: salto a salto, estático vs dinámico, enrutado vs de enrutamiento, AS. Después comprobar con [[Conceptos fundamentales de enrutamiento]].
- [x] Practicar conversión decimal ↔ binario de octetos hasta hacerla de cabeza (128, 192, 224, 240, 248, 252, 254, 255).
- [x] Rehacer en papel la [[Tarea 1 - Separar red y host|Tarea 1]] y la [[Tarea 2 - Clases IP y direcciones de red|Tarea 2]] sin mirar la solución.
- **Listo si:** dada cualquier IP, dices clase, máscara por defecto y dirección de red en menos de 1 min.

### Sesión 2 (mar 29 sep) — Subnetting clásico (tema 3, primera mitad)
- [x] **Recuperar:** 3 IPs inventadas → clase, máscara por defecto y red; pasar 2 octetos a binario; ¿qué es un AS y qué rango tiene?
- [ ] Escribir de memoria 2ⁿ subredes, 2ʰ − 2 hosts y cómo se hace el AND lógico; comprobar con [[Enmascaramiento y subnetting]].
- [ ] Rehacer la Tarea 3 (clase B, 300 subredes → /25, 126 hosts) y el Ejercicio 2 (178.224.123.5/20 → subred 178.224.112.0, host 0.0.11.5).
- [ ] Inventar 3 ejercicios más de cada tipo y resolverlos **alternando** Tarea 3 / Ejercicio 2, no todos los de un tipo seguidos.
- **Listo si:** resuelves un ejercicio tipo Ejercicio 2 sin calculadora y sin errores.

### Sesión 3 (mié 30 sep) — VLSM y CIDR (tema 3, segunda mitad)
- [ ] **Recuperar:** 1 ejercicio tipo Ejercicio 2, 1 tipo Tarea 3 y 1 IP → clase y red.
- [ ] Explicar sin mirar la diferencia subnetting / VLSM / CIDR; comprobar con [[CIDR y VLSM]].
- [ ] Rehacer la [[Practica 3 - VLSM|Práctica 3]] desde cero: 192.168.40.0/24 con 100/40/22/10/5 hosts → /25, /26, /27, /28, /29, más los /30 de los enlaces.
- [ ] Explicar en voz alta el caso de la máscara mal puesta (ping al gateway sí, a otras subredes no, por ARP).
- **Listo si:** armas la tabla VLSM completa (red, máscara, rango, broadcast) sin solapamientos.

### Sesión 4 (jue 1 oct) — Cisco IOS (tema 4 y pregunta ⭐)
- [ ] **Recuperar:** un VLSM corto inventado (3 LANs y 1 enlace /30) y 1 ejercicio tipo Ejercicio 2.
- [ ] Escribir de memoria los modos de IOS y la configuración básica; comprobar con [[Sistema operativo IOS de cisco]], [[Practica 1 - Configuracion inicial del router|Práctica 1]] y [[Practica 2 - Router fisico Cisco 2514|Práctica 2]].
- [ ] En Packet Tracer, configurar un router desde cero sin apuntes: hostname, consola, vty, `enable secret`, `service password-encryption`, banner, guardar.
- [ ] Recitar el arranque (POST → bootstrap → IOS → startup-config) y qué vive en RAM, NVRAM y flash.
- [ ] Contestar por escrito la pregunta ⭐ de `enable secret` vs `service password-encryption`, y la del 2514 (0 FastEthernet, porque sus puertos son Ethernet AUI de 10 Mbps).
- **Listo si:** la configuración básica sale de memoria y `show running-config` muestra todo cifrado.

### Colchón A (vie 2 oct) — Serie mezclada de las sesiones 1–4
- [ ] Primero, lo pendiente: terminar una sesión atrasada o repetir un «listo si» fallido.
- [ ] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [ ] Serie mezclada de 45 min, en orden aleatorio: 2 IP → clase y red, 2 tipo Ejercicio 2, 1 tipo Tarea 3, 1 VLSM, pregunta ⭐, arranque del router y 5 comandos IOS con su modo. Antes de resolver cada uno, di qué tipo de problema es.

### Sesión 5 (sáb 3 oct) — Rutas estáticas (tema 5)
- [ ] **Recuperar:** configuración básica de un router escrita de memoria, pregunta ⭐ y 1 VLSM corto.
- [ ] Resolver la [[Practica 4 - Rutas estaticas|Práctica 4]] completa en Packet Tracer (cierra el pendiente de arriba).
- [ ] Configurar la misma ruta de las dos formas (siguiente salto e interfaz de salida) y comparar `show ip route`.
- [ ] Hacer la sumarización a /22 y la ruta por defecto; poner `clock rate` solo en el DCE.
- **Listo si:** hay ping extremo a extremo y sabes leer cada línea `S`, `C` y `L` de la tabla.

### Sesión 6 (lun 5 oct) — Distancia administrativa, flotantes y FHRP (temas 6 y 7)
- [ ] **Recuperar:** escribir de memoria una ruta estática, una por defecto y una sumarización de 4 redes /24; qué hacen RAM, NVRAM y flash; ¿cuántas FastEthernet tiene el 2514 y por qué?
- [ ] Escribir la tabla de AD (0, 1, 90, 110, 120, 255) de memoria hasta que salga completa dos veces seguidas.
- [ ] Resolver la [[Practica 5 - Rutas estaticas flotantes|Práctica 5]] (cierra el pendiente de arriba): tirar el enlace principal con `ping -t` corriendo y ver entrar la flotante.
- [ ] FHRP, lo justo: explicar sin mirar el problema que resuelve, HSRP (prioridad 100, preempt, Hello 3 s / 10 s, estados), VRRP y GLBP en una línea cada uno; después comprobar con el tema 7.
- **Listo si:** explicas por qué la flotante no aparece en la tabla hasta que cae la principal, y qué AD le pondrías si la principal es OSPF.

### Colchón B (mar 6 oct) — Serie mezclada de las sesiones 1–6
- [ ] Primero, lo pendiente: terminar una sesión atrasada o repetir un «listo si» fallido.
- [ ] Rehacer sin apuntes todo lo del [[#Registro de fallos]].
- [ ] Serie mezclada de 45 min, en orden aleatorio: 1 IP → clase y red, 1 tipo Ejercicio 2, 1 VLSM, 1 sumarización, tabla de AD, 1 ruta flotante (principal EIGRP u OSPF), 1 pregunta de HSRP y la pregunta ⭐.

### Sesión 7 (mié 7 oct) — Simulacro
- [ ] Sin apuntes, 60 min: 2 ejercicios de clases, 2 de subnetting, 1 VLSM, 1 configuración IOS, 1 ruta estática + flotante, y las dos preguntas ⭐, **mezclados, no por tema**.
- [ ] Corregir con este temario y volver solo a lo que fallaste.
- [ ] Repaso final de 15 min: volver a contestar sin mirar solo lo que fallaste hoy y lo que quede en el registro. Y a dormir temprano.

### Registro de fallos

Anota aquí cada pregunta o ejercicio que falles en un calentamiento, un «listo si» o el simulacro. Los colchones empiezan rehaciéndolos; borra una línea cuando te salga bien en dos días distintos.

- 

> Índice de la materia: [[Enrutamiento basico (materia)]]
