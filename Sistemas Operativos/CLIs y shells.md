---
materia: Sistemas Operativos
semestre: 3
tipo: concepto
tags:
  - sistemas-operativos
  - interfaces
  - cli
  - shell
  - posix
---

# CLIs y shells

Durante la época de los primeros sistemas de tiempo compartido, se necesitaba una forma de comunicarse con las computadoras de manera interactiva, en lugar de entregar trabajos por lotes y esperar horas por el resultado. La solución fue escribir comandos en un teclado y recibir la respuesta al momento, primero impresa en papel mediante teletipos (TTY) y después en terminales de video.

Una interfaz de línea de comandos la componen tres conceptos ligados, pero que no son lo mismo:

**Terminal (consola)**  
Originalmente era un dispositivo físico con teclado y pantalla (o papel) que solo envía y recibe texto, sin interpretar nada. En Linux, la "pantalla negra" que aparece en un sistema sin entorno gráfico son las consolas virtuales (tty1, tty2, etc.) que proporciona el kernel.

**Emulador de terminal**  
Es un programa que emula una terminal física dentro de un entorno gráfico. Se encarga de dibujar el texto y capturar el teclado, y se comunica con la shell mediante una pseudoterminal (pty). No ejecuta comandos por sí mismo.

**Shell (intérprete de comandos)**  
Es un software que toma la cadena de texto de un comando, la divide en partes lógicas y expande variables, comodines, redirecciones y pipes. Después revisa si el comando es un alias, una función o un comando interno (builtin), y si no lo es, busca el programa en los directorios listados en la variable de entorno PATH y lo ejecuta

El termino shell suele ser utlizado de forma general para casi cualquier cli o terminal, muchas veces no es del todo correcto, pero es el uso comun.

## Diferentes shells en linux

Podemos clasificarlos de diferentes maneras, pero la mas comun (y la que mas me parece obvia) es como maneja los estandares POSIX, o que tan cercano se encuentra de cumplir POSIX

POSIX, es el estandar o convencion al que se llego para que los shells manejasen las mismas terminologias y comandos, dandole una experiencia al usuario final parecida entre diferentes shells.

### BASH

BOURNE AGAIN SHELL

Nacido para reemplazar BOURNE y llevar a cabo el estandar POSIX. Es el shell mas utilizado en las distribuciones linux, la mayoria de las distros lo tienen con unas cuantas exceptciones.

Es el mas utilizado por diferentes razones

Historicamente, UNIX empezo a utilizar BASH desde los 80s, entonces todo el mundo en ese momento empezo a aprender BASH, se fue documentando, y como todo estaba hecho en BASH, el mundo moderno sigue utilizandolo, es retroactivo.

BASH no solamente es un shell que interpreta los comandos y los ejecuta, tiene aspectos de un lenguaje de programacion, el scripting es uno de sus puntos fuertes, para automatizar tareas y tener control de bajo nivel automatico sobre el sistema operativo o un sistema, o una base de datos. 
Como la mayoria de los scripts con el tiempo se han hecho en BASH y la mayoria de los sistemas linux lo tienen cargado, escribir un script y hacer que corra en un sistema distinto al que se escribio se torna sencillo.

Un sistema util, bien documentado y con scripts portables de un lugar a otro

Si no esta roto, no lo reemplaces

### ZSH

Z shell, escrito por zhong shao, es un shell de la familia POSIX aunque con ciertas diferencias que lo alejan un poco del estandar.

Busca ser sumamente personalizable, probablemente de los shells mas personalizables, con una gran documentacion, util para scripting, aunque debido a no ser completamente POSIX friendly, algunos scripts podrian no correr en BASH

Es el estandar en MACOS y en distribuciones de linux como KALI

### FISH

Friendly interactive shell, un shell que busca ser interactivo, y comodo desde el primer uso con poca o nula configuracion por parte del usuario.

Para mantener su comodidad se aleja del estandar POSIX, si bien se puede programar scripts en el, las documentaciones de arch linux recomiendan no utilizarlo para esto, utilizar bash para scripting y subsistemas del SO.

Muy comodo, poca configuracion, ideal para usuarios nuevos o que buscan poca friccion con su terminal

### KSH

Korn Shell, uno de los pioneros en cuanto al estandar POSIX, al principio fue de codigo privado, y en 2000 se lanzo el codigo a internet despues de que sus creadores dejaran la empresa AT&T

Bastante viejo, no se ha modernizado lo suficiente a pesar de que existen diferentes repos en github que lo intentan

Su uso queda relegado a sistemas o codigo heredado

### TCS

Se encuentra en la misma situacion de korn shell, con scripting muy parecido a C, lo que lo aleja del estandar POSIX

Su uso queda relegado a sistemas o codigo heredado

## Relacionadas

- [[Interfaces graficas]] — la otra mitad de la capa de interfaz de usuario: lo que la GUI vino a sustituir para el usuario no tecnico
- [[Capas de un sistema operativo]] — la shell es la capa mas externa, la que traduce lo que el usuario escribe hacia el kernel
- [[Definicion y funciones del sistema operativo]] — el shell aparece ahi como la interfaz de usuario del esquema shell / kernel / hardware
- [[Generaciones de sistemas operativos]] — los sistemas de tiempo compartido de la 3ª generacion son los que hicieron necesaria la CLI; ahi aparece la interfaz CLI como rasgo de la generacion
- [[Reporte de instalacion de un sistema linux maquina virtual]] — la instalacion se hizo entera por CLI, sin entorno grafico
- [[Sistemas Operativos (materia)]] — indice de la materia
