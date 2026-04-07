# ==============================================================================
# Clase 6 - Ejercicio 2
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Análisis de notas:
# Pedir al usuario que ingrese 5 notas (entre 1 y 10) y almacenarlas en una lista.
# Luego, crear una función que reciba esa lista como parámetro, calcule el
# promedio de las notas y lo devuelva.
# Finalmente, mostrar el promedio por pantalla.
# ==============================================================================

def calcular_promedio(lista_notas):
    # Sumamos todas las notas y dividimos por la cantidad total
    suma = sum(lista_notas)
    promedio = suma / len(lista_notas)
    return promedio

notas_ingresadas = []

print("--- Ingreso de Calificaciones ---")
for i in range(5):
    # Asumimos que el usuario ingresa valores válidos entre 1 y 10
    nota = float(input(f"Ingresá la nota {i + 1}: "))
    notas_ingresadas.append(nota)

# Llamamos a la función y guardamos el resultado
promedio_final = calcular_promedio(notas_ingresadas)

print(f"\nEl promedio de las notas ingresadas es: {promedio_final:.2f}")