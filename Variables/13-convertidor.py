try:
    distancia_metros = float(input("Ingrese la distancia en metros: "))
    opcion = input("Ingrese la unidad a la que desea convertir (km, cm o mm): ")

    if opcion == "km":
        distancia_convertida = distancia_metros / 1000
        print("La distancia equivale a", distancia_convertida, "kilómetros.")
        
    elif opcion == "cm":
        distancia_convertida = distancia_metros * 100
        print("La distancia equivale a", distancia_convertida, "centímetros.")
        
    elif opcion == "mm":
        distancia_convertida = distancia_metros * 1000
        print("La distancia equivale a", distancia_convertida, "milímetros.")
        
    else:
        print("Error: Opción inválida. Debe elegir entre km, cm o mm.")

except ValueError:
    print("Error: Ingrese un valor numérico válido.")
