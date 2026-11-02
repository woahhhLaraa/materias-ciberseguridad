#include <stdio.h>

int main() {
    FILE *archivo = fopen("../archivoPrueba.txt", "a");
    if (archivo == NULL) return 1;

    int caracter;
    while ((caracter = getchar()) != '\n' && caracter != EOF) {
        fputc(caracter, archivo);
    }

    fclose(archivo);
    return 0;
}
