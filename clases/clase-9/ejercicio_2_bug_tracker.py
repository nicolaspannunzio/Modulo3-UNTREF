# ==============================================================================
# Clase 9 - Ejercicio 2
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Bug Tracker Lite:
# Un equipo necesita registrar y cerrar bugs en un proyecto.
# Objetivo técnico: múltiples objetos con estados sencillos.
# Entidades: Bug (id, título, severidad, estado), Proyecto (nombre, lista_bugs).
# Requerimientos: reportarBug, cerrarBug, listarAbiertos, contarPorSeveridad.
# ==============================================================================

# --- Definición de Entidades ---

class Bug:
    def __init__(self, id_bug, titulo, severidad):
        self.id = id_bug
        self.titulo = titulo
        self.severidad = severidad
        self.estado = "open" # Todo bug nace con estado abierto

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bugs = []
        self.contador_id = 1 # Usamos esto para auto-generar IDs únicos

    def reportarBug(self, titulo, severidad):
        # Criterio de Aceptación: Severidad solo admite low/medium/high
        if severidad not in ["low", "medium", "high"]:
            print(f"❌ Error: La severidad '{severidad}' no es válida para el bug '{titulo}'.")
            return

        # Instanciamos el Bug y lo guardamos
        nuevo_bug = Bug(self.contador_id, titulo, severidad)
        self.bugs.append(nuevo_bug)
        print(f"🐛 Bug reportado: [ID {nuevo_bug.id}] {nuevo_bug.titulo} (Severidad: {nuevo_bug.severidad})")
        
        # Aumentamos el contador para el próximo bug
        self.contador_id += 1

    def cerrarBug(self, id_bug):
        for bug in self.bugs:
            if bug.id == id_bug:
                # Criterio de Aceptación: Un bug cerrado no cambia de estado si se intenta cerrar de nuevo
                if bug.estado == "closed":
                    print(f"⚠️ Atención: El bug [ID {id_bug}] ya se encontraba cerrado.")
                else:
                    bug.estado = "closed"
                    print(f"✅ Éxito: El bug [ID {id_bug}] ha sido cerrado correctamente.")
                return
        
        print(f"❌ Error: No se encontró ningún bug con el ID {id_bug}.")

    def listarAbiertos(self):
        print(f"\n--- Listado de Bugs Abiertos en '{self.nombre}' ---")
        # Criterio de Aceptación: Devuelve solo los "open"
        bugs_abiertos = [bug for bug in self.bugs if bug.estado == "open"]
        
        if not bugs_abiertos:
            print("🎉 No hay bugs abiertos. ¡Todo limpio!")
        else:
            for bug in bugs_abiertos:
                print(f"- [ID {bug.id}] {bug.titulo} ({bug.severidad})")

    def contarPorSeveridad(self, severidad):
        contador = 0
        for bug in self.bugs:
            if bug.severidad == severidad:
                contador += 1
        return contador


# --- Ejecución y Escenarios de Prueba QA ---

print("--- Iniciando Bug Tracker Lite ---")
mi_proyecto = Proyecto("E-commerce Juguetería")

print("\n--- Escenario 1: Reportar 3 bugs (1 high, 2 medium) ---")
mi_proyecto.reportarBug("El botón de pago no funciona", "high")
mi_proyecto.reportarBug("Error tipográfico en el footer", "medium")
mi_proyecto.reportarBug("La imagen del producto carga lento", "medium")

# Prueba extra de QA para validar que el filtro de severidad funciona:
mi_proyecto.reportarBug("Color incorrecto", "invalid_severity") 

total_medium = mi_proyecto.contarPorSeveridad("medium")
print(f"-> Total de bugs 'medium' (Esperado: 2): {total_medium}")

print("\n--- Escenario 2: Cerrar 1 bug e imprimir listado ---")
# Cerramos el bug del error tipográfico (que tiene el ID 2)
mi_proyecto.cerrarBug(2)
# Al listar, ya no debería aparecer el ID 2
mi_proyecto.listarAbiertos()

print("\n--- Escenario 3: Cerrar un bug dos veces ---")
# Intentamos cerrar el ID 2 nuevamente para ver el mensaje de validación
mi_proyecto.cerrarBug(2)