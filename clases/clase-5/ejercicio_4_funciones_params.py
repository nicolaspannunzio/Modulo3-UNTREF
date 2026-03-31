# Clase 5 - Ejercicio 4
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio

# 1, 2 y 3. Crear la estructura de la función, variables y print.
def mostrar_informacion(nombre, apellido, edad):
    print("\n--- Información Recibida ---")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")

# 5. Solicitar el ingreso de datos por terminal.
print("Por favor, ingresá los siguientes datos:")
input_nombre = input("Tu nombre: ")
input_apellido = input("Tu apellido: ")
input_edad = int(input("Tu edad: "))

# 4. Agregar el llamado a la función pasándole los parámetros.
mostrar_informacion(input_nombre, input_apellido, input_edad)