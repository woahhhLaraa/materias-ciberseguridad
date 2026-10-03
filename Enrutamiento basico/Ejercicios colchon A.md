---
materia: Enrutamiento basico
semestre: 3
tipo: ejercicios
tags: [examen, parcial, subnetting, vlsm, ios, repaso]
---

# Serie mezclada — Colchón A (sesiones 1–4)

45 min, **sin apuntes ni calculadora**, en el orden en que vienen. Antes de resolver cada uno, di qué tipo de problema es. En el VLSM, el número de hosts de cada LAN ya incluye la interfaz del router. Lo que falles va al [[Temario primer parcial#Registro de fallos|registro de fallos]].

1. **140.27.183.66/22** → clase, red con clase, subred y porción de host.
2. Para cada tarea, escribe el comando y el modo (con su prompt) en el que se teclea:
   a) Guardar la configuración para que sobreviva a un reinicio.
   b) Que la consola pida la contraseña que ya le pusiste con `password`.
   c) Cifrar las contraseñas que están en texto plano en la configuración.
   d) Ver la configuración activa.
   e) Darle a G0/0 la IP 192.168.1.1/24 y encenderla.
3. `01111110.00001010.11001000.00000001` → pásala a decimal y di clase, máscara por defecto y dirección de red.
4. VLSM de **192.168.60.0/24**: LANs de 29, 63, 9 y 50 hosts, más 2 enlaces punto a punto. Tabla completa: red, máscara, rango utilizable y broadcast. (Ojo con los números.)
5. ⭐ ¿Cuál es la diferencia entre `enable secret` y `service password-encryption`?
6. Red clase B que se divide en **120 subredes** → máscara (decimal y prefijo) y hosts utilizables por subred.
7. **92.205.47.130** con máscara **255.192.0.0** → clase, red con clase, subred y porción de host.
8. Describe en orden el arranque de un router Cisco. ¿Qué guarda la RAM, la NVRAM y la flash? ¿Qué pasa si no hay startup-config?
9. **192.0.2.77** → clase, máscara por defecto y dirección de red.

---
---
---

## Soluciones

**1.** Clase B (128–191) → red con clase 140.27.0.0. /22 = 255.255.252.0. Tercer octeto: 183 = `10110111` AND `11111100` = `10110100` = 180 → **subred 140.27.180.0**. Host: 183 − 180 = 3 → **0.0.3.66**.

**2.**

| | Comando | Modo |
|---|---|---|
| a) | `copy running-config startup-config` (`copy run start`) | EXEC privilegiado — `Router#` |
| b) | `login` (después de `line console 0`) | Config de línea — `Router(config-line)#` |
| c) | `service password-encryption` | Config global — `Router(config)#` |
| d) | `show running-config` | EXEC privilegiado — `Router#` |
| e) | `interface g0/0` → `ip address 192.168.1.1 255.255.255.0` → `no shutdown` | Config de interfaz — `Router(config-if)#` |

En b), sin `login` la consola no pide la contraseña aunque esté puesta. En e), sin `no shutdown` la interfaz queda apagada.

**3.** 126.10.200.1. Empieza por `0` → **clase A**, **/8 (255.0.0.0)**, red **126.0.0.0**. (126 es la última de la A; 127 es loopback.)

**4.** Ordena de mayor a menor: 63, 50, 29, 9. La trampa: 63 no cabe en /26 (2⁶ − 2 = 62), así que sube a /25. 29 sí cabe en /27 (30) y 9 en /28 (14).

| LAN | Hosts | Red | Máscara | Rango | Broadcast |
|---|---|---|---|---|---|
| 63 | 126 | 192.168.60.0/25 | 255.255.255.128 | .1 – .126 | .127 |
| 50 | 62 | 192.168.60.128/26 | 255.255.255.192 | .129 – .190 | .191 |
| 29 | 30 | 192.168.60.192/27 | 255.255.255.224 | .193 – .222 | .223 |
| 9 | 14 | 192.168.60.224/28 | 255.255.255.240 | .225 – .238 | .239 |
| Enlace 1 | 2 | 192.168.60.240/30 | 255.255.255.252 | .241 – .242 | .243 |
| Enlace 2 | 2 | 192.168.60.244/30 | 255.255.255.252 | .245 – .246 | .247 |

Libre desde 192.168.60.248.

**5.**
- `enable secret` protege el modo privilegiado con un hash fuerte que no se puede revertir, y tiene prioridad sobre `enable password`.
- `service password-encryption` cifra con tipo 7 (débil y reversible) las contraseñas que estaban en texto plano en la configuración: consola, vty y `enable password`.

**6.** 2⁷ = 128 ≥ 120 → 7 bits prestados → **/23 = 255.255.254.0**. Hosts: 2⁹ − 2 = **510**.

**7.** Clase A (1–126) → red con clase 92.0.0.0. 255.192.0.0 = /10. Segundo octeto: 205 = `11001101` AND `11000000` = `11000000` = 192 → **subred 92.192.0.0**. Host: 205 − 192 = 13 → **0.13.47.130**.

**8.** POST → bootstrap → carga el IOS de la flash a la RAM → carga la startup-config de la NVRAM a la RAM, donde pasa a ser la running-config.
- **RAM:** running-config (se pierde al apagar).
- **NVRAM:** startup-config.
- **Flash:** imagen del IOS (el `.bin` más grande).
- Sin startup-config, el router entra en **modo setup** (diálogo de configuración inicial).

**9.** 192 = `11000000`, empieza por `110` → **clase C**, **/24 (255.255.255.0)**, red **192.0.2.0**. (191 sería la última de la B.)

> Índice de la materia: [[Enrutamiento basico (materia)]]
