---
materia: Sistemas Operativos
semestre: 3
tipo: concepto
tags: [sistemas-operativos, clasificacion]
---

# Tipos de sistemas operativos

Tres criterios de clasificación.

## 1. Según el tipo de sistema informático

### Mainframes

### SO de servidor
- Proporcionan servicios a otras computadoras a través de la red
- Multiusuario, multitarea, escalables, orientados a red
- Para cargas intensas
- Diseñados para **nunca apagarse**
- Muy robustos en seguridad

### SO de escritorio
Windows, distribuciones Linux, BSD, sistemas Apple.
- Para uso personal, usuarios finales
- Interfaces *user friendly*
- Cuentan con aplicaciones y tiendas de aplicaciones

### SO móviles
Smartphones y tabletas.
- Orientados a la movilidad y la conectividad inalámbrica
- Pantallas táctiles
- Aprovechan múltiples sensores: GPS, cámara, acelerómetro
- Su limitación característica es la **batería**

| SO | Kernel | Uso |
|---|---|---|
| Android | Linux | Smartphones, tabletas |
| iOS | Darwin (UNIX) | Dispositivos Apple |
| HarmonyOS | Microkernel HongMeng | Huawei |
| Tizen OS | Linux | Smart TV |
| Xiaomi HyperOS | — | Smart bands |
| Roku | Linux | Smart TV |
| Android Automotive OS | Linux | Automóviles |

### SO embebidos

Aquellos Sistemas operativos que se utilizan en sistemas de hardware especializados, donde la eficiencia y el bajo consumo son la norma. Un microondas, un refrigerador, sistema medico. No suelen correr en procesadores, mas bien en microcontroladores.

Suelen ser cargados en sistemas de poco almacenamiento, podria ser directamente en la placa. Suelen tener un solo uso y al ser cargados tienden a no cambiarse, quizas actualizarse, pero no cambiar de OS.

Tambien suelen ser llamados embarcados o empotrados

Los sistemas embebidos mas conocicos suelen correr en linux y son:
- Embedded linux
	- El nucleo del sistema linux (su kernel) en un sistema empotrado
	- Una instalacion tipica de linux embebido suele ocupar en promedio 2MB
	- Camaras, routers, smart tvs, sistemas multimedia
- Open WRT
	- Routers y dispositivos de red
- TinyOS
	- Hecho principalmente para sensores en redes (IoT)
## 2. Según servicios y capacidades
### Sistemas de tiempo real
Son aquellos sistemas donde se espera una respuesta predecible tanto en tiempo como en forma, decimos "en tiempo real" porque esperamos que contesten de forma inmediata o casi inmediata. Utilizados principalmente en sistemas mas grandes donde cumplir en una ventana de tiempo reducida es obligatorio. 


Podemos dividirlos en otros dos grupos:

#### Tiempo real duro
Cuando se espera una respuesta inmediata obligatoria en un rango minimo de tiempo, pues podria ocurrir un fallo grave o peligroso, es normal que se midan en vidas humanas o perdidas millonarias.
#### Tiempo real blando
Cuando se puede permitir un pequeno retraso en la respuesta.

Suelen ser parte de un sistema mas grande, no acostumbran a ser el sistema principal. Por ejemplo, en un automovil, las bolsas de aire o frenos de emergencia son llevados por un sistmea embebido de tiempo real duro, mientras que un sistema aparte (que bien podria tambien ser linux) esta llevando el sistema de infoentretenimiento.

### Sistemas por numero de usuario
#### Monousuario
Aquellos sistemas operativos que solo pueden manejar a un usuario a la vez sin importar el numero de procesadores o de tareas que pueda ejecutar al mismo tiempo

Ojo: Que un sistema sea monousuario de forma comercial (como lo experimenta el usuario final) no significa que su kernel no tenga las capacidades de ser multiusuario, por eso windows server puede ser multiusuario sin tener que cambiar su kernel

#### Multiusuario
Aquellos sistemas que pueden manejar las peticiones de varios usuarios al mismo tiempo, donde cada uno puede tener su entorno shell (comunmente en CLI), con sus propios procesos, permisos y  memoria. De manera concurrente

### Sistemas por numero de tareas
#### Monotareas
Solo pueden realizar una sola tarea, una sola tarea acapara todo el procesador.

#### Multitareas
Pueden realizar multiples tareas "al mismo tiempo" dependiendo del sistema operativo y de la forma en que maneja la concurrencia

### Sistemas por numero de procesadores
#### Monoprocesador
Aquellos sistemas que tienen un solo procesador y que si tuvieran mas no serian capaces de detectarlo

#### Multiprocesador
OS que tienen mas de un procesador (o un procesador con varios nucleos). Los puede manejar con la siguientes tecnicas
	Simetrica
		El OS escoge un procesador "maestro" el cual va a dirigir a los demas procesadores (o nucleos) "esclavos".
	Asimetrica
		El OS es el que dirige a todos los procesadores o nucleos a los que tiene acceso, sin maestros ni esclavos, el OS se encarga de como usarlos.
## 3. Según su estructura interna

- **Monolíticos** — todo en un solo bloque
- **Microkernel** — el núcleo mínimo, el resto en espacio de usuario
- **Híbridos**

## Relacionadas

- [[Definicion y funciones del sistema operativo]] — lo que todos comparten por debajo de la clasificación: administrar recursos
- [[Generaciones de sistemas operativos]] — de dónde viene cada tipo; el de servidor hereda del mainframe de segunda generación
