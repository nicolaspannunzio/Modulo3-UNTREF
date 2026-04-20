# ==============================================================================
# Clase 9 - Ejercicio 1
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Newsletter & Suscriptores:
# Marketing necesita administrar suscriptores de un boletín.
# Objetivo técnico: modelar dos objetos que interactúan.
# Entidades: Suscriptor (nombre, email), Newsletter (nombre, lista).
# Requerimientos: suscribir (sin repetidos), desuscribir (validar), totalSuscriptores.
# Escenarios: 1) Alta con repetido, 2) Baja exitosa, 3) Baja inexistente.
# ==============================================================================

# --- Definición de Entidades ---

class Suscriptor:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Newsletter:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscriptores = []  # Arranca como una lista vacía

    def suscribir(self, nuevo_suscriptor):
        # Validamos que el email no esté repetido recorriendo la lista actual
        for suscriptor_existente in self.suscriptores:
            if suscriptor_existente.email == nuevo_suscriptor.email:
                print(f"❌ Error: El email '{nuevo_suscriptor.email}' ya está suscrito.")
                return # Cortamos la ejecución del método para que no lo agregue

        # Si el loop termina sin encontrar repetidos, lo agregamos
        self.suscriptores.append(nuevo_suscriptor)
        print(f"✅ Éxito: '{nuevo_suscriptor.nombre}' se ha suscrito correctamente.")

    def desuscribir(self, email_baja):
        for suscriptor in self.suscriptores:
            if suscriptor.email == email_baja:
                self.suscriptores.remove(suscriptor)
                print(f"✅ Baja exitosa: Se eliminó la suscripción de '{email_baja}'.")
                return # Cortamos porque ya lo encontramos y borramos
        
        # Si termina el for y no hizo el return, significa que no existía
        print(f"⚠️ Atención: No se encontró ningún suscriptor con el email '{email_baja}'.")

    def totalSuscriptores(self):
        return len(self.suscriptores)

# --- Ejecución y Escenarios de Prueba QA ---

print("--- Iniciando Sistema de Newsletter ---")
mi_boletin = Newsletter("Novedades IT & QA")

# Creamos los objetos Suscriptor
sub1 = Suscriptor("Nicolás", "nico@untref.edu.ar")
sub2 = Suscriptor("Margarita", "margarita@guau.com")
sub3 = Suscriptor("Nico Falso", "nico@untref.edu.ar") # Email intencionalmente repetido

print("\n--- Escenario 1: Suscribir 3 personas (una repetida) ---")
mi_boletin.suscribir(sub1)
mi_boletin.suscribir(sub2)
mi_boletin.suscribir(sub3)
print(f"Total de suscriptores (Esperado: 2) -> {mi_boletin.totalSuscriptores()}")

print("\n--- Escenario 2: Desuscribir un email existente ---")
mi_boletin.desuscribir("margarita@guau.com")
print(f"Total de suscriptores (Esperado: 1) -> {mi_boletin.totalSuscriptores()}")

print("\n--- Escenario 3: Desuscribir un email inexistente ---")
mi_boletin.desuscribir("fantasma@correo.com")
print(f"Total final (Esperado: 1) -> {mi_boletin.totalSuscriptores()}")