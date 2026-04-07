# ==============================================================================
# Clase 6 - Ejercicio 1
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Bienvenida personalizada:
# Pedir al usuario que ingrese su nombre, edad y ciudad.
# Guardar esta información en un diccionario.
# Luego, imprimir un mensaje personalizado como el siguiente:
# "Hola Juan, tenés 25 años y vivís en Rosario."
# ==============================================================================

# 1. Pedir al usuario que ingrese su nombre, edad y ciudad.
nombre_ingresado = input("Ingresá tu nombre: ")
edad_ingresada = input("Ingresá tu edad: ")
ciudad_ingresada = input("Ingresá tu ciudad: ")

# 2. Guardar esta información en un diccionario.
datos_usuario = {
    "nombre": nombre_ingresado,
    "edad": edad_ingresada,
    "ciudad": ciudad_ingresada
}

# 3. Imprimir un mensaje personalizado accediendo a los valores del diccionario.
print(f"Hola {datos_usuario['nombre']}, tenés {datos_usuario['edad']} años y vivís en {datos_usuario['ciudad']}.")