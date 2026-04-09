# ==============================================================================
# Clase 8 - Ejercicio 1
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Una clase para todos:
# Con lo visto durante la clase, deberán armar una clase tipo vehículo, 
# con toda la información que crean necesaria.
# ==============================================================================

class Vehiculo:
    # Usamos __init__ para crear el constructor con los atributos principales
    def __init__(self, marca, modelo, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0  # Todo vehículo arranca detenido
        self.color = color
        self.encendido = False

print("--- Creando nuestro primer Vehículo ---")
mi_vehiculo = Vehiculo("Volkswagen", "Golf", 200, "Gris")
print(f"Vehículo registrado: {mi_vehiculo.marca} {mi_vehiculo.modelo} - Color: {mi_vehiculo.color}")