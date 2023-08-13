def lista_pares():
    numeros = [1,4,3,6,8,9,12]
    pares = [num for num in numeros if num % 2 == 0]
    
    if len(pares) > 0:
        print("Los numeros pares en la lista [1,4,3,6,8,9,12] son:",pares)
    else:
        print("No hay mas numeros pares")

lista_pares()