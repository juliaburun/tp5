#Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3). 
#Por cada empleado se lee su legajo, categoría y salario. 
#Se solicita elaborar un informe que contenga:
#· Importe total de salarios pagados por la empresa.
#· Cantidad de empleados que ganan más de $200000.
#· Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3.
#· Legajo del empleado que más gana.
#· Sueldo más bajo.
#· Importe total de sueldos por cada categoría. 
#· Salario promedio

legajo = int(input("Ingrese el legajo o -1 para salir: "))

total_salarios = 0
empleados_senior = 0
empleados_junior = 0
flag = True
flag2 = True
legajo_mas_gana = 0
sueldo_mas_bajo = 0
sueldo_mas_alto = 0
importe_cat_1 = 0
importe_cat_2 = 0
importe_cat_3 = 0
acum_salarios = 0
contador = 0

while legajo != -1:

    categoria = int(input("Ingrese la categoria (1, 2 o 3): "))
    salario = int(input("Ingrese el salario: "))

    if legajo < 0:
        legajo = int(input("Reingrese el legajo, no puede ser menor a 0: "))

    if categoria != 1 and categoria != 2 and categoria != 3:
        categoria = int(input("Reingrese la categoria (1, 2 o 3): "))
    
    total_salarios += salario

    if salario > 200000:
        empleados_senior += 1
    elif salario < 50000 and categoria == 3:
        empleados_junior +=1

    if flag:
        legajo_mas_gana = legajo
        sueldo_mas_alto = salario
        flag = False
    elif salario > sueldo_mas_alto:
        sueldo_mas_alto = salario
        legajo_mas_gana = legajo
    
    if flag2:
        sueldo_mas_bajo = salario
        flag2 = False
    elif salario < sueldo_mas_bajo:
        sueldo_mas_bajo = salario

    if categoria == 1:
        importe_cat_1 += salario
    elif categoria == 2:
        importe_cat_2 += salario
    else:
        importe_cat_3 += salario

    acum_salarios += salario
    contador += 1

    legajo = int(input("Ingrese el legajo o -1 para salir: "))

if contador > 0:
    promedio = acum_salarios / contador
else:
    print("No se ingresaron datos")

print("Importe total de salarios pagados por la empresa: ", total_salarios)
print("Cantidad de empleados que ganan más de $200000: ", empleados_senior)
print("Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3: ", empleados_junior)
print("Legajo del empleado que más gana: ", legajo_mas_gana)
print("Sueldo más bajo: ", sueldo_mas_bajo)
print("Importe total de sueldos por cada categoría:")
print("Categoria 1: ", importe_cat_1)
print("Categoria 2: ", importe_cat_2)
print("Categoria 3: ", importe_cat_3)
print("Salario promedio: ", promedio)
