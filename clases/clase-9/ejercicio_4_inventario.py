# ==============================================================================
# Clase 9 - Ejercicio 4
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Inventario & Valorización:
# Logística necesita controlar stock y valor de inventario.
# Entidades: Producto (nombre, precio), Inventario (ítems: producto + cantidad).
# Requerimientos: agregar, remover, stockDe, valorTotal.
# Reglas: No precio <= 0, no cantidad <= 0, no stock negativo, sumar si existe.
# ==============================================================================

# --- Definición de Entidades ---

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Inventario:
    def __init__(self):
        # Usamos un diccionario donde la clave es el nombre del producto
        # y el valor es un sub-diccionario con el objeto 'producto' y su 'cantidad'
        self.items = {}

    def agregar(self, producto, cantidad):
        # Criterio de Aceptación: No se aceptan cantidades <= 0
        if cantidad <= 0:
            print(f"❌ Error: La cantidad a agregar debe ser mayor a 0.")
            return
            
        # Criterio de Aceptación: No se agregan productos con precio <= 0
        if producto.precio <= 0:
            print(f"❌ Error: El producto '{producto.nombre}' tiene un precio inválido (${producto.precio}).")
            return

        # Si ya existe, sumamos la cantidad
        if producto.nombre in self.items:
            self.items[producto.nombre]["cantidad"] += cantidad
            print(f"➕ Update: Se sumaron {cantidad}u de '{producto.nombre}'. Stock nuevo: {self.items[producto.nombre]['cantidad']}u.")
        # Si no existe, lo creamos en el diccionario
        else:
            self.items[producto.nombre] = {"producto": producto, "cantidad": cantidad}
            print(f"✅ Alta: Producto '{producto.nombre}' agregado con {cantidad}u.")

    def remover(self, nombre_producto, cantidad):
        # Validación de cantidad positiva
        if cantidad <= 0:
            print(f"❌ Error: La cantidad a remover debe ser mayor a 0.")
            return
            
        # Validación de existencia
        if nombre_producto not in self.items:
            print(f"❌ Error: El producto '{nombre_producto}' no existe en el inventario.")
            return
            
        stock_actual = self.items[nombre_producto]["cantidad"]
        
        # Validación de stock negativo
        if cantidad > stock_actual:
            print(f"⚠️ Operación denegada: Querés remover {cantidad}u pero solo hay {stock_actual}u de '{nombre_producto}'.")
            return
            
        # Si pasa todas las validaciones, restamos
        self.items[nombre_producto]["cantidad"] -= cantidad
        print(f"➖ Baja: Se removieron {cantidad}u de '{nombre_producto}'. Stock restante: {self.items[nombre_producto]['cantidad']}u.")

    def stockDe(self, nombre_producto):
        if nombre_producto in self.items:
            return self.items[nombre_producto]["cantidad"]
        return 0

    def valorTotal(self):
        total = 0
        for item in self.items.values():
            # Multiplicamos el precio del objeto Producto por la cantidad en el inventario
            total += item["producto"].precio * item["cantidad"]
        return total


# --- Ejecución y Escenarios de Prueba QA ---

print("--- Iniciando Sistema de Inventario ---")
mi_inventario = Inventario()

print("\n--- Escenario 1: Agregar A(10$, 3u) y B(25$, 2u) ---")
prod_A = Producto("A", 10)
prod_B = Producto("B", 25)

mi_inventario.agregar(prod_A, 3)
mi_inventario.agregar(prod_B, 2)

# Calculo: (10 * 3) + (25 * 2) = 30 + 50 = 80
print(f"💰 Valor Total (Esperado: $80) -> ${mi_inventario.valorTotal()}")

print("\n--- Escenario 2: Agregar más de A (2u) ---")
mi_inventario.agregar(prod_A, 2)
print(f"📦 Stock de 'A' (Esperado: 5u) -> {mi_inventario.stockDe('A')}u")

print("\n--- Escenario 3: Remover más de lo existente ---")
# Intentamos remover 5 unidades de B, pero solo hay 2
mi_inventario.remover("B", 5)

print("\n--- Escenario 4: Intentar agregar C con precio 0 ---")
prod_C = Producto("C", 0)
mi_inventario.agregar(prod_C, 1)