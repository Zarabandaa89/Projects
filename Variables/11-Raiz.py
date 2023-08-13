try:
    numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
    
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        raiz_cuadrada = numero ** 0.5
        print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)

except ValueError:
    print("Error: Ingrese un número válido.")
