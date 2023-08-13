def calcular_promedio(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

def main():
    numeros = []
    for i in range(5):
        try:
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)
        except ValueError:
            print("Error: Ingrese un número válido.")
            return

    promedio = calcular_promedio(numeros)
    print("El promedio de los números ingresados es:", promedio)

if __name__ == "__main__":
    main()
