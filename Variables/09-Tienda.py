def ValorTotal(Unitario, Cantidad):
    total = Unitario * Cantidad
    iva = total * 0.16
    total_IVA = total + iva
    return total_IVA

def main():
    try:
        Unitario = float(input("Ingrese el valor unitario del producto: "))
        Cantidad = int(input("Ingrese la cantidad de productos comprados: "))

        if Unitario <= 0 or Cantidad <= 0:
            print("Error: El valor unitario y la cantidad deben ser mayores a cero.")
            return

        total_IVA = ValorTotal(Unitario, Cantidad)
        print("El total a pagar con IVA es:", total_IVA)

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
  