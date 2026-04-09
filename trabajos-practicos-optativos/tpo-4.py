# ==============================================================================
# Trabajo Optativo N° 4
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Clase de Clases:
# Diseñar un "FormularioContacto" con nombre, email y mensaje.
# El método enviar() solo debería 'permitir' el envío si los tres campos 
# tienen contenido; si no, debe 'responder' con un mensaje claro por 
# campo faltante.
# Pensar 3 casos de prueba (completo, un campo vacío, todos vacíos).
# ==============================================================================

class FormularioContacto:
    def __init__(self, nombre, email, mensaje):
        # Usamos strip() como buena práctica de QA para evitar que 
        # el usuario burle el sistema ingresando solo espacios en blanco.
        self.nombre = nombre.strip()
        self.email = email.strip()
        self.mensaje = mensaje.strip()

    def enviar(self):
        campos_faltantes = []
        
        # Validamos campo por campo
        if not self.nombre:
            campos_faltantes.append("Nombre")
        if not self.email:
            campos_faltantes.append("Email")
        if not self.mensaje:
            campos_faltantes.append("Mensaje")
            
        # Si la lista de faltantes tiene elementos, fallamos la validación
        if len(campos_faltantes) > 0:
            print(f"❌ Error al enviar. Faltan completar los siguientes campos: {', '.join(campos_faltantes)}")
        else:
            print(f"✅ ¡Éxito! Mensaje enviado correctamente por {self.nombre} ({self.email}).")

# --- Batería de Casos de Prueba ---
print("--- Ejecutando Pruebas del Formulario ---")

print("\n1. Caso de prueba: Formulario Completo (Happy Path)")
form_completo = FormularioContacto("Nicolás", "nico@untref.edu.ar", "Hola, adjunto mis ejercicios finales.")
form_completo.enviar()

print("\n2. Caso de prueba: Un campo vacío (Sad Path - Faltan datos)")
# Simulamos que el usuario se olvidó de escribir el mensaje
form_incompleto = FormularioContacto("Tatiana", "profesora@untref.edu.ar", "")
form_incompleto.enviar()

print("\n3. Caso de prueba: Todos los campos vacíos (Sad Path - Formulario en blanco)")
# Le pasamos espacios en blanco al email para probar que el .strip() funciona bien
form_vacio = FormularioContacto("", "   ", "") 
form_vacio.enviar()