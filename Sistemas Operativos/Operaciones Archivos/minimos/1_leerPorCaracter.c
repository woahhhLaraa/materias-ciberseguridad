#include <stdio.h>

int main() {
    FILE *archivo = fopen("../archivoPrueba.txt", "r");
    if (archivo == NULL) return 1;

    int caracter;
    while ((caracter = fgetc(archivo)) != EOF) {
        putchar(caracter);
    }

    fclose(archivo);
    return 0;
}
