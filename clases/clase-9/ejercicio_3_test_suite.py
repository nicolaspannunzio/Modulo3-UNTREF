# ==============================================================================
# Clase 9 - Ejercicio 3
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Suite de Pruebas & Casos:
# QA necesita un resumen de ejecución de casos.
# Entidades: TestCase (id, nombre, pasos, estado), TestSuite (nombre, lista_casos)
# Estados permitidos: "PENDING", "PASS", "FAIL".
# Requerimientos: agregarCaso, marcarPass, marcarFail, resumen.
# ==============================================================================

# --- Definición de Entidades ---

class TestCase:
    def __init__(self, id_caso, nombre, pasos):
        self.id = id_caso
        self.nombre = nombre
        self.pasos = pasos
        # Todo caso nace como pendiente
        self.estado = "PENDING"

class TestSuite:
    def __init__(self, nombre):
        self.nombre = nombre
        self.casos = []

    def agregarCaso(self, caso):
        # Aseguramos que al entrar a la suite, el estado inicial sea PENDING
        caso.estado = "PENDING"
        self.casos.append(caso)
        print(f"➕ Caso agregado: [TC-{caso.id}] {caso.nombre} (Estado: {caso.estado})")

    # Método interno privado (convención con guion bajo) para reutilizar lógica
    def _cambiarEstado(self, id_caso, nuevo_estado):
        # Validación de Criterio de Aceptación: Solo permite estados específicos
        if nuevo_estado not in ["PENDING", "PASS", "FAIL"]:
            print(f"❌ Error: El estado '{nuevo_estado}' no es válido.")
            return

        # Buscamos el caso por ID
        for caso in self.casos:
            if caso.id == id_caso:
                caso.estado = nuevo_estado
                print(f"✔️ Update: [TC-{id_caso}] ha cambiado a estado {nuevo_estado}.")
                return
        
        # Si termina el bucle y no lo encontró:
        print(f"❌ Error: No se encontró ningún Test Case con el ID {id_caso}.")

    def marcarPass(self, id_caso):
        self._cambiarEstado(id_caso, "PASS")

    def marcarFail(self, id_caso):
        self._cambiarEstado(id_caso, "FAIL")

    def resumen(self):
        # Inicializamos contadores
        conteo = {"PENDING": 0, "PASS": 0, "FAIL": 0}
        
        # Contamos iterando sobre la lista
        for caso in self.casos:
            conteo[caso.estado] += 1
            
        print(f"\n📊 Resumen de Suite '{self.nombre}':")
        print(f"  🟩 PASS:    {conteo['PASS']}")
        print(f"  🟥 FAIL:    {conteo['FAIL']}")
        print(f"  ⬜ PENDING: {conteo['PENDING']}")
        print(f"  -----------------")
        print(f"  Total Casos: {len(self.casos)}\n")


# --- Ejecución y Escenarios de Prueba QA ---

print("--- Iniciando Gestor de QA ---")
suite_regresion = TestSuite("Regresión E-commerce v2.0")

# Creamos las instancias de los casos
tc1 = TestCase(1, "Login con credenciales válidas", 3)
tc2 = TestCase(2, "Agregar producto al carrito", 5)
tc3 = TestCase(3, "Checkout con tarjeta expirada", 4)
tc4 = TestCase(4, "Recuperar contraseña", 2)

print("\n--- Escenario 1: Agregar 4 casos y setear (2 PASS, 1 FAIL, 1 PENDING) ---")
suite_regresion.agregarCaso(tc1)
suite_regresion.agregarCaso(tc2)
suite_regresion.agregarCaso(tc3)
suite_regresion.agregarCaso(tc4)

print("\nEjecutando pruebas...")
suite_regresion.marcarPass(1) # PASS
suite_regresion.marcarPass(2) # PASS
suite_regresion.marcarFail(3) # FAIL
# El TC 4 queda intacto, por lo que retiene su estado "PENDING"

# Verificamos que el resumen muestre la suma correcta
suite_regresion.resumen()

print("--- Escenario 2: Marcar FAIL sobre un id inexistente ---")
# Intentamos fallar el TC 99 que no existe
suite_regresion.marcarFail(99) 

print("\n--- Escenario 3: Cambiar un FAIL a PASS ---")
# El desarrollador arregló el bug del TC 3, lo volvemos a correr y pasa
suite_regresion.marcarPass(3)
# El resumen se debe actualizar y mostrar 3 PASS y 0 FAIL
suite_regresion.resumen()