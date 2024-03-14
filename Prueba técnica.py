
print("------------ Bienvenido al restaurante ---------")
nombre = str(input("Buen día. Ingrese su nombre: "))
compras = int(input("Ingrese el monto de su compra: "))


if (compras>=200000):
    descuento1 = compras*0.15
    total1 = compras-descuento1
    print("-------- Factura --------")
    print(f"{nombre} debes pagar el total de {compras} \nPero como tienes descuento de 15% ahora debes pagar {total1}. \n¡Muchas gracias por comprar en nuestra tienda!")

    
elif(compras>=50000):
    descuento2 = compras*0.02
    total2 = compras-descuento2
    print("-------- Factura --------")
    print(f"{nombre} debes pagar el total de {compras} \nPero como tienes descuento de 2% ahora debes pagar {total2}. \n¡Muchas gracias por comprar en nuestra tienda!")
    

elif(compras>=20000):
    descuento3 = compras*0.015
    total3 = compras-descuento3
    print("-------- Factura --------")
    print(f"{nombre} debes pagar el total de {compras} \nPero como tienes descuento de 1.5% ahora debes pagar {total3}. \n¡Muchas gracias por comprar en nuestra tienda!")

elif(compras<20000):
    print("-------- Factura --------")
    print(f"{nombre} debes pagar el total de {compras} \nYa que no hay descuento. \n¡Muchas gracias por comprar en nuestra tienda!")