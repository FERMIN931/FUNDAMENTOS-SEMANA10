import copy

# Definición de la función según los requerimientos del tema
def duplicar_notas(lista):
    """
    Recibe una lista de diccionarios.
    Usa copy.deepcopy() para evitar modificar la lista original por referencia.
    """
    # Clonamos la lista completa en una nueva dirección de memoria
    nueva_lista = copy.deepcopy(lista)
    
    # Modificamos los valores únicamente en la nueva lista
    for alumno in nueva_lista:
        alumno["nota"] = alumno["nota"] * 1.5
        
    # Retornamos el nuevo objeto clónico
    return nueva_lista


# --- Bloque de ejecución y verificación exigido por el ejercicio ---
if __name__ == "__main__":
    print("=== DEMOSTRACIÓN DE MUTABILIDAD Y REFERENCIAS (SEMANA 10) ===")
    
    # 1. Crear la lista original de diccionarios {nombre, nota}
    lista_original = [
        {"nombre": "Juan", "nota": 12},
        {"nombre": "María", "nota": 16}
    ]
    
    # 2. Llamar a la función para obtener la NUEVA lista
    lista_resultado = duplicar_notas(lista_original)
    
    # 3. VERIFICACIÓN CON id() (Exigencia del problema)
    print("\n[VERIFICACIÓN DE DIRECCIONES DE MEMORIA]")
    print(f"Dirección (id) de Lista Original:  {id(lista_original)}")
    print(f"Dirección (id) de Nueva Lista:     {id(lista_resultado)}")
    
    # Verificación de los diccionarios internos
    print(f"Dirección (id) del alumno 1 Orig:  {id(lista_original[0])}")
    print(f"Dirección (id) del alumno 1 Nuevo: {id(lista_resultado[0])}")
    
    # 4. COMPROBACIÓN DE LA PISTA (Las notas originales no deben cambiar)
    print("\n[COMPROBACIÓN DE VALORES]")
    print(f"Nota en lista original: {lista_original[0]['nota']} (Sigue siendo 12 -> ¡Éxito!)")
    print(f"Nota en lista nueva:     {lista_resultado[0]['nota']} (Cambió a 18.0 -> ¡Éxito!)")