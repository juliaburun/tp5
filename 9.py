#Ingresar un número N y validar que sea positivo. Luego:
#a. Mostrar los primeros números impares, hasta alcanzar el número ingresado. 
#b. Informar la suma de esos números impares.
#Ejemplo:
#· Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
#· Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16. 
#· Si se ingresa -5, se debe pedir otro número.

n = int(input("Ingresa un número positivo: "))

if n <= 0:
    print("Por favor, ingresa un número positivo.")
else:
    current = 1
    suma_impares = 0

    while current <= n:

        if current % 2 != 0:
            print(current)
            suma_impares += current
            
        current += 1
    
    print("\nLa suma de los números impares es:", suma_impares)





