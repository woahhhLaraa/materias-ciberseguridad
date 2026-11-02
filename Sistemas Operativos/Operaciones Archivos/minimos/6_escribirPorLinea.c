#include <stdio.h>

int main() {
    FILE *archivo = fopen("../archivoPrueba.txt", "a");
    if (archivo == NULL) return 1;

    char linea[255];
    if (fgets(linea, sizeof(linea), stdin) != NULL) {
        fputs(linea, archivo);
    }

    fclose(archivo);
    return 0;
}
