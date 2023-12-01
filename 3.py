#Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
#· Aplica el precio base a la primera docena de unidades.
#· Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#· Aplica un 25% de descuento a todas las unidades por encima de las 100.
#Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:
# 100 * 12 + 90 * 88 + 75 * 130 = 18870
# y el precio promedio es de 18870/230 = 82.04
# Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar:
# · Cantidad de ventas realizadas total.
# · Cantidad de ventas en las que se aplicó un 10% de descuento.
# · Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.

cantidad = int(input("Ingrese la cantidad de productos: "))
contador_base = 0
contador_descuento = 0
contador = 0

while cantidad != -1:
    
    precio_base = int(input("Ingrese el precio base: "))

    con_descuento_10 = precio_base - (precio_base * 0.1)
    con_descuento_25 = precio_base - (precio_base * 0.25)

    if cantidad < 13 and cantidad != -1:
        contador_base += 1
        total = precio_base
    elif cantidad > 12 and cantidad < 100:
        contador_descuento += 1
        total = precio_base * 12 + (con_descuento_10 * (cantidad - 12))
    else:
        total = precio_base * 12 + (con_descuento_10 * 88) + (con_descuento_25 * (cantidad - 100))

    if cantidad > 0:
        promedio = total / cantidad
    else:
        print("No se agregaron productos.")

    print("El total de la venta es de: ", total)
    print("Su precio promedio es de: ", promedio)

    cantidad = int(input("Ingrese la cantidad de productos: "))

    contador += 1
        

print("La cantidad de ventas total es de: ", contador)
print("La cantidad de ventas donde se aplicó 10 de descuento es de: ", contador_descuento)
print("La cantidad de ventas donde solo se aplicó el precio base es de: ", contador_base)