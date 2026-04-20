# ==============================================================================
# Clase 10 - Ejercicio 1
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Objetos:
# Crear 5 clases que hereden de su clase padre. Luego, invocar dichos 
# objetos y utilizar sus métodos.
# ==============================================================================

# 1. Creamos la clase Padre
class ProfesionalIT:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def trabajar(self):
        print(f"[{self.rol}] {self.nombre} está realizando sus tareas diarias.")

# 2. Creamos 5 clases hijas que heredan de ProfesionalIT
class Desarrollador(ProfesionalIT):
    def __init__(self, nombre):
        super().__init__(nombre, "Desarrollador Full Stack")
    
    def programar(self):
        print(f"👨‍💻 {self.nombre} está escribiendo código en Python y React.")

class QASpecialist(ProfesionalIT):
    def __init__(self, nombre):
        super().__init__(nombre, "QA Specialist")
        
    def testear(self):
        print(f"🔎 {self.nombre} está automatizando pruebas y buscando bugs.")

class DevOps(ProfesionalIT):
    def __init__(self, nombre):
        super().__init__(nombre, "DevOps Engineer")
        
    def desplegar(self):
        print(f"🚀 {self.nombre} está subiendo la nueva versión a producción.")

class DataScientist(ProfesionalIT):
    def __init__(self, nombre):
        super().__init__(nombre, "Data Scientist")
        
    def analizar(self):
        print(f"📊 {self.nombre} está entrenando un modelo de Machine Learning.")

class DisenadorUX(ProfesionalIT):
    def __init__(self, nombre):
        super().__init__(nombre, "Diseñador UX/UI")
        
    def disenar(self):
        print(f"🎨 {self.nombre} está armando los prototipos en Figma.")

# 3. Invocar objetos y utilizar métodos
print("--- Equipo de IT ---")
dev = Desarrollador("Lucas")
qa = QASpecialist("Nicolás")
ops = DevOps("Martina")
data = DataScientist("Sofía")
ux = DisenadorUX("Julieta")

# Usamos el método heredado del padre
qa.trabajar() 

# Usamos los métodos propios de cada clase hija
print("\n--- Tareas Específicas ---")
dev.programar()
qa.testear()
ops.desplegar()
data.analizar()
ux.disenar()