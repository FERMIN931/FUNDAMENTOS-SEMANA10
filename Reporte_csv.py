import csv
import os

# 1. Datos de prueba (La lista de diccionarios que pide el enunciado)
estudiantes = [
    {"nombre": "Ana Gomez", "nota": 15.5, "carrera": "Sistemas"},
    {"nombre": "Luis Perez", "nota": 9.0, "carrera": "Industrial"},
    {"nombre": "Maria Diaz", "nota": 12.0, "carrera": "Civil"}
]

# Definimos la ruta de salida usando el módulo 'os'
carpeta_actual = os.path.dirname(__file__)
ruta_reporte = os.path.join(carpeta_actual, "reporte.csv")

# 2. Definimos los encabezados (las columnas del archivo)
# Agregamos la columna 'estado' como pide el ejercicio
columnas = ["nombre", "nota", "carrera", "estado"]

# Variables para calcular el promedio al final
suma_notas = 0
total_estudiantes = len(estudiantes)

# 3. Abrimos el archivo en modo escritura ('w' de write)
with open(ruta_reporte, mode="w", encoding="utf-8", newline="") as archivo:
    # Creamos el escritor de tipo diccionario configurando las columnas
    escritor_csv = csv.DictWriter(archivo, fieldnames=columnas)
    
    # Escribimos la primera fila con los títulos de las columnas
    escritor_csv.writeheader()
    
    # 4. Recorremos los estudiantes, evaluamos su estado y escribimos
    for estudiante in estudiantes:
        nota = estudiante["nota"]
        suma_notas += nota  # Acumulamos para el promedio
        
        # Evaluamos el umbral (nota >= 11)
        if nota >= 11:
            estudiante["estado"] = "Aprobado"
        else:
            estudiante["estado"] = "Reprobado"
            
        # Escribimos el diccionario modificado directamente en el CSV
        escritor_csv.writerow(estudiante)
        
    # 5. Agregamos la fila final con el promedio
    promedio = suma_notas / total_estudiantes
    
    # Creamos un diccionario especial para la fila del promedio
    fila_promedio = {
        "nombre": "PROMEDIO GENERAL",
        "nota": round(promedio, 2),
        "carrera": "",
        "estado": ""
    }
    escritor_csv.writerow(fila_promedio)

print("¡Reporte generado con éxito en 'reporte.csv'!")