def factorial(n):
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


no_negativo = int(input("Ingrese un numero entero NO NEGATIVO:"))


resultado = factorial(no_negativo)

print(f"El factorial de {no_negativo} es: {resultado}")
