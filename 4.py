#Una empresa factura a sus clientes el último día de cada mes. 
#Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente. 
#Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura, mientras que 
#si paga después del día 20 deberá abonar una multa de $350 o del 10% de su factura, lo que resulte mayor. 
#Escribir un programa que lea el número del cliente y el total de la factura, y emita un informe donde conste el número del cliente y los tres importes que podría abonar según la fecha de pago.

# CONSULTAR

#num_cliente = int(input("Ingrese el numero de cliente: "))
factura_total = int(input("Ingrese el monto total de la factura: "))

dia = 0

while dia < 31:

    if dia < 10:
        precio_desc_2 = factura_total - (factura_total * 0.02)
        precio_desc_200 = factura_total - 200

        if precio_desc_2 < precio_desc_200 or factura_total < 150:
            precio_desc = precio_desc_2
        else:
            precio_desc = precio_desc_200

    elif dia > 10 and dia < 20:
        precio_total = factura_total
    else:
        precio_aum_350 = factura_total + 350
        precio_aum_10 = factura_total + (factura_total * 0.1)

        if precio_aum_350 < precio_aum_10:
            precio_multa = precio_aum_350
        else:
            precio_multa = precio_aum_10
    
    dia += 1

print("Los tres importes que podria abonar son: ")
print("Con descuento: ", precio_desc)
print("Sin descuento ni aumento: ", precio_total)
print("Con aumento: ", precio_multa)