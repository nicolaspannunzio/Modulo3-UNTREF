# ==============================================================================
# Clase 7 - Ejercicio 2
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Plataforma educativa:
# Estás participando en la creación de una plataforma educativa.
# Queremos automatizar pruebas sobre distintos aspectos del sistema.
# Indicar:
# 1. ¿Qué objetos podrías identificar dentro de la plataforma?
# 2. Elegí uno (por ejemplo, una clase virtual, un usuario, una tarea)
# 3. Indicá qué atributos tendría
# 4. Indicá qué métodos podría tener
# 5. ¿Por qué te resultaría útil pensar ese objeto como una clase 
# en tu código de automatización?
# ==============================================================================

"""
RESPUESTAS TEÓRICAS:
1. Objetos identificables: Usuario (Estudiante/Profesor), Curso, ClaseVirtual, Tarea, Examen, Certificado, Foro.
2. Objeto elegido: Usuario (Estudiante).
3. Atributos del Estudiante: nombre, apellido, email, contraseña, cursos_inscritos, progreso_actual.
4. Métodos del Estudiante: iniciar_sesion(), inscribirse_a_curso(), entregar_tarea(), ver_calificaciones(), cerrar_sesion().

5. UTILIDAD EN QA AUTOMATION:
Pensar esto como una clase es la base del patrón POM (Page Object Model). 
Si creo una clase "Usuario", en mis scripts de prueba (tests) no tengo que repetir 
el código de login 50 veces. Simplemente llamo a `usuario_prueba.iniciar_sesion()`. 
Si mañana los desarrolladores cambian cómo funciona el login en la web, solo corrijo 
el método dentro de mi clase "Usuario" y todos mis 50 tests se arreglan automáticamente.
"""

# EJEMPLO PRÁCTICO EN CÓDIGO
class UsuarioEstudiante:
    # Atributos
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.sesion_iniciada = False

    # Métodos
    def iniciar_sesion(self, password_ingresada):
        # Simulamos una validación de QA
        if password_ingresada == "123456":
            self.sesion_iniciada = True
            return f"[{self.nombre}] Login Exitoso. Acceso al dashboard concedido."
        else:
            return f"[{self.nombre}] Error de Login. Credenciales incorrectas."

# Probando nuestra clase como si fuera un script de automatización
print("--- Test de Automatización: Login de Usuario ---")
estudiante_qa = UsuarioEstudiante("Nicolás Pannunzio", "nico@untref.edu.ar")

print("Intento 1 (Fallo esperado):", estudiante_qa.iniciar_sesion("clave_equivocada"))
print("Intento 2 (Éxito esperado):", estudiante_qa.iniciar_sesion("123456"))