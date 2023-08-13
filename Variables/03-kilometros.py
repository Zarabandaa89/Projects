def kilometros():
    try:
        velocidad_kmh = float(input("Ingresa la velocidad en kilómetros por hora (Km/h): "))
        
        tiempo_horas = float(input("Ingresa el tiempo en horas: "))

        distancia_km = velocidad_kmh * tiempo_horas

        print(f"La distancia recorrida es de {distancia_km:.2f} kilómetros.")
        
    except ValueError:
        print("Error: Ingresa valores numéricos válidos para la velocidad y el tiempo.")

if __name__ == "__main__":
    kilometros()

    