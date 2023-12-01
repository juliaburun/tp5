#Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene. Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa 12345 se debe imprimir 5.

numero = int(input("Ingrese un número entero: "))
conteo_digitos = 0

# Pasar a positivo
if numero < 0:
    numero *= -1

if numero == 0:
    conteo_digitos = 1
else:
    while numero > 0:
        numero = numero // 10  # Eliminar el último dígito
        conteo_digitos += 1
        
print(f"El número tiene {conteo_digitos} dígitos.")
