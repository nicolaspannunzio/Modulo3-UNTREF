# Trabajo Optativo N° 2 - UNTREF
# Módulo III
# Alumno: Nicolás Pannunzio

temperaturas = []

# --- Ingreso de datos ---
print("--- Registro de Temperaturas Semanales ---")
# Usamos un for simple para pedir el dato 7 veces
for i in range(7):
    # Pedimos la temperatura y la convertimos a float por si ingresan decimales
    temp = float(input(f"Ingresá la temperatura del día {i + 1}: "))
    temperaturas.append(temp)

# --- Bloque 1: Ciclo FOR (Temperaturas > 30) ---
dias_calurosos = 0

for temp in temperaturas:
    if temp > 30:
        dias_calurosos += 1

print("\n--- Resultados ---")
print(f"Total de días con temperatura mayor a 30 grados: {dias_calurosos}")

# --- Bloque 2: Ciclo WHILE (Temperaturas < 10) ---
print("\nDetalle de días con temperatura menor a 10 grados:")
indice = 0

# Mientras el índice sea menor a la cantidad de elementos en la lista
while indice < len(temperaturas):
    if temperaturas[indice] < 10:
        # Sumamos 1 al índice solo para que visualmente diga "Día 1" en vez de "Día 0"
        print(f"Día {indice + 1}: {temperaturas[indice]} grados")
    
    # Fundamental: incrementar el índice para que no sea un bucle infinito
    indice += 1