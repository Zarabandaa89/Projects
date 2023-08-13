def esta_en_rango(numero, rango_inicio, rango_fin):
    return rango_inicio <= numero <= rango_fin


numero = int(input("ingrese el numero a verificar si esta en el rango:"))

inicio = int(input("Digite el valor del rango inicial:"))

fin = int(input("Digite el valor del rango final:  "))


if esta_en_rango(numero, inicio, fin):
    print(f"El número {numero} está en el rango [{inicio}, {fin}]")
    
else:
    print(f"El número {numero} no está en el rango [{inicio}, {fin}]")



