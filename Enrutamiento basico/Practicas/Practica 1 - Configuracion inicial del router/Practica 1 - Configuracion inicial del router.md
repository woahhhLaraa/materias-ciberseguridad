---
materia: Enrutamiento basico
semestre: 3
tipo: practica
tags: [packet-tracer, cisco, ios, router, configuracion-inicial, contrasenas]
---

# Practica 1 - Configuracion inicial del router

> Actividad de Packet Tracer *Configure Initial Router Settings* (CCNA, Cisco NetAcad).
> Archivos originales de la actividad, en esta misma carpeta:
> ![[Practica 1 - Configuracion inicial del router.pdf]] — instrucciones
> ![[Practica 1 - Configuracion inicial del router.pka]] — topologia de Packet Tracer

Objetivo: verificar la configuracion por defecto de R1, aplicarle la configuracion inicial (nombre, contrasenas, banner) y guardarla en NVRAM.

## Parte 1: verificar la configuracion por defecto

Conexion por consola: cable **Console** desde PCA (`RS 232`) a R1 (`Console`), y luego `PCA > Desktop > Terminal > OK > ENTER`.

```
Router> enable
Router# show running-config
Router# show startup-config
```

### Respuestas

| Pregunta | Respuesta |
|---|---|
| Nombre del router | `Router` (el hostname por defecto de IOS) |
| Interfaces FastEthernet | 0 |
| Interfaces GigabitEthernet | 3 (`GigabitEthernet0/0/0` a `0/0/2`) |
| Interfaces Serial | 0 |
| Rango de lineas vty | `0 4` (cinco sesiones Telnet/SSH simultaneas) |

> ⚠️ El conteo de interfaces depende del modelo que traiga la topologia. Los valores de la tabla son los del **ISR 4331**, el router de la version 7 de la actividad. Si tu practica usa el modelo viejo **1941**, las respuestas son 0 FastEthernet, **2** GigabitEthernet y **2** Serial. Confirmalo con la salida de `show running-config` antes de entregar: cuenta las lineas `interface ...` que aparecen.

**Por que responde `startup-config is not present`?**
Porque la NVRAM esta vacia. El archivo `startup-config` solo existe despues de guardar explicitamente la configuracion con `copy running-config startup-config`; como el router nunca se ha configurado ni guardado, no hay nada que mostrar. La configuracion actual vive unicamente en RAM.

## Parte 2: configuracion inicial de R1

Secuencia completa, desde el prompt `Router>`:

```
enable
configure terminal

hostname R1

enable password cisco
enable secret itsasecret

line console 0
 password letmein
 login
 exit

banner motd #Unauthorized access is strictly prohibited.#

service password-encryption
end
```

Notas sobre esta secuencia:

- `login` en la linea de consola es **obligatorio**: sin el, la contrasena queda configurada pero el router nunca la pide.
- El caracter `#` del banner es el delimitador. Puede ser cualquier caracter que no aparezca dentro del mensaje; abre y cierra el texto.
- `service password-encryption` va al final por claridad, pero cifra tanto las contrasenas ya existentes como las que se configuren despues.

### Verificacion

```
R1# show running-config
```

Salir de la sesion hasta ver `R1 con0 is now available`, presionar ENTER y comprobar que aparece el banner y la peticion de contrasena. Para volver a EXEC privilegiado: `letmein` (consola) y luego `enable` + `itsasecret`.

### Respuestas

**Que comando usas para verificar la configuracion?**
`show running-config` — muestra la configuracion activa en RAM, que es donde estan los cambios recien hechos.

**Por que todo router deberia tener un banner MOTD?**
Es un aviso legal. Advierte a quien se conecta que el acceso no autorizado esta prohibido, lo que sustenta acciones legales posteriores contra un intruso. Un banner de "bienvenida" puede interpretarse como invitacion a usar el equipo; por eso nunca se pone la palabra *welcome*. Tambien sirve para avisar de mantenimientos programados.

**Si no te pide contrasena antes del prompt de usuario, que comando de linea de consola olvidaste?**
`login`.

**Por que el `enable secret` da acceso y el `enable password` deja de ser valido?**
Cuando ambos estan configurados, IOS **ignora** `enable password` y valida solo contra `enable secret`. `enable secret` usa un hash fuerte (tipo 5, MD5, o tipo 8/9 en IOS recientes), mientras que `enable password` es texto plano o cifrado tipo 7, reversible. IOS da prioridad al mecanismo mas seguro.

**Las contrasenas que configures despues, se veran en texto plano o cifradas?**
Cifradas. `service password-encryption` no es una accion puntual: queda activo como servicio y cifra automaticamente cualquier contrasena en texto plano que se configure a partir de ese momento.

> ⚠️ Ese cifrado es de **tipo 7**, un algoritmo propietario debil y reversible en segundos con herramientas publicas. Solo protege contra alguien que mire la pantalla por encima del hombro, no contra un atacante que obtenga el archivo de configuracion. Por eso las contrasenas realmente sensibles van con `enable secret`, nunca con `enable password` + `service password-encryption`.

## Parte 3: guardar la configuracion

```
R1# copy running-config startup-config
```

**Que comando guarda la configuracion en NVRAM?**
`copy running-config startup-config` (copia de RAM a NVRAM).

**Version mas corta y no ambigua?**
`cop r s` — cada abreviatura es suficiente para que IOS identifique un unico comando/parametro posible. El alias `write memory` (`wr`) hace lo mismo pero es una forma heredada.

### Opcional: guardar en flash

```
R1# show flash
R1# copy startup-config flash
Destination filename [startup-config]?   <- ENTER para aceptar el nombre
R1# show flash
```

**Cuantos archivos hay en flash y cual es la imagen de IOS?**
La imagen de IOS es el archivo `.bin` con nombre del tipo `isr4300-universalk9.16.09.04.SPA.bin`: se reconoce porque es con diferencia el mas grande (decenas o cientos de MB frente a unos pocos KB de los demas) y porque su nombre codifica plataforma, tren de version y numero de release.

> ⚠️ El numero exacto de archivos depende del modelo simulado — leelo de tu salida de `show flash`.

Guardar el `startup-config` en flash es una copia de respaldo: el router sigue arrancando desde NVRAM, pero si la NVRAM se corrompe se puede restaurar copiando el archivo de vuelta.

## Relacionadas

- [[Conceptos fundamentales de enrutamiento]] — el router que aqui se configura es el dispositivo cuyo funcionamiento describe esa nota
- [[Enrutamiento basico (materia)]] — indice de la materia a la que pertenece esta practica
