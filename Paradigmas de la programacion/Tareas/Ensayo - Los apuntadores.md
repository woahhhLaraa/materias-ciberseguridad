---
materia: Paradigmas de la programacion
semestre: 3
tipo: tarea
tags: [tarea, ensayo, lenguaje-c, apuntadores, memoria]
---

# Ensayo - Los apuntadores

Ensayo entregado el 17 de septiembre de 2026. Original: ![[Ensayo - Los apuntadores.docx]] · versión entregada ![[Ensayo - Los apuntadores.pdf]]

> El código de clase que acompaña este tema está en `Codigo/apuntadores_arreglos_cadenas.c` (apuntadores, arreglos, cadenas y arreglos de estructuras).

Cuando uno empieza a programar, la memoria de la computadora es algo invisible: declaras una variable y no te preguntas dónde quedó. Los apuntadores rompen eso. Te obligan a aceptar que cada dato está guardado en algún lugar concreto, que ese lugar tiene un número, y que ese número también se puede manejar como cualquier otro dato.

## ¿Qué es un apuntador?

Un apuntador es una variable que guarda la dirección de memoria de otra variable. Eso es todo. No guarda el dato: guarda dónde está el dato.

La memoria se puede imaginar como una fila enorme de casillas numeradas. Cuando declaras una variable, el programa aparta unas casillas para ella. El apuntador solo guarda el número de la primera casilla.

Son dos operadores nada más. El operador & pregunta «¿dónde está esto?» y el operador \* pregunta «¿qué hay en esta dirección?». También existe NULL, que significa que el apuntador no apunta a nada válido.

## ¿Para qué sirve?

- **Modificar variables desde una función.** En C las funciones reciben copias, así que si quieres cambiar el original tienes que mandar la dirección.

- **No copiar datos grandes.** Pasar una dirección cuesta 8 bytes, aunque la estructura pese un megabyte.

- **Pedir memoria en tiempo de ejecución.** Cuando no sabes de antemano cuántos datos vas a necesitar, pides memoria al sistema y solo puedes llegar a ella por el apuntador.

- **Armar estructuras enlazadas.** Listas, árboles y grafos funcionan porque cada nodo guarda la dirección del siguiente.

- **Hablar con el hardware.** Muchos dispositivos se controlan escribiendo en direcciones fijas de memoria.

## ¿Dónde se usan?

Sobre todo en C y C++, donde están a la vista y se usan todos los días. También en programación de sistemas: sistemas operativos, controladores y sistemas embebidos no tienen otra forma de trabajar.

En lenguajes como Java o Python no los manejas directamente, pero ahí siguen: las referencias a objetos son apuntadores administrados por el lenguaje. El clásico error de referencia nula lo delata.

En seguridad informática importan mucho, porque buena parte de las vulnerabilidades graves (desbordamiento de búfer, uso después de liberar) son apuntadores que terminaron señalando a donde no debían.

## Ventajas y desventajas

**Ventajas:** son rápidos, evitan copiar datos, permiten memoria dinámica y hacen posibles estructuras que de otro modo no existirían. Dan control total sobre lo que pasa en memoria.

**Desventajas:** ese mismo control es el problema. Si liberas memoria y sigues usando el apuntador, tienes un apuntador colgante. Si reservas y nunca liberas, tienes una fuga de memoria. Si te pasas del límite de un arreglo, el compilador no te dice nada y el programa falla más tarde, en otro lado, a veces sin patrón claro. Además cuestan trabajo de entender y hacen el código más difícil de leer.

Se puede vivir con eso si uno se disciplina: inicializar siempre, poner el apuntador en NULL después de liberar, revisar que la petición de memoria no haya fallado y liberar todo lo que se reservó.

## Conclusión

El apuntador no es más que una dirección guardada en una variable, pero de esa idea salen la memoria dinámica, las estructuras enlazadas y el acceso al hardware. El lenguaje te da el control y da por hecho que sabes lo que haces; si no, no te avisa. Por eso conviene entenderlos aunque uno termine programando en lenguajes que los esconden: siguen siendo la explicación de por qué dos variables pueden apuntar al mismo objeto y de por qué un programa truena donde no era.

## Relacionadas

- [[Gestion de memoria]] — la memoria dinámica que el apuntador pide al sistema es la que el SO administra
- [[Jerarquia de memoria]] — la "fila de casillas numeradas" es la memoria principal, con su dirección por celda
- [[Riesgo amenaza y vulnerabilidad]] — el desbordamiento de búfer y el uso después de liberar son vulnerabilidades que nacen de apuntadores mal manejados
- [[Paradigmas de la programacion]] — índice de la materia
