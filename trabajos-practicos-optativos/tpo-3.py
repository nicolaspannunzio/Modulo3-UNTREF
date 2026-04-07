# ==============================================================================
# Trabajo Optativo N° 3
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Integrando el código:
# Armar un programa que permita registrar usuarios. Cada usuario debe tener un
# nombre, apellido, edad y ciudad.
# Al finalizar la carga de 3 usuarios, el programa debe:
# - Mostrar cuántos viven en “Buenos Aires”
# - Calcular el promedio de edad
# - Mostrar los nombres completos (nombre + apellido) de todos los usuarios
# Los usuarios deben almacenarse como diccionarios dentro de una lista.
# Se pueden hacer funciones para organizar el código.
# ==============================================================================

# --- Funciones de procesamiento ---

def contar_residentes_ba(lista_usuarios):
    contador = 0
    for usuario in lista_usuarios:
        # Usamos lower() y strip() para evitar errores si el usuario escribe
        # "Buenos Aires", "buenos aires", o deja un espacio sin querer.
        if usuario["ciudad"].strip().lower() == "buenos aires":
            contador += 1
    return contador

def calcular_promedio_edad(lista_usuarios):
    suma_edades = 0
    for usuario in lista_usuarios:
        suma_edades += usuario["edad"]
    
    promedio = suma_edades / len(lista_usuarios)
    return promedio

def mostrar_nombres(lista_usuarios):
    for usuario in lista_usuarios:
        print(f"- {usuario['nombre']} {usuario['apellido']}")

# --- Bloque principal del programa ---

usuarios = []
cantidad_a_registrar = 3

print("--- Registro de Usuarios ---")
for i in range(cantidad_a_registrar):
    print(f"\nIngresando datos del usuario {i + 1}:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    # Armamos el diccionario del usuario
    usuario_dict = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "ciudad": ciudad
    }
    
    # Lo agregamos a la lista general
    usuarios.append(usuario_dict)

# --- Ejecución y Muestra de Resultados ---

print("\n================ RESULTADOS ================")

# 1. Contar los que viven en Buenos Aires
total_ba = contar_residentes_ba(usuarios)
print(f"Cantidad de usuarios que viven en Buenos Aires: {total_ba}")

# 2. Calcular promedio de edad
promedio = calcular_promedio_edad(usuarios)
print(f"El promedio de edad de los usuarios es: {promedio:.1f} años")

# 3. Mostrar nombres completos
print("\nNombres completos registrados:")
mostrar_nombres(usuarios)