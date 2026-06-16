import csv
import os  # <--- Importamos el módulo para manejar rutas del sistema

# 1. Ubicamos el archivo de forma dinámica
# 'os.path.dirname(__file__)' obtiene la carpeta exacta donde está guardado este script
carpeta_actual = os.path.dirname(__file__)
archivo_csv = os.path.join(carpeta_actual, "estudiantes.csv")

# Creamos una lista para almacenar todas las notas y calcular el promedio general
todas_las_notas = []

print("--- ESTUDIANTES CON NOTA MAYOR O IGUAL A 11 ---")

# 2. Abrimos el archivo utilizando la ruta dinámica que construimos
with open(archivo_csv, mode="r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)
    
    for fila in lector_csv:
        # Convertimos la nota de texto a número decimal (float)
        nota = float(fila["nota"])
        nombre = fila["nombre"]
        carrera = fila["carrera"]
        
        todas_las_notas.append(nota)
        
        # 3. Filtramos: Solo mostramos si la nota es >= 11
        if nota >= 11:
            print(f"Nombre: {nombre} | Carrera: {carrera} | Nota: {nota}")

print("-" * 47)

# 4. Calculamos y mostramos el promedio general
if todas_las_notas:
    promedio_general = sum(todas_las_notas) / len(todas_las_notas)
    print(f"Promedio General de todos los estudiantes: {promedio_general:.2f}")
else:
    print("No se encontraron datos para calcular el promedio.")