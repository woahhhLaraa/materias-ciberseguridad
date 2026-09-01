---
materia: Sistemas Operativos
semestre: 3
tipo: concepto
tags: [sistemas-operativos, entrada-salida, hardware, drivers]
---
#review
# Dispositivos de entrada y salida

Aquellos capaces de recibir un input del usuario para ser usado por el sistema operativo — a través del subsistema de entrada y salida descrito en [[Capas de un sistema operativo]] — o, en su defecto, de dar un output para comunicarse con el usuario.

Entre ellos se encuentran: mouse, teclado, dispositivos de almacenamiento secundario, bocinas, pantalla, tarjeta gráfica y tarjeta de red.

## Componentes de cada dispositivo

Cada dispositivo se puede dividir en dos partes:

- **Componente físico** — lo que se puede ver y tocar: mouse, teclado, bocinas, pantalla, almacenamiento secundario. Es el componente mecánico.
- **Componente lógico** — una tarjeta o chip que funciona como el "cerebro" del dispositivo: tiene su propia lógica, su controlador y, en algunos casos, memoria y búferes.

## Clasificación

### Por forma de transferencia (legacy)

| Tipo | Descripción | Ejemplos |
|---|---|---|
| **De bloque** | Mueve datos en cantidades de tamaño fijo | Dispositivos de almacenamiento |
| **De carácter** | Mueve datos byte por byte | Teclado, mouse |

### Por función (clasificación actual)

Las clasificaciones anteriores no son incorrectas, pero han dejado de aplicar a todos los dispositivos de E/S de la actualidad, por lo que se ha adoptado esta otra clasificación:

| Tipo | Descripción | Ejemplos |
|---|---|---|
| **De entrada** | Reciben información, pero no la envían | Teclado, mando, mouse |
| **De salida** | Permiten comunicarse hacia el exterior, sin recibir nada | Pantallas, bocinas |
| **De entrada/salida** | Pueden hacer ambas cosas | Tarjetas gráficas, discos de almacenamiento |

## Comunicación con el sistema operativo: drivers

Para comunicarse con el sistema operativo de forma bidireccional, todos los dispositivos de entrada y salida usan **controladores (drivers)**, que se encuentran dentro de su componente lógico.

### Registros E/S

- **Registro de control** — mediante comandos, el CPU controla al dispositivo E/S: escribe y lee
- **Registro de datos** — donde se guarda toda la información que se quiere leer del dispositivo, y también donde se escribe información hacia él desde la computadora
- **Registro de estado** — indica el estado actual del dispositivo E/S: suspendido, ocupado, encendido, listo, error

### Puertos o direcciones E/S

- Funcionan como puente entre el dispositivo E/S y el sistema operativo
- Le dan a cada registro proveniente del E/S una dirección única, para que el sistema operativo sepa con quién está hablando en todo momento

## Relacionadas

- [[Capas de un sistema operativo]] — el subsistema de entrada y salida al que pertenecen estos dispositivos
- [[Tecnicas de entrada y salida]] — las tres formas en que la CPU mueve datos hacia y desde estos dispositivos, vistas en Organización de computadoras
- [[Arquitectura de entrada y salida]] — el módulo de E/S del lado del hardware, con el que se comunican estos registros y puertos
- [[Definicion y funciones del sistema operativo]] — gestionar dispositivos es una de las funciones esenciales del SO
