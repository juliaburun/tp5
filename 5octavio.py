#Ejercicio 5
D = int(input("ingrese el dia: "))
M = int(input("ingrese el mes: "))
A = int(input("ingrese el año: "))

N = int(input("ingrese cantidad de dias a sumar: "))
c = 0

while c < N:
    D = D + 1
    if D > 31 and ((M <= 7 and M%2 != 0) or (M >= 7 and M%2 == 0)): #Aca puse el patron que te decia de los meses con 31 dias
        D = 1
        M = M + 1
    elif D > 30 and ((M >= 7 and M%2 != 0) or (M <= 7 and M%2 == 0) and M != 2):#Estos son los de 30 dias
        M = M + 1
        D = 1
    elif D > 29 and M == 2 and ((A%4 == 0 and A%100 != 0) or (A%400 == 0)):#Estas son las condiciones de que sea bisiesto
        D = 1
        M = M + 1
    elif D > 28 and M == 2 and ((A%4 != 0) or (A%100 == 0)):#Y esto de cuando no son bisiestos
        D = 1
        M = M + 1
        
    if M == 13:#Si el mes pasa a ser 13, ya tengo que cambiar el año
        M = 1
        A = A + 1
    c = c + 1
    
print("la nueva fecha es", D, "/", M, "/", A)
