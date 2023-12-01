#Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el número invertido. Tener en cuenta que el número puede ser negativo. Por ejemplo, si se ingresa 1234 debe mostrar 4321.

# Leer un número entero
numero = int(input("Ingrese un número entero: "))

# Variable para almacenar el número invertido
numero_invertido = 0
es_negativo = False

if numero < 0:
    es_negativo = True
    numero *= -1  # Convertir el número negativo en positivo

while numero > 0:
    # Obtener la última cifra del número
    cifra = numero % 10
    # Agregar la cifra al número invertido
    numero_invertido = numero_invertido * 10 + cifra
    # Eliminar la última cifra del número original
    numero = numero // 10

if es_negativo:
    print(f"El número invertido es: -{numero_invertido}")
else:
    print(f"El número invertido es: {numero_invertido}")
