# ==============================================================================
# Clase 8 - Ejercicio 2
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Un método para todos:
# Deberán armar un método como acelerar, con toda la información que crean necesaria.
# Luego, traten de generar dos métodos extras que se puedan aplicar a vehículos.
# ==============================================================================

class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.color = color
        self.encendido = False

    # Método 1: Acelerar (con la lógica de QA para evitar errores de tipo de dato)
    def acelerar(self, aceleracion):
        if not self.encendido:
            print("No podés acelerar, el vehículo está apagado.")
            return

        try:
            self.velocidad_actual += aceleracion
            # Lógica para no superar la velocidad máxima
            if self.velocidad_actual > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            print(f"Acelerando... Ahora el vehículo va a {self.velocidad_actual} km/h.")
        except TypeError:
            print(f"Error: Ingresá un número válido. El vehículo sigue a {self.velocidad_actual} km/h.")

    # Método 2 Extra: Encender
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("Motor encendido. ¡Listo para arrancar!")
        else:
            print("El vehículo ya estaba encendido.")

    # Método 3 Extra: Frenar
    def frenar(self, presion_freno):
        try:
            self.velocidad_actual -= presion_freno
            if self.velocidad_actual < 0:
                self.velocidad_actual = 0
            print(f"Frenando... La velocidad bajó a {self.velocidad_actual} km/h.")
        except TypeError:
            print("Error al pisar el freno.")

# --- Probando los métodos ---
print("--- Test de Métodos ---")
mi_auto = Vehiculo("Peugeot", "208", 180, "Blanco")

mi_auto.acelerar(50) # Intento acelerar apagado
mi_auto.encender()   # Enciendo
mi_auto.acelerar(80) # Acelero bien
mi_auto.acelerar("Fondo") # Intento romper el código pasando un texto (Prueba QA)
mi_auto.frenar(30)   # Freno