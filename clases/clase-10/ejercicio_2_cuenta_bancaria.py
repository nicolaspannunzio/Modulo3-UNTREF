# ==============================================================================
# Clase 10 - Ejercicio 2
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Cuenta Bancaria:
# Crear una clase CuentaBancaria con atributos titular y saldo.
# Métodos: depositar(monto), retirar(monto), mostrar_saldo().
# Prueba: crear cuenta con 1000 iniciales, depositar 500, 
# intentar retirar 2000 y luego 700.
# ==============================================================================

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"⬆️ Depósito exitoso de ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("❌ Error: El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto):
        if monto <= 0:
            print("❌ Error: El monto a retirar debe ser mayor a 0.")
            return

        if monto > self.saldo:
            print(f"⚠️ Operación denegada: Fondos insuficientes. Intentaste retirar ${monto} pero tu saldo es ${self.saldo}.")
        else:
            self.saldo -= monto
            print(f"⬇️ Retiro exitoso de ${monto}. Saldo restante: ${self.saldo}")

    def mostrar_saldo(self):
        print(f"💳 Saldo actual de {self.titular}: ${self.saldo}")


# --- Prueba solicitada ---
print("--- Operaciones Bancarias ---")
# 1. Crear cuenta con 1000 iniciales
mi_cuenta = CuentaBancaria("Nicolás Pannunzio", 1000)
mi_cuenta.mostrar_saldo()

# 2. Depositar 500
mi_cuenta.depositar(500)

# 3. Intentar retirar 2000
mi_cuenta.retirar(2000)

# 4. Retirar 700
mi_cuenta.retirar(700)