#include <stdio.h>
#include <string.h>

//Prototipos de funciones
void limpiarBuffer(){
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}


void leerArchivoPorPalabra(char *nombreArchivo){
    FILE *archivo;
    char cadena[30];

    archivo = fopen(nombreArchivo,"r");

    if (archivo == NULL){
        printf("Archivo nulo\n");
        return;
    }

    while (fscanf(archivo,"%29s",cadena) == 1){
        printf("%s\n",cadena);
    }

    fclose(archivo);
}


void leerArchivoPorCaracter(char *nombreArchivo){
    FILE *archivo;
    int caracter;
    archivo = fopen(nombreArchivo,"r");

    if (archivo == NULL){
        printf("Archivo nulo\n");
        return;
    }

    while((caracter = fgetc(archivo)) != EOF){
        printf("%c",caracter);
    }

    fclose(archivo);
}


void pedirDatos(char *nombreArchivo){
    printf("Ingrese el nombre del archivo: ");
    if (fgets(nombreArchivo,20,stdin) == NULL){
        nombreArchivo[0] = '\0';
        return;
    }
    nombreArchivo[strcspn(nombreArchivo,"\n")] = '\0';
}


void leerArchivoPorLinea(char *nombreArchivo){
    FILE *archivo;
    char linea[255];

    archivo = fopen(nombreArchivo, "r");

    if (archivo == NULL){
        printf("Archivo nulo\n");
        return;
    }

    while(fgets(linea,sizeof(linea),archivo) != NULL){
        printf("%s",linea);
    }

    fclose(archivo);
}


void escribirArchivoPorCaracter(char *nombreArchivo){
    FILE *archivo;
    int caracter;

    archivo = fopen (nombreArchivo,"a");

    if (archivo == NULL){
        printf("Archivo nulo\n");
        return;
    }

    printf("Introducemelo! \n ");

    while((caracter = getchar())!= '\n' && caracter != EOF){
        fputc(caracter,archivo);
    }
fclose(archivo);

}


void escribirArchivoPorPalabra(char *nombreArchivo){
FILE *archivo;
char palabra[30]; //hasta 29 caracteres mas '/0' (fin de la cadena)

    archivo = fopen (nombreArchivo,"a");

    if (archivo == NULL){
        printf("Archivo nulo\n");
        return;
    }

    printf("Introducemelo! y escribe 'fin' para terminar!\n ");

    while (scanf("%29s",palabra) == 1){
        if(strcmp(palabra,"fin")==0){
            break;
        }


if (fprintf(archivo,"%s ",palabra) < 0 ){
    printf("Error!");
    break;
    return;
}


        fclose(archivo);


    }


}


void escribirArchivoPorLinea(char *nombreArchivo){
FILE *archivo;
char linea[255]; //hasta 254 caracteres mas '/0' (fin de la cadena)

    archivo = fopen (nombreArchivo,"a");

    if (archivo == NULL){
        printf("Archivo nulo\n");
        return;
    }

    printf("Introducemelo! y escribe 'fin' para terminar!\n ");

    if (fgets(linea,sizeof(linea),stdin) == NULL){
        printf("Error al leer la entrada\n");
        fclose(archivo);
        return;
    }

if( fprintf(archivo,"%s ", linea) < 0){
    printf("Error!, linea vacia!");
    return;
}

    fclose(archivo);

}


int main() {

    char nombreArchivo[20];
    int eleccion;

    printf("Escoja el tipo de lectura.\n 1 = Por Caracter \n 2 = Por palabra \n 3 = Por linea \n ");
    printf("Escoja el tipo de escritura.\n 4 = Por Caracter \n 5 = Por palabra \n 6 = Por linea \n ");
    eleccion = getchar();
    printf("Escogiste %c:\n", eleccion);

    switch (eleccion) {
        case '1':
            limpiarBuffer();
            pedirDatos(nombreArchivo);
            leerArchivoPorCaracter(nombreArchivo);
            break;

        case '2':
            limpiarBuffer();
            pedirDatos(nombreArchivo);
            leerArchivoPorPalabra(nombreArchivo);
            break;

        case '3':
            limpiarBuffer();
            pedirDatos(nombreArchivo);
            leerArchivoPorLinea(nombreArchivo);
            break;

        case '4':
            limpiarBuffer();
            pedirDatos(nombreArchivo);
            escribirArchivoPorCaracter(nombreArchivo);
            break;

        case '5':
            limpiarBuffer();
            pedirDatos(nombreArchivo);
            escribirArchivoPorPalabra(nombreArchivo);
            break;

        case '6':
            limpiarBuffer();
            pedirDatos(nombreArchivo);
            escribirArchivoPorLinea(nombreArchivo);
            break;
        default:
            printf("INVALIDO!\n");
            break;
    }

    return 0;
}
