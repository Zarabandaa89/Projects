def lista_multiplicacion():
    numeros = [8, 2, 3, -1, 7]
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado
print("La multiplicacion de los numeros es: ",lista_multiplicacion())