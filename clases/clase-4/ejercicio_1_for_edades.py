# Clase 4 - Ejercicio 1
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio

edades = []
cantidad_ciclos = 5

print("--- Ingreso de Edades ---")
# 1 y 2. Primera estructura for para ingresar números.
for i in range(cantidad_ciclos):
    edad = int(input(f"Ingresá la edad de la persona {i + 1}: "))
    edades.append(edad)

print("\n--- Edades mayores a 30 ---")
# 3 y 4. Segunda estructura for para mostrar los mayores a 30.
for edad in edades:
    if edad > 30:
        print(f"La edad {edad} es mayor a 30.")