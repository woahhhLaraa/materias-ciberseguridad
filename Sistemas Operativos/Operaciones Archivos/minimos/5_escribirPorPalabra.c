#include <stdio.h>
#include <string.h>

int main() {
    FILE *archivo = fopen("../archivoPrueba.txt", "a");
    if (archivo == NULL) return 1;

    char palabra[30];
    while (scanf("%29s", palabra) == 1 && strcmp(palabra, "fin") != 0) {
        fprintf(archivo, "%s ", palabra);
    }

    fclose(archivo);
    return 0;
}
