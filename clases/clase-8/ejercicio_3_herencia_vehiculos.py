# ==============================================================================
# Clase 8 - Ejercicio 3
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Una herencia para todos:
# Con lo visto durante la clase, deberán crear objetos Auto y Bicicleta que 
# reutilizan los métodos del padre.
# ==============================================================================

# 1. Creamos la clase Padre (reducida para el ejemplo)
class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.color = color

    def acelerar(self, aceleracion):
        try:
            self.velocidad_actual += aceleracion
            if self.velocidad_actual > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            print(f"[{self.marca} {self.modelo}] va a {self.velocidad_actual} km/h.")
        except TypeError:
            pass

# 2. Creamos la clase Hija 'Auto' que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, color, cantidad_puertas):
        # Usamos super() para cargar los datos en el constructor del padre
        super().__init__(marca, modelo, velocidad_maxima, color)
        self.cantidad_puertas = cantidad_puertas # Atributo

# 3. Creamos la clase Hija 'Bicicleta' que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, rodado):
        # La bici tiene velocidad máxima distinta, se la pasamos directo al padre
        super().__init__(marca, modelo, 40, color) 
        self.rodado = rodado

    # Sobrescribimos el método acelerar porque en la bici se pedalea
    def acelerar(self, aceleracion):
        try:
            self.velocidad_actual += aceleracion
            print(f"[{self.marca} Rodado {self.rodado}] Pedaleo más fuerte y voy a {self.velocidad_actual} km/h.")
        except TypeError:
            print("No sé pedalear así.")

# --- Probando la Herencia ---
print("--- Instanciando Auto ---")
# Acá 'construimos' el auto pasándole los datos
mi_coche = Auto("Toyota", "Corolla", 200, "Negro", 5)
# Acá le damos la orden de acelerar
mi_coche.acelerar(60) 

print("\n--- Instanciando Bicicleta ---")
# Acá 'construimos' la bici
mi_bici = Bicicleta("Trek", "Marlin", "Rojo", 29)
# Acá le damos la orden de acelerar
mi_bici.acelerar(15)