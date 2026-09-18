#include <stdio.h> // Esta directiva le dice al compilador que incluya las declaraciones de funciones para la entrada y salida estándar (como printf() para imprimir en pantalla)


//-----------------------------Reglas de los identificadores en C---------------------------------------------------//
// 1. Deben comenzar con una letra (a-z, A-Z) o un guion bajo (_).
// 2. Pueden contener letras, números (0-9) y guiones bajos
// 3. No pueden ser palabras reservadas del lenguaje C (como int, return, if, etc.)
// 4. Son sensibles a mayúsculas y minúsculas (edad, Edad y EDAD son variables diferentes)

// Ejemplo de identificadores válidos e inválidos:
//  int main() {
//      int mi_edad;      // Correcto
//      int nombreEstudiante; // Correcto
//      int _dia_1;       // Correcto
//      int 1_dia;        // Incorrecto: no puede iniciar con un numero
//      int for;          // Incorrecto: `for` es una palabra reservada
//  }

//-------------------------------Tipos de datos en C-------------------------------------------------//
// 1. int: para números enteros
// 2. float: para números con decimales (precisión simple) 4 bytes de memoria = 32 bits de memoria = 6 a 7 dígitos de precisión
// 3. double: para números con decimales (precisión doble) 8 bytes de memoria = 64 bits de memoria = 15 a 16 dígitos de precisión
// 4. char: para caracteres individuales
// 5. void: representa la ausencia de valor (usado en funciones que no retornan nada).
// 6. _Bool: para valores booleanos (0 o 1)

// Ejemplo de uso de tipos de datos en C
// int main() {
//     int edad = 25;               // Variable de tipo entero
//     float pi = 3.141616;        // Variable de tipo flotante
//     double peso = 80.565412;  // Variable de tipo doble precisión
//     char inicial = 'A';         // Variable de tipo carácter
//     _Bool esEstudiante = 1;     // Variable de tipo booleano (1 para verdadero, 0 para falso)

//     printf("Edad: %d\n", edad);
//     printf("Pi: %.2f metros\n", pi);
//     printf("Peso: %.2lf kg\n", peso);
//     printf("Inicial: %c\n", inicial);
//     printf("Es estudiante: %d\n", esEstudiante);

//     return 0;
// }

//---------------------------------Modificadores de tipo en C-----------------------------------------------//
// Estos sirven para modificar el tamaño o el rango de los tipos de datos básicos. Se usan poco en la práctica,
// pero son importantes para optimizar el uso de memoria y para trabajar con valores específicos.
// Los modificadores más comunes son:
// 1. short: para enteros de menor tamaño
// 2. long: para enteros de mayor tamaño
// 3. unsigned: para enteros sin signo (solo valores positivos)
// 4. long long: para enteros de tamaño aún mayor
// 5. long double: para números de punto flotante de mayor precisión
// 6  signed: para enteros con signo (valores positivos y negativos, es el predeterminado), ASCII es un conjunto de caracteres que representa texto en computadoras y otros dispositivos. Cada carácter tiene un valor numérico asociado (código ASCII) que va de 0 a 127.

// Ejemplo de uso de modificadores de tipo
// int main() {
//     short int numeroCorto = 32767;          // Rango: -32768 a 32.767
//     long int numeroLargo = 2147483647;      // Rango: -2.147.483.648 a 2.147.483.647
//     unsigned int numeroSinSigno = 4294967295; // Rango: 0 a 4.294.967.295
//     long long int numeroMuyLargo = 9223372036854775807;  // Rango: -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807

//     printf("Numero corto: %d\n", numeroCorto);
//     printf("Numero largo: %ld\n", numeroLargo);
//     printf("Numero sin signo: %u\n", numeroSinSigno);
//     printf("Numero muy largo: %lld\n", numeroMuyLargo);

//     return 0;
// }

// ---------------------------------Rangos de los tipos de datos en C-----------------------------------------------//
// Estos rangos pueden variar según la implementación del compilador y la arquitectura del sistema.
// Sirven para saber los límites de los valores que se pueden almacenar en cada tipo de dato y para evitar errores de desbordamiento o pérdida de datos.
// Ejemplo de rangos de tipos de datos en C
// int main() {
//     // MODIFICADOR: unsigned char
//     // RANGO: 0 a 255
//     unsigned char edadPersona = 25;

//     printf("La edad guardada correctamente es: %d años.\n", edadPersona);

//     // ¿Qué pasa si intentamos romper el rango metiendo un número negativo?
//     // Como es 'unsigned' (sin signo), la máquina se confunde y da la vuelta al rango.
//     unsigned char edadInvalida = -1;

//     printf("¡Cuidado! Intentamos guardar -1 y la máquina leyó: %d\n", edadInvalida);

//     return 0;
// }

// Nota: Los rangos pueden variar según la implementación del compilador y la arquitectura del sistema.

//----------------------------------Constantes en C----------------------------------------------//
// int main() {
// const float PI = 3.14159;

// float radio = 5.766;
//     float area = PI * radio * radio;

//     printf("El area de un circulo con radio %.f es %.f\n", radio, area);

//     // Esta línea generaría un error de compilación.
//     //PI = 3.14;

//     return 0;
// }

// Tambien tenemos #define para definir constantes, fuera del main y no llevan punto y coma (;) al final.
// #define PI 3.14159

// Creamos una constante con #define
// #define IVA 0.16

// int main() {
//     // Creamos una constante con 'const'
//     const int PRECIO_TACO = 20;

//     // Creamos una variable normal
//     int cantidadTacos = 5;

//     // ACCESO: Para calcular el total, accedemos a ambas por su nombre
//     int subtotal = cantidadTacos * PRECIO_TACO;
//     float totalConIva = subtotal + (subtotal * IVA);

//     // ACCESO EN PRINTF: Se imprimen usando el mismo formato (%d, %f)
//     printf("Precio por taco: $%d\n", PRECIO_TACO); // Acceso a constante
//     printf("Cantidad comprada: %d\n", cantidadTacos); // Acceso a variable
//     printf("Total con IVA: $%.2f\n", totalConIva);

//     return 0;
// }

//-----------------------------------Variables en C---------------------------------------------//
// Una variable es un espacio en memoria que se utiliza para almacenar datos que pueden cambiar durante la
// ejecución del programa. Cada variable tiene un nombre (identificador) y un tipo de dato asociado.
// Existen diferentes tipos de variables según el tipo de dato que almacenan, como int, float, char, etc.
// Además, las variables pueden ser de diferentes tipos según su duración y alcance, como variables locales, globales y estáticas.
// Las variables deben ser declaradas antes de usarse, especificando su tipo y nombre.
// Finalmente, las variables pueden ser inicializadas al momento de su declaración o en cualquier otro punto del programa antes de su uso.

//  ----------------------------------Variables globales en C---------------------------------------------//
// Son variables declaradas fuera de cualquier función, accesibles desde cualquier parte del archivo.
// Mantienen su valor durante toda la ejecución del programa.
// Además, si se desea que una variable global sea accesible desde otros archivos, se puede usar la palabra clave 'extern' en su declaración en esos archivos.

// Ejemplo de variable global
// int variableGlobal = 100; // Todas las funciones la pueden usar
// void funcionEjemplo() {
//     printf("Dentro de la función, variableGlobal: %d\n", variableGlobal);
//     variableGlobal += 50; // Modificamos su valor
// }
// int main() {
//     printf("Antes de llamar a la función, variableGlobal: %d\n", variableGlobal);
//     funcionEjemplo();
//     printf("Después de llamar a la función, variableGlobal: %d\n", variableGlobal);
//     return 0;
// }

// ----------------------------------Variables locales en C---------------------------------------------//
// Son variables declaradas dentro de una función, accesibles solo dentro de esa función.
// Se crean cuando la función es llamada y se destruyen cuando la función termina su ejecución.
// No pueden ser accedidas desde otras funciones.

// Ejemplo de variable local
// void funcionEjemplo() {
//     int variableLocal = 50; // Solo esta función la puede usar
//     printf("Dentro de la función, variableLocal: %d\n", variableLocal);
//     variableLocal += 20; // Modificamos su valor
//     printf("Después de modificar, variableLocal: %d\n", variableLocal);
// }
// int main() {
//     funcionEjemplo();
//     // La siguiente línea generaría un error de compilación porque variableLocal no es accesible aquí.
//     // printf("En main, variableLocal: %d\n", variableLocal);
//     return 0;
// }

//---------------------------------Variables estáticas en C---------------------------------------------//
// Son variables locales a una función, pero mantienen su valor entre llamadas a la función.
// Se declaran con la palabra clave 'static'.
// Su alcance es local a la función donde se declaran, pero su duración es toda la ejecución del programa.
// En este sentido, pueden considerarse como una mezcla entre variables locales y globales.
// Pero nunca podran ser accedidas mediante extern desde otro archivo, ya que su alcance es local o dentro del script donde se declaran, aunque su duración sea global o de todo el programa.
// Ejemplo de variable estática

// void funcionEjemplo() {
//     static int contadorLlamadas = 0; // Mantiene su valor entre llamadas
//     contadorLlamadas++;
//     printf("La función ha sido llamada %d veces\n", contadorLlamadas);
// }

// void funcionEjemplo2() {
//     int contadorLlamadas = 0; // Mantiene su valor entre llamadas
//     contadorLlamadas++;
//     printf("La función 2 ha sido llamada %d veces\n", contadorLlamadas);
// }
// int main() {
//     funcionEjemplo(); // Primera llamada|
//     funcionEjemplo(); // Segunda llamada
//     funcionEjemplo(); // Tercera llamada
//     funcionEjemplo2(); // Llamada a la segunda función
//     funcionEjemplo2(); // Segunda llamada a la segunda función
//     funcionEjemplo2(); // Tercera llamada a la segunda función
//     return 0;
// }

//----------------------------------Alcance de las variables en C---------------------------------------------//
// El alcance de una variable determina dónde puede ser accedida dentro del código.
// 1. Variables globales: declaradas fuera de cualquier función, accesibles desde cualquier parte del archivo.
// 2. Variables locales: declaradas dentro de una función, accesibles solo dentro de esa función.
// 3. Variables estáticas: mantienen su valor entre llamadas a funciones, pero su alcance
//    es local a la función donde se declaran.
// Ejemplo de alcance de variables en C
// int variableGlobal = 10; // Variable global
// void funcionEjemplo() {
//     int variableLocal = 20; // Variable local
//     static int variableEstatica = 30; // Variable estática
//     variableEstatica++;
//     printf("Dentro de la función:\n");
//     printf("Variable global: %d\n", variableGlobal); // Acceso a variable global
//     printf("Variable local: %d\n", variableLocal);   // Acceso a variable local
//     printf("Variable estática: %d\n", variableEstatica); // Acceso a variable estática
// }
// int main() {
//     funcionEjemplo();
//     return 0;
// }

//----------------------------------Operadores en C----------------------------------------------//

// 1. Aritméticos: +, -, *, /, % (módulo o residuo de una división,  es útil para saber si un número es par o impar)

// int main() {

//     int suma = 5 + 3;                 // Suma
//     int resta = 5 - 3;                // Resta
//     int multiplicacion = 5 * 3;       // Multiplicación
//     int division = 5 / 3;             // División entera
//     int residuo = 5 % 3;              // Residuo de una división

//     printf("Suma: %d\n", suma);
//     printf("Resta: %d\n", resta);
//     printf("Multiplicación: %d\n", multiplicacion);
//     printf("División entera: %d\n", division);
//     printf("Residuo: %d\n", residuo);

//     return 0;
// }

// 2. De asignación: =, +=, -=, *=, /=
// int main() {
//     int numero = 10;

//     numero += 5; // Es lo mismo que numero = numero + 5; Ahora numero vale 15
//     printf("El valor de numero es: %d\n", numero);
//     numero -= 2; // Es lo mismo que numero = numero - 2; Ahora numero vale 13
//     printf("El valor de numero es: %d\n", numero);
//     numero *= 3; // Es lo mismo que numero = numero * 3; Ahora numero vale 39
//     printf("El valor de numero es: %d\n", numero);
//     numero /= 4; // Es lo mismo que numero = numero / 4; Ahora numero vale 9
//     printf("El valor de numero es: %d\n", numero);
//     numero %= 4; // Es lo mismo que numero = numero % 4; Ahora numero vale 1
//     printf("El valor de numero es: %d\n", numero);

//     return 0;
// }

// 3. De comparación: ==, !=, >, <, >=, <=
// int main() {
//     int a = 5;
//     int b = 10;
//     printf("a == b: %d\n", a == b);   // Igualdad
//     printf("a != b: %d\n", a != b);   // Desigualdad
//     printf("a > b: %d\n", a > b);     // Mayor
//     printf("a < b: %d\n", a < b);     // Menor
//     printf("a >= b: %d\n", a >= b);   // Mayor o igual
//     printf("a <= b: %d\n", a <= b);   // Menor o igual
//     return 0;
// }

// 4. Lógicos: &&, ||, !
// && (AND lógico) Devuelve verdadero solo si ambas condiciones son verdaderas.
// || (OR lógico) Devuelve verdadero si al menos una de las condiciones es verdadera.
// ! (NOT lógico) Invierte el resultado de una condición. Lo que era verdadero se vuelve falso, y viceversa.
// Tabla de verdad:
// A     B     A && B   A || B   !A     !B
// 0     0       0        0       1     1
// 0     1       0        1       1     0
// 1     0       0        1       0     1
// 1     1       1        1       0     0

// int main() {
//     int x = 5;
//     int y = 10;
//     int z = 5;
//     printf("(x < y) && (x == z): %d\n", (x < y) && (x == z)); // AND lógico
//     printf("(x < y) || (x != z): %d\n", (x < y) || (x != z)); // OR lógico
//     printf("!(x == z): %d\n", !(x == z)); // NOT lógico
//     return 0;
// }

// 5. De incremento/decremento: ++, --
// ++ Incrementa el valor de una variable en 1.
// -- Decrementa el valor de una variable en 1.

// int main() {
//     int contador = 5;
//     printf("Valor inicial: %d\n", contador);
//     contador++; // Incrementa en 1, es lo mismo que contador = contador + 1;
//     printf("Después de incrementar: %d\n", contador);
//     contador--; // Decrementa en 1, es lo mismo que contador = contador - 1;
//     printf("Después de decrementar: %d\n", contador);
//     return 0;
// }

//-------------------------------Condicionales en C-------------------------------------------------//


//     // if, else if, else
//     // if (condicion) {hacer esto si la condicion es verdadera}
//     // else if (otra condicion) {hacer esto si la otra condicion es verdadera}
//     // else {hacer esto si ninguna condicion es verdadera}
// int main() {
//     int edad = 20;

//     if (edad < 18) {
//         printf("Eres menor de edad.\n");
//     } else if (edad >= 18 && edad < 65) {
//         printf("Eres un adulto.\n");
//     } else {
//         printf("Eres un adulto mayor.\n");
//     }
// }

// int main() {
//     //switch
//     // switch (variable) {
//     // case valor1: hacer esto; break;
//     // case valor2: hacer esto; break;
//     // ...}
//     // Solo se puede usar con variables de tipo entero, char o enumeraciones. No se puede usar con float o double.
//     printf ("Bucle switch\n");
//     int mes = 4;
//     switch (mes)
//     {
//     case 1:
//         printf("Enero\n");
//         break;
//     case 2:
//         printf("Febrero\n");
//         break;
//     case 3:
//         printf("Marzo\n");
//         break;
//     case 4:
//         printf("Abril\n");
//         break;
//     case 5:
//         printf("Mayo\n");
//         break;
//     case 6:
//         printf("Junio\n");
//         break;
//     case 7:
//         printf("Julio\n");
//         break;
//     case 8:
//         printf("Agosto\n");
//         break;
//     case 9:
//         printf("Septiembre\n");
//         break;
//     case 10:
//         printf("Octubre\n");
//         break;
//     case 11:
//         printf("Noviembre\n");
//         break;
//     case 12:
//         printf("Diciembre\n");
//         break;
//     }

//     return 0;
// }

//---------------------------------Bucles en C-----------------------------------------------//


    // Bucle for se ejecuta un numero determinado de veces
    // Si la condicion es falsa desde el inicio, no se ejecuta ninguna vez
    // En C tenemos los siguientes bucles: for, while y do-while.
    // For se utiliza cuando sabemos cuántas veces queremos que se ejecute el bucle,
    // mientras que while y do-while se utilizan cuando no sabemos cuántas veces se ejecutará el bucle,
    // pero sí sabemos la condición que debe cumplirse para que se ejecute.
    // La diferencia entre while y do-while es que do-while se ejecuta al menos una vez,
    // mientras que while puede no ejecutarse nunca si la condición es falsa desde el inicio.


    // for (inicializacion; condicion; incremento/decremento)
// int main() {
//     printf("Bucle for:\n");

//     for (int i = 0; i < 5; i++) {
//         printf("i = %d\n", i);
//     }

//     return 0;
// }
    // Bucle while, se ejecuta mientras la condicion sea verdadera
    // Si la condicion es falsa desde el inicio, no se ejecuta ninguna vez
    // while (condicion) {mientras la condicion sea verdadera}
    // la diferencia con for es que no se inicializa, incrementa o decrementa, sino que se utiliza una variable externa para controlar la ejecución.
// int main() {
//     printf("\nBucle while:\n");
//     int j = 4;
//     while (j < 5) {
//         printf("j = %d\n", j);
//         j++;
//     }
//     return 0;
// }

    // Bucle do-while se ejecuta al menos una vez, y luego mientras la condicion sea verdadera
    // Si la condicion es falsa desde el inicio, se ejecuta una vez
    // do {hacer esto} while (condicion) {mientras la condicion sea verdadera}


// int main() {
//     printf("\nBucle do-while:\n");
//     int k = 6;
//     do {
//         printf("k = %d\n", k);
//         k++;
//     } while (k < 5);
//     return 0;
// }



