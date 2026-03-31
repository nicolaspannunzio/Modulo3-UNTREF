### UNTREF - DIPLOMATURA QA ###
### Nicolás Pannunzio ###

# Ejercicio 2
# Usando if o elif:Crear dos estructuras de código del tipo if/elif/else. 
# Ingresar los valores de las variables de forma manual.

""" Pasos básicos:
1. Crear una variable y asignarle un valor.
2. Crear la estructura de if/elif/else con lo visto.
3. Agregar print() en cada instancia para ir probando cómo ingresa en cada decisión.
4. Replicar la estructura de decisión."""

# 1. Crear una variable y asignarle un valor (manual)
nota = int(input("Ingresa la nota del examen (0-10): "))

# 2 y 3. Estructura if/elif/else con prints de prueba
if nota >= 9:
    print("Excelente: El examen está aprobado con honores.") 
elif nota >= 6:
    print("Aprobado: El examen cumple con los requisitos mínimos.")
else:
    print("Reprobado: Es necesario volver a rendir.") 