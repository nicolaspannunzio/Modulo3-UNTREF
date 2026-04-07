# ==============================================================================
# Clase 6 - Ejercicio 5
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Control de acceso con función:
# Pedirle al usuario que ingrese su nombre y edad.
# Crear una función llamada verificar_acceso() que reciba ambos valores por parámetro.
# Si la edad es mayor o igual a 18, la función debe imprimir:
# "Bienvenido/a, [nombre]. Tenés acceso autorizado."
# Caso contrario, debe imprimir:
# "Lo siento, [nombre]. El acceso no está permitido."
# ==============================================================================

def verificar_acceso(nombre_usuario, edad_usuario):
    print("\n--- Resultado de Verificación ---")
    if edad_usuario >= 18:
        print(f"Bienvenido/a, {nombre_usuario}. Tenés acceso autorizado.")
    else:
        print(f"Lo siento, {nombre_usuario}. El acceso no está permitido.")

print("--- Control de Acceso ---")
nombre_ingresado = input("Ingresá tu nombre: ")
edad_ingresada = int(input("Ingresá tu edad: "))

# Llamamos a la función pasándole los datos capturados
verificar_acceso(nombre_ingresado, edad_ingresada)