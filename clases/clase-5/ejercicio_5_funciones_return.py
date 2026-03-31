# Clase 5 - Ejercicio 5
# Módulo III - UNTREF
# Alumno: Nicolás Pannunzio

# 1 y 2. Armar función y crear algoritmo para encontrar el mayor.
def encontrar_valor_mas_alto():
    valor_mas_alto = None
    
    print("Ingresá 5 números para encontrar el mayor:")
    for i in range(5):
        numero = int(input(f"Valor {i + 1}: "))
        
        # Si es la primera iteración o el número actual es mayor al guardado
        if valor_mas_alto is None or numero > valor_mas_alto:
            valor_mas_alto = numero
            
    # Retornamos el valor más alto encontrado
    return valor_mas_alto

# 3 y 4. Instanciar la variable que recibirá el valor llamando a la función.
resultado_mayor = encontrar_valor_mas_alto()

# 5. Escribir un print con la variable retornada.
print(f"\nEl valor más alto ingresado fue: {resultado_mayor}")