def calcular_porcentaje(numero, porcentaje):
    return (numero * porcentaje) / 100

try:
    numero = float(input("Ingrese un número: "))
    porcentaje = 20

    resultado = calcular_porcentaje(numero, porcentaje)

    print(f"El 20% de {numero} es: {resultado:.2f}")
except ValueError:
    print("Error: Ingrese un número válido.")

        