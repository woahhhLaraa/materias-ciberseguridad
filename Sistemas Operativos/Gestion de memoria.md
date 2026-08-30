## Memoria Virtual
Es un concepto, o ilusion que crea el sistema operativo para los programas, sirviendo para manejar el uso del espacio de la memoria principal, evitando que los programas "se pisen" al escribir en ella.
 
Ademas, si esa memoria real se llegase a quedar sin espacio (por un proceso muy complejo,  o multiples), tiene permitido "asignar" un espacio de la memoria secundaria para su beneficio.

## Paginacion
Si bien, memoria virtual es un concepto. La paginacion es la tecnica que utliza para lograr lo que conocemos como Memoria virtual.

El sistema operativo le da a cada programa, o proceso un "mapa de apodos" o "mapa virtual" propio de la memoria, para hacerle creer que tiene todo el acceso a la memoria para el solo y de forma secuencial. El sistema operativo solo tiene que ver en la paginacion durante la creacion expansion o resolucion de problemas del mapa virtual.

El programa en cuestion usa esos "apodos" para referirse a la memoria real, sin saber ni como se llama de verdad ni donde esta ubicada fisicamente.

El MMU lee esos "apodos" y "traduce" para meter esos datos en los espacios reales de la memoria principal, la escritura sucede directamente en el lugar fisico de la memoria, sin un lugar "intermedio" donde se almacena el dato

La razon de existir del MMU (un componente de hardware fisico que existe dentro de la propia cpu, pero no forma parte de su esquema logico), es para bajar la carga logica del CPU con miles de milones de entradas a la memoria, lo que le quitaria mucho tiempo y poder de procesamiento al CPU