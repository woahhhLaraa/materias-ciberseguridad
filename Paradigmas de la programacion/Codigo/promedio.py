
MATERIAS = ["Redes", "Criptografia", "Bases de datos", "Programacion"]
CALIFICACIONES = [10.0, 9.5, 9.8, 9.4]
MINIMA_APROBATORIA = 6.0



def estado(calificacion):
    if calificacion >= MINIMA_APROBATORIA:
        return "APROBADA"
    else:
        return "REPROBADA"

##AcuNmulador

suma = 0


for materia, calificacion in zip(MATERIAS, CALIFICACIONES):
    suma += calificacion
    print(f"{materia:<16} {calificacion:>4}  {estado(calificacion)}")

promedio = suma / len(CALIFICACIONES)
print("-" * 36)
print(f"Promedio general: {promedio}")





i = 0
while i < len(CALIFICACIONES) and CALIFICACIONES[i] >= MINIMA_APROBATORIA:
    i += 1

if i < len(CALIFICACIONES):
    print(f"Primera materia reprobada: {MATERIAS[i]} ({CALIFICACIONES[i]})")
else:
    print("No hay materias reprobadas.")


if promedio >= 9:
    print("Excelente semestre.")
elif promedio >= MINIMA_APROBATORIA:
    print("Semestre aprobado.")
else:
    print("Hay que recuperar materias.")
