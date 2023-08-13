def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa_1= cateto1**2 + cateto2**2
    hipotenusa = hipotenusa_1**0.5
    return hipotenusa

def main():
    try:
        cateto1 = float(input("Ingrese la longitud del primer cateto: "))
        cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

        hipotenusa = calcular_hipotenusa(cateto1, cateto2)
        print("La longitud de la hipotenusa es:", hipotenusa)

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
