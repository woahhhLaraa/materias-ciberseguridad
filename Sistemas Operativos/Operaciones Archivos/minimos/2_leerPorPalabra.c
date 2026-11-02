#include <stdio.h>

int main() {
    FILE *archivo = fopen("../archivoPrueba.txt", "r");
    if (archivo == NULL) return 1;

    char palabra[30];
    while (fscanf(archivo, "%29s", palabra) == 1) {
        printf("%s\n", palabra);
    }

    fclose(archivo);
    return 0;
}
