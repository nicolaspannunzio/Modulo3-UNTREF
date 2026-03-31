# Clase 3 - Ejercicio 4
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio

# 1. Crear variable edad con input() y convertirla a entero.
edad = int(input("Ingresá tu edad: "))

# Creamos una variable vacía para guardar la clasificación (Paso 4)
clasificacion = ""

# 2 y 3. Usar if, elif y else para controlar los rangos usando comparadores simples.
if edad < 13:
    clasificacion = "Niño"

# Como nos pide controlar los rangos con comparadores, usamos 'and' para unir las condiciones
elif edad >= 13 and edad <= 17:
    clasificacion = "Adolescente"

elif edad >= 18 and edad <= 64:
    clasificacion = "Adulto"

# Si no cumple ninguna de las anteriores, por descarte es 65 o más
else:
    clasificacion = "Jubilado"

# 4. Escribir un print con la variable retornada.
print(f"La persona es: {clasificacion}")