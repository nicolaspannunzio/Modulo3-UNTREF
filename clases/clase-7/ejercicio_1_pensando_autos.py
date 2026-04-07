# ==============================================================================
# Clase 7 - Ejercicio 1
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Pensando Objetos:
# Imaginemos que estamos automatizando una web donde se gestionan autos.
# Hasta ahora, usamos funciones, variables y listas para manejar la información.
# Ahora piensen:
# 1. ¿Qué atributos debería tener un auto (qué datos tiene)?
# 2. ¿Qué métodos podría tener ese auto (qué cosas puede hacer)?
# 3. ¿Qué ventajas tendría si juntamos toda esa información y 
# comportamientos en una misma estructura?
# ==============================================================================

"""
RESPUESTAS TEÓRICAS:
1. Atributos (datos/características): Marca, modelo, año, color, patente, kilometraje, estado_motor (encendido/apagado).
2. Métodos (acciones/comportamientos): arrancar(), acelerar(), frenar(), apagar(), obtener_informacion().
3. Ventajas: 
   - Organización: Tenemos todo lo relacionado al "Auto" en un solo lugar, sin tener variables sueltas por todo el código.
   - Reutilización: Podemos crear 100 autos distintos usando la misma "plantilla" o clase.
   - Mantenimiento: Si un auto necesita un nuevo dato (ej: tipo_combustible), lo agregamos a la clase y automáticamente todos los autos lo soportan.
"""

# EJEMPLO PRÁCTICO EN CÓDIGO (Para que veas cómo se aplica lo de arriba)
class Auto:
    # 1. Atributos (se definen en el método constructor __init__)
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False # Estado inicial

    # 2. Métodos (las cosas que puede hacer)
    def arrancar(self):
        self.encendido = True
        return f"El {self.marca} {self.modelo} acaba de arrancar. ¡Brum brum!"
    
    def detener(self):
        self.encendido = False
        return f"El {self.marca} se ha detenido."

# Imprimimos para probar nuestra clase
print("--- Gestión de Autos ---")
mi_auto = Auto("Ford", "Fiesta", "Azul")
print(f"Auto registrado: {mi_auto.marca} {mi_auto.modelo} ({mi_auto.color})")
print(mi_auto.arrancar())