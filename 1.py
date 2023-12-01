#Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válida una edad entre 0 y 100).

edad = None
contador_menores = 0
suma_menores = 0
contador_mayores = 0
suma_mayores = 0

while edad != -1:

    edad = int(input("Ingrese la edad: "))
    if edad < -1 or edad > 100:
        edad = int(input("Ingrese una edad válida (0-100): "))
    
    if edad != -1:
        if edad < 18:
            contador_menores += 1
            suma_menores += edad
        else:
            contador_mayores += 1
            suma_mayores += edad

if contador_menores > 0:
    promedio_menores = suma_menores / contador_menores
    print("El promedio de menores es de: ", promedio_menores)
else:
    print("No hay datos de menores ingresados")

if contador_mayores > 0:
    promedio_mayores = suma_mayores / contador_mayores
    print("El promedio de mayores es de: ", promedio_mayores)
else:
    print("No hay datos de mayores ingresados")

