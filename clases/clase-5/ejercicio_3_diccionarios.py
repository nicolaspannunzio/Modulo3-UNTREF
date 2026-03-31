# Clase 5 - Ejercicio 3
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio

# 1. Armar un diccionario con al menos 8 elementos de información personal.
mi_info = {
    "nombre": "Nicolás",
    "apellido": "Pannunzio",
    "ubicacion": "Santa Fe",
    "profesion": "QA Specialist",
    "mascotas": ["Margarita", "Tino"],
    "hobby": "Play Chess",
    "estudiante_untref": True,
    "lenguaje_favorito": "Python"
}

# 2. Mostrar todos los elementos en la terminal.
print("--- Mi Diccionario Personal ---")
for clave, valor in mi_info.items():
    print(f"{clave.capitalize()}: {valor}")