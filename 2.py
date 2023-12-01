#Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
#· Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
#· Cantidad de alumnos que desaprobaron el examen con nota menor a 4. 
#· Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

legajo= None
contador_aprobados = 0
contador_desaprobados = 0
contador_aplazados = 0
contador = 0

while legajo != -1:

    legajo = int(input("Ingrese el numero de legajo: "))

    if legajo != -1:
        nota = int(input("Ingrese la nota de examen final: "))

    if nota < 0 or nota > 10:
        nota = int(input("Reingrese la nota de examen final (0-10): "))
    
    if nota >= 4:
        contador_aprobados += 1
    elif nota == 1:
        contador_aplazados += 1
    else:
        contador_desaprobados += 1
    
    contador += 1
    
if contador > 0:
        porcentaje_aplazados = contador_aplazados / contador * 100
else:
    print("No se ingresaron datos.")

print("Cantidad de alumnos que aprobaron con nota mayor o igual a 4: ", contador_aprobados)
print("Cantidad de alumnos que desaprobaron el examen con nota menor a 4: ", contador_desaprobados)
print("Porcentaje de alumnos que están aplazados: ", porcentaje_aplazados)