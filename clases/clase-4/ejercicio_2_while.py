# Clase 4 - Ejercicio 2
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio

# 1. Creamos una variable y le asignamos un valor.
# Como queremos que arranque mostrando el 1, la inicializamos en 1.
contador = 1

# 2. Creamos la estructura while.
# La condición es que el ciclo se repita mientras el contador sea menor o igual a 5.
while contador <= 5:
    
    # 4. Ponemos un print para ver los valores en pantalla.
    print(contador)
    
    # 3. Colocamos un agregador de valor en la variable.
    # Esto es fundamental para romper el ciclo y evitar un "loop infinito".
    # contador += 1 es la forma resumida y profesional de escribir: contador = contador + 1
    contador += 1