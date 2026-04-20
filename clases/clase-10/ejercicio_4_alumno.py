# ==============================================================================
# Clase 10 - Ejercicio 4
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Alumno:
# Crear una clase Alumno con atributos nombre y notas (lista vacía).
# Métodos: agregar_nota (0 a 10), promedio(), estado() (>= 6 Aprobado).
# Prueba: crear un alumno, agregarle 3 notas, mostrar promedio y estado.
# ==============================================================================

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        # Validación requerida: solo acepta notas entre 0 y 10
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f"📝 Nota {nota} agregada correctamente a {self.nombre}.")
        else:
            print(f"❌ Error: La nota {nota} no es válida. Debe estar entre 0 y 10.")

    def promedio(self):
        # Validamos que la lista no esté vacía para evitar errores matemáticos
        if len(self.notas) == 0:
            return 0
            
        suma = sum(self.notas)
        return suma / len(self.notas)

    def estado(self):
        promedio_actual = self.promedio()
        
        if len(self.notas) == 0:
            print(f"[{self.nombre}] Estado: Sin calificar (No hay notas ingresadas).")
            return
            
        if promedio_actual >= 6:
            print(f"🎓 [{self.nombre}] Estado: APROBADO (Promedio: {promedio_actual:.2f})")
        else:
            print(f"📚 [{self.nombre}] Estado: DESAPROBADO (Promedio: {promedio_actual:.2f})")


# --- Prueba solicitada ---
print("--- Sistema de Gestión de Alumnos ---")
# 1. Crear un alumno
estudiante = Alumno("Nicolás Pannunzio")

# 2. Agregarle 3 notas
estudiante.agregar_nota(8)
estudiante.agregar_nota(5)
estudiante.agregar_nota(9)

# (Prueba QA extra: Intentar agregar una nota inválida)
estudiante.agregar_nota(12) 

print("\n--- Resultados Finales ---")
# 3. Mostrar promedio y estado
promedio_final = estudiante.promedio()
print(f"El promedio calculado es: {promedio_final:.2f}")
estudiante.estado()