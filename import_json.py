import json
import os

def gestionar_catalogo():
    # 1. Crear el diccionario que representa el catálogo de productos
    # Usamos los IDs como claves y diccionarios internos para los atributos
    catalogo = {
        "1": {"nombre": "Teclado Mecánico", "precio": 45.99, "stock": 25},
        "2": {"nombre": "Mouse Óptico", "precio": 19.50, "stock": 12},
        "3": {"nombre": "Monitor 24 pulgadas", "precio": 149.99, "stock": 8},
        "4": {"nombre": "Auriculares Gamer", "precio": 35.00, "stock": 40}
    }
    
    nombre_archivo = "catalogo.json"
    
    
    # PARTE A: GUARDAR EL DICCIONARIO EN UN ARCHIVO JSON
  
    print("--- Guardando datos en JSON ---")
    
    # Abrimos el archivo en modo escritura ('w')
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        # json.dump convierte el diccionario en texto JSON y lo escribe en el archivo
        json.dump(catalogo, f, indent=2, ensure_ascii=False)
        
    print(f"Éxito: Datos guardados correctamente en '{nombre_archivo}'.\n")
    
   
    # PARTE B: VALIDAR Y CARGAR EL ARCHIVO JSON
   
    print("--- Cargando y filtrando datos desde JSON ---")
    
    # Pista del ejercicio: Validar si el archivo existe antes de abrirlo
    if os.path.exists(nombre_archivo):
        
        # Abrimos el archivo en modo lectura ('r')
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            # json.load lee el archivo de texto y lo transforma de vuelta a un diccionario Python
            catalogo_cargado = json.load(f)
            
        print("Archivo cargado con éxito. Productos con bajo stock (< 20):")
        print("-" * 50)
        
       
        # PARTE C: FILTRAR Y MOSTRAR PRODUCTOS (STOCK < 20)
       
        for prod_id, info in catalogo_cargado.items():
            # Evaluamos la condición de stock solicitada
            if info["stock"] < 20:
                print(f"ID: {prod_id} | Producto: {info['nombre']} | Precio: ${info['precio']} | Stock: {info['stock']}")
                
        print("-" * 50)
        
    else:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")

# Ejecución del programa
if __name__ == "__main__":
    gestionar_catalogo()