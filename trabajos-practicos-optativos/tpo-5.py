# ==============================================================================
# Trabajo Optativo N° 5
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio
#
# ENUNCIADO:
# Control de Saldo:
# Un cajero automático tiene que decidir si entrega el dinero o no.
# Los datos que tiene son: saldo_disponible y monto_a_retirar.
# Explicar con palabras el paso a paso de la lógica que debería seguir 
# el cajero para aprobar la operación, rechazarla si el monto es mayor 
# al saldo y rechazarla si el monto es igual a 0.
# ==============================================================================

def cajero_automatico(saldo_disponible, monto_a_retirar):
    print(f"\n--- Iniciando transacción ---")
    print(f"Saldo en cuenta: ${saldo_disponible} | Monto solicitado: ${monto_a_retirar}")
    
    # PASO 1: Rechazar si el monto es 0 (o negativo)
    if monto_a_retirar <= 0:
        print("❌ Operación rechazada: El monto a retirar debe ser mayor a $0.")
        return saldo_disponible
        
    # PASO 2: Rechazar si el monto es mayor al saldo
    elif monto_a_retirar > saldo_disponible:
        print("❌ Operación rechazada: Fondos insuficientes.")
        return saldo_disponible
        
    # PASO 3: Aprobar si pasa las validaciones anteriores
    else:
        saldo_disponible -= monto_a_retirar
        print("✅ Operación aprobada: Entregando el dinero...")
        print(f"💳 Su nuevo saldo disponible es: ${saldo_disponible}")
        return saldo_disponible

# --- Escenarios de Prueba QA ---
print("--- Pruebas del Cajero Automático ---")

# Caso 1: Intentar retirar $0 (Debe rechazar)
cajero_automatico(1000, 0)

# Caso 2: Intentar retirar más de lo que hay (Debe rechazar)
cajero_automatico(1000, 1500)

# Caso 3: Retiro exitoso (Debe aprobar y descontar)
cajero_automatico(1000, 300)