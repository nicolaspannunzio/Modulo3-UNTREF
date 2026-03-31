### UNTREF - DIPLOMATURA QA ###
### Clase 4 - Ejercicio 3 ###

# 1 y 2. Crear una lista con 5 nombres y mostrarlos en terminal.
nombres = ["Julia", "Margarita", "Tino", "Lucía", "Nicolás"]
print("Nuestra lista original es:")
print(nombres)

# 3. Remover el nombre en la posición 3.
# Nota: Los índices empiezan en 0, así que la posición 3 es el índice 2.
# En Python usamos pop() para remover por índice.
nombres.pop(2) 

# Si quisieras forzar el uso de la palabra 'remove' como dice la consigna, sería así:
# nombres.remove(nombres[2])

# 4. Agregar un nuevo nombre al final de la lista.
# Nota: En Python el equivalente a 'push' es 'append'.
nombres.append("Julieta")

# 5. Mostrar en terminal cómo quedó la lista.
print("\nLa lista final después de los cambios:")
print(nombres)