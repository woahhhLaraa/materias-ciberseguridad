#include <stdio.h>

int main() {
    FILE *archivo = fopen("../archivoPrueba.txt", "r");
    if (archivo == NULL) return 1;

    char linea[255];
    while (fgets(linea, sizeof(linea), archivo) != NULL) {
        printf("%s", linea);
    }

    fclose(archivo);
    return 0;
}
