# Clase 3 - Ejercicio 2
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio

# 1. Crear una variable y asignarle un valor manual.
estado_clima = "lluvioso"

# 2 y 3. Crear estructura if/elif/else y agregar print en cada instancia.
print("--- Primera estructura ---")
if estado_clima == "soleado":
    print("El día está hermoso para salir a pasear con los perros.")
elif estado_clima == "lluvioso":
    print("Mejor me quedo adentro practicando Python.")
else:
    print("El clima está inestable, mejor llevar paraguas.")

# 4. Replicar la estructura de decisión (hacemos otra prueba con otra variable).
print("\n--- Segunda estructura ---")
hora_dia = 14

if hora_dia < 12:
    print("¡Buenos días!")
elif hora_dia >= 12 and hora_dia < 19:
    print("¡Buenas tardes!")
else:
    print("¡Buenas noches!")