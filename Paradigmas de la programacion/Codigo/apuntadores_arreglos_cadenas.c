#include <stdio.h>

// -----------------------------Apuntadores en C-----------------------------------//
// Un apuntador (puntero) es una variable que almacena la dirección de memoria de otra variable (número o letra). 
// Se utilizan para manipular directamente la memoria y para pasar grandes estructuras de datos a funciones sin necesidad de copiarlas.
// El operador '&' se usa para obtener la dirección de una variable, y el operador '*' se usa para acceder al valor al que apunta un apuntador.
// Uso de apuntadores para modificar el valor de una variable dentro de una función:


// Imagina que tienes un videojuego y quieres crear una función que sume puntos al puntaje del jugador.
// Esta función recibe una COPIA del puntaje
// por lo que cualquier cambio que hagas dentro de la función no afectará el puntaje original fuera de la función.


// // Ejemplo de apuntadores en C:
// void agregarPuntos(int *puntaje) {
//     // el valor original que está en la dirección de memoria.
//     *puntaje += 50; 
//     printf("Dentro de la función, el nuevo puntaje es: %d\n", *puntaje);
// }

// // Función principal
// int main() {    
//     int puntajeJugador = 100;
//     printf("Puntaje de jugador inicial: %d\n", puntajeJugador);
    
//     // La llamada ahora coincide con el nombre de la función definida.
//     agregarPuntos(&puntajeJugador); 
    
//     printf("Puntaje después de la función: %d\n", puntajeJugador); 

//     return 0;     
// }

// -----------------------------Arreglos en C-----------------------------------//
// Un arreglo (array) es una colección de elementos del mismo tipo almacenados en ubicaciones de memoria contiguas (uno al lado del otro).
// Se accede a los elementos del arreglo mediante un índice, que comienza en 0.
// Los arreglos son útiles para almacenar listas de datos, como números o caracteres.
// Finalmente, los arreglos en C tienen un tamaño fijo que debe ser definido al momento de su declaración.

// Ejemplo de arreglos con enteros en C:
// int main() {
//     int numeros[] = {10, 20, 30, 40, 50};    // Declaración e inicialización de un arreglo de enteros
    
//     // Acceso a elementos individuales del arreglo
//     printf("Elemento del arreglo No.3: %d\n", numeros[2]); // Acceso al tercer elemento (índice 2)

//     // Acceso a los elementos del arreglo mediante índices
//     for (int i = 0; i < 5; i++) {
//         printf("Elemento en el índice %d: %d\n", i, numeros[i]);
//     }

//     // Modificación de un elemento del arreglo
//     numeros[1] = 25; // Cambiando el segundo elemento (índice 1)
//     printf("Después de la modificación, elemento No.2: %d\n", numeros[1]);


//     return 0;

// }

// Arreglos con cadenas de caracteres C
// int main() {
//     char *animales[] = {"perro", "gato", "cotorro", "leon"}; // Arreglo de 4 elementos
//     //int numAnimales = 4; // Es buena práctica definir el tamaño

//     //Usas sizeof para calcular el número de elementos AUTOMÁTICAMENTE.
//     //sizeof(animales) = tamaño total en bytes del arreglo
//     //sizeof(animales[0]) = tamaño en bytes de UN elemento (un char *)
//     //int numAnimales = sizeof(animales) / sizeof(animales[0]); // Calcula el número de elementos en el arreglo

//     // Acceso a elementos individuales del arreglo
//     printf("Elemento del arreglo No.4: %s\n", animales[3]); // Acceso al cuarto elemento (índice 3)
//     // Acceso a los elementos del arreglo mediante índices 
//     printf("\n--- Lista de Animales ---\n");
//     for (int i = 0; i < 4; i++) { // El bucle ahora va hasta 4
//         printf("Elemento en el índice %d: %s\n", i, animales[i]);
//     }
//     // Modificación de un elemento del arreglo 
//     printf("\n--- Modificación ---\n");
//     printf("Cambiando 'leon' por 'tigre' en el índice 3...\n");
//     animales[3] = "tigre"; // Cambiando el cuarto elemento (índice 3)
//     // Imprimimos el elemento que realmente modificamos
//     printf("Después de la modificación, elemento en el índice 3: %s\n", animales[3]);

//     // Ejemplo de Manipulación con Apuntadores ---
//     printf("\n\n--- Manipulación con un Apuntador Explícito ---\n");

//     // Declaramos un apuntador a char (cadena).
//     char **punteroAnimal;

//     // Usamos '&' para ASIGNAR la DIRECCIÓN de un elemento del arreglo al apuntador.
//     //    Vamos a apuntar al segundo elemento: "gato" (índice 1).
//     punteroAnimal = &animales[3];
//     printf("El puntero ahora apunta a la dirección de 'animales[3]'.\n");

//     // Usamos '*' para UTILIZAR el valor al que apunta el puntero.
//     //    *punteroAAnimal nos da el contenido de animales[1], que es la dirección de "gato".
//     printf("Usando el puntero, el animal es: %s\n", *punteroAnimal);
    
//     // También podemos modificar el arreglo a través del puntero.
//     // Cambiemos "gato" por "pez" usando solo el puntero.
//     printf("Cambiando el valor a través del puntero...\n");
//     *punteroAnimal = "pez";
    
//     // 5. Verificamos el cambio en el arreglo original.
//     printf("Después de modificar con el puntero, el elemento 'animales[3]' ahora es: %s\n", animales[3]);

//     // ... (Después de toda la manipulación con el puntero) ...

//     // --- Imprimiendo la Lista Final Completa ---
//     printf("\n\n--- Imprimiendo la Lista Final Completa ---\n");
//     printf("Este es el estado del arreglo 'animales' después de todos los cambios:\n");

//     // Recorremos el arreglo 'animales' para ver el resultado final
//     for (int i = 0; i < 4; i++) {
//         printf("Elemento en el índice %d: %s\n", i, animales[i]);
//     }
    

//     return 0;
// }

// -----------------------------Cadenas en C-----------------------------------//
// Una cadena es una secuencia de caracteres almacenados en un arreglo de tipo char.
// En C, las cadenas se representan como arreglos de caracteres terminados con un carácter nulo '\0'.
// Se pueden manipular cadenas utilizando funciones de la biblioteca estándar como strlen, strcpy, strcat, strcmp.
// Nunca debes manipular cadenas manualmente. Siempre usa la biblioteca <string.h>.
    //1. strlen(cadena): Devuelve la longitud de la cadena (sin contar \0).
    //2. strcpy(destino, origen): Copia una cadena. No puedes hacer destino = origen;.
    //3. strcat(destino, origen): Concatena (une) cadenas.
    //4. strcmp(cadena1, cadena2): Compara dos cadenas. Devuelve 0 si son iguales.

// Además, las cadenas pueden ser literales (definidas entre comillas dobles) o dinámicas (creadas en tiempo de ejecución).
// Finalmente, las cadenas en C no tienen un tamaño fijo, pero es importante asegurarse de que el arreglo tenga suficiente espacio para almacenar la cadena y el carácter nulo.


// Ejemplo de cadenas en C:
// #include <string.h>
// int main() {
//     char saludo[] = "Hola, Mundo!"; // Declaración e inicialización de una cadena, // En memoria:
//                                    // H  o  l  a  ,     M  u  n  d  o  !  \0
//                                    // 0  1  2  3  4  5  6  7  8  9 10 11 

//     // Acceso a caracteres individuales de la cadena
//     printf("Primer carácter: %c\n", saludo[0]); // Acceso al primer carácter

//     // Acceso a los caracteres de la cadena mediante índices
//     for (int i = 0; saludo[i] != '\0'; i++) {
//         printf("Carácter en el índice %d: %c\n", i, saludo[i]);
//     }

//     // Modificación de un carácter en la cadena
//     saludo[7] = 'C'; // Cambiando 'M' por 'C'
//     printf("Después de la modificación: %s\n", saludo);

//     // 1. strlen(): Obtener la longitud de la cadena
//     printf("1. strlen(): La longitud de '%s' es %zu.\n", saludo, strlen(saludo));

//     // 2. strcpy(): Copiar una cadena
//     char copia[30]; // Un nuevo arreglo para guardar la copia
//     strcpy(copia, "Adios!");
//     printf("2. strcpy(): La cadena copiada en 'copia' es: %s\n", copia);

//     // 3. strcat(): Concatenar (unir) cadenas
//     // Vamos a unir " Adios!" al final de "Hola, MCundo!"
//     strcat(saludo, copia); 
//     printf("3. strcat(): El saludo concatenado es: '%s'\n", saludo);

//     // 4. strcmp(): Comparar dos cadenas
//     char cadenaA[] = "Hola";
//     char cadenaB[] = "Hola";
//     char cadenaC[] = "Adios";

//     // 4. strcmp(): Comparar dos cadenas
//     printf("4. strcmp(): Comparando '%s' y '%s'.\n", cadenaA, cadenaB);
//     if (strcmp(cadenaA, cadenaB) == 0) {
//         printf("   Resultado: Las cadenas A y B son iguales.\n");
//     } else if (strcmp(cadenaA, cadenaC) == 0) {
//         // Este bloque nunca se ejecuta en este caso, ya que la primera condición es verdadera
//         printf("   Resultado: Las cadenas son A y C iguales.\n");
//     } else {
//         printf("   Resultado: Las cadenas son diferentes.\n");
//     }

                        
//     return 0;
// }

// -----------------------------Arreglos y estructuras en C-----------------------------------//

// Arreglos de estructuras (objetos) en C 
// strct es una palabra clave en C que se utiliza para definir estructuras, 
// que son tipos de datos personalizados que pueden contener múltiples variables de diferentes tipos bajo un mismo nombre.
// Imagina que quieres representar a varias personas, cada una con un nombre y una edad.
// Puedes definir una estructura llamada Persona y luego crear un arreglo de estas estructuras para almacenar información 
// sobre varias personas.

// Ejemplo de arreglos de estructuras en C:
// int main() {
//     struct Persona {               // Definición de una estructura para representar una persona
//         char nombre[50];          // Campo para el nombre, 50 caracteres como máximo de longitud
//         int edad;                 // Campo para la edad,
//     };


//     struct Persona personas[3] = { // Declaración e inicialización de un arreglo de estructuras
//         {"Alice", 30},            // Primer objeto Persona
//         {"Bob", 25},              // Segundo objeto Persona
//         {"Charlie", 35}           // Tercer objeto Persona
//     };

//    // Acceso a los elementos del arreglo de estructuras
//     for (int i = 0; i < 3; i++) {
//         printf("Persona %d: Nombre: %s, Edad: %d\n", i + 1, personas[i].nombre, personas[i].edad);
//     }
// return 0;
// }
    


// ------------------------- Array de estructuras con apuntadores en C ---------------------------//
// Anidar arreglos y estructuras en C
// Una estructura puede contener otros arreglos, lo que permite crear estructuras más complejas.
// Imagina que quieres guardar la ficha de un alumno. 
// El alumno tiene datos personales, pero también tiene una lista de materias en las que está inscrito. 
// Cada materia, a su vez, tiene su propio nombre y número de créditos.


// #include <stdlib.h> // Permite realizar operaciones de memoria dinámica, como conversion de tipos y gestión de memoria, entre otras cosas más.
// #include <string.h> // Permite manipular cadenas de caracteres y realizar operaciones como copiar, concatenar y comparar cadenas.

// // 1. Primero, definimos la estructura más simple: la Materia
// struct Materia {
//     char nombre[50];
//     int creditos;
// };

// // 2. Ahora, definimos la estructura principal que USA la anterior
// struct Alumno {
//     char *nombreCompleto; // Usaremos un apuntador para el nombre, el cual asignaremos memoria dinámica
//     // la memoria dinámica es útil cuando no sabemos de antemano cuántos datos vamos a necesitar almacenar
//     int id;
//     int numMaterias;      // Para saber cuántas materias cursa
//     struct Materia materias[5]; // Un ARREGLO de ESTRUCTURAS anidado (5 materias máximo)
// };

// // 3. Una función para imprimir la ficha (recibe un apuntador a la struct)
// // Aqui le pasamos la DIRECCIÓN de la estructura en donde están los datos del alumno, como nombre, id y materias

// void imprimirFichaAlumno(const struct Alumno *alumno) {
//     printf("\n--- Ficha del Alumno ---\n"); 
//     printf("ID: %d\n", alumno->id); // Usamos el operador de acceso '->' para acceder a los campos de la estructura a través del apuntador
//     printf("Nombre: %s\n", alumno->nombreCompleto); // El nombre es un apuntador, pero se imprime igual que una cadena normal
    
//     printf("\nMaterias Inscritas (%d):\n", alumno->numMaterias); // Imprimimos el número de materias
//     printf("---------------------------\n");
//     for (int i = 0; i < alumno->numMaterias; i++) { // Recorremos solo las materias que el alumno está cursando
//         printf(" -> Materia: %s (%d créditos)\n", // Imprimimos el nombre y créditos de cada materia
//                alumno->materias[i].nombre, 
//                alumno->materias[i].creditos);
//     }
//     printf("---------------------------\n");
// }

// int main() {
    // // Creamos una variable de nuestro tipo Alumno
    // struct Alumno alumno1;

    // // --- Llenando los datos del Alumno ---
    
    // // Asignamos memoria dinámica para el nombre
    // alumno1.nombreCompleto = malloc(50 * sizeof(char)); // Malloc es una función de asignacion de memoria dínamica y reservamos espacio para 50 caracteres
    
    // // Copiamos el nombre en la memoria asignada con strcpy (la función strcpy copia una cadena en otra)
    // strcpy(alumno1.nombreCompleto, "Ana Sofia Garcia");
    
    // alumno1.id = 20251234;
    // alumno1.numMaterias = 3; // El alumno cursa 3 materias

    // // --- Llenando los datos del arreglo de materias anidado ---
    // strcpy(alumno1.materias[0].nombre, "Cálculo Diferencial");
    // alumno1.materias[0].creditos = 10;
    
    // strcpy(alumno1.materias[1].nombre, "Programación Estructurada");
    // alumno1.materias[1].creditos = 8;

    // strcpy(alumno1.materias[2].nombre, "Álgebra Lineal");
    // alumno1.materias[2].creditos = 8;
    
    // // Llamamos a la función para mostrar los datos
    // // Le pasamos la DIRECCIÓN de la estructura con el operador &
    // imprimirFichaAlumno(&alumno1);

    // // Liberamos la memoria que pedimos con malloc
    // free(alumno1.nombreCompleto); // free libera la memoria asignada dinámicamente para evitar fugas de memoria
    // }
    // return 0;


    // --- Ahora, vamos a crear y manejar varios alumnos usando un arreglo de estructuras ---

    // // Crear un arreglo de estructuras para varios alumnos 
    // struct Alumno listaDeAlumnos[2];

    // // Llenar los datos del PRIMER alumno (índice 0)
    // listaDeAlumnos[0].nombreCompleto = malloc(50 * sizeof(char));
    // strcpy(listaDeAlumnos[0].nombreCompleto, "Ana Sofía García");
    // listaDeAlumnos[0].id = 20251234;
    // listaDeAlumnos[0].numMaterias = 2;
    // strcpy(listaDeAlumnos[0].materias[0].nombre, "Cálculo Diferencial");
    // listaDeAlumnos[0].materias[0].creditos = 10;
    // strcpy(listaDeAlumnos[0].materias[1].nombre, "Programación Estructurada");
    // listaDeAlumnos[0].materias[1].creditos = 8;

    // // Llenar los datos del SEGUNDO alumno (índice 1)
    // listaDeAlumnos[1].nombreCompleto = malloc(50 * sizeof(char));
    // strcpy(listaDeAlumnos[1].nombreCompleto, "Carlos David Pérez");
    // listaDeAlumnos[1].id = 20255678;
    // listaDeAlumnos[1].numMaterias = 1;
    // strcpy(listaDeAlumnos[1].materias[0].nombre, "Álgebra Lineal");
    // listaDeAlumnos[1].materias[0].creditos = 8;
    
    // // Imprimir la lista completa usando un bucle
    // printf("\n\n=== MOSTRANDO LISTA COMPLETA DE ALUMNOS ===\n");
    // for (int i = 0; i < 2; i++) {
    //     imprimirFichaAlumno(&listaDeAlumnos[i]);
    // }

    // // Liberar la memoria de CADA alumno 
    // for (int i = 0; i < 2; i++) {
    //     free(listaDeAlumnos[i].nombreCompleto); // Liberamos cada nombre que pedimos con malloc


    // }
    // return 0;
// }


