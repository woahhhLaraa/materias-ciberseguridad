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
## 3. Según su estructura interna

- **Monolíticos** — todo en un solo bloque
- **Microkernel** — el núcleo mínimo, el resto en espacio de usuario
- **Híbridos**

## Relacionadas

- [[Definicion y funciones del sistema operativo]] — lo que todos comparten por debajo de la clasificación: administrar recursos
- [[Generaciones de sistemas operativos]] — de dónde viene cada tipo; el de servidor hereda del mainframe de segunda generación
