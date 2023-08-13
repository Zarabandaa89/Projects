def porcentajes(numero):
    treinta_por_ciento = numero * 0.30
    sesenta_por_ciento = numero * 0.60
    noventa_por_ciento = numero * 0.90
    return treinta_por_ciento, sesenta_por_ciento, noventa_por_ciento

if __name__ == "__main__":
    
    try:
        numero_ingresado = float(input("Ingresa un número para calcular los porcentajes: "))
        
        resultado_30, resultado_60, resultado_90 = porcentajes(numero_ingresado)
        
        print(f"El 30% de {numero_ingresado} es: {resultado_30}")
        
        print(f"El 60% de {numero_ingresado} es: {resultado_60}")
        
        print(f"El 90% de {numero_ingresado} es: {resultado_90}")
        
        
    except ValueError:
        print("Error: Ingresa un número válido.")
