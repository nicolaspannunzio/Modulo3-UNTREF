# ==============================================================================
# Clase 6 - Ejercicio 3
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Censo de mascotas:
# Armar un pequeño programa que permita cargar información de 3 mascotas.
# Para cada una, pedirle al usuario que ingrese el nombre, especie y edad.
# Guardar cada mascota como un diccionario y agregala a una lista general.
# Luego, crear una función que recorra la lista y muestre los nombres de las
# mascotas que tengan más de 5 años.
# ==============================================================================

def mostrar_mascotas_mayores(lista_mascotas):
    print("\n--- Mascotas con más de 5 años ---")
    for mascota in lista_mascotas:
        if mascota["edad"] > 5:
            print(f"- {mascota['nombre']} ({mascota['especie']})")

censo_general = []

print("--- Censo de Mascotas ---")
for i in range(3):
    print(f"\nDatos de la mascota {i + 1}:")
    nombre = input("Nombre: ")
    especie = input("Especie (ej: perro, gato): ")
    edad = int(input("Edad: "))
    
    # Creamos el diccionario temporal
    datos_mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }
    
    # Lo agregamos a la lista general
    censo_general.append(datos_mascota)

# Llamamos a la función pasándole nuestra lista de diccionarios
mostrar_mascotas_mayores(censo_general)