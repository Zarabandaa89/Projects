def calcular_horas_minutos(tiempo_segundos):
    horas = tiempo_segundos // 3600
    minutos = (tiempo_segundos % 3600) // 60
    return horas, minutos

def main():
    try:
        tiempo_segundos = int(input("Ingrese el tiempo en segundos: "))

        if tiempo_segundos < 0:
            print("Error: El tiempo no puede ser negativo.")
            return

        horas, minutos = calcular_horas_minutos(tiempo_segundos)

        print(f"El tiempo ingresado equivale a: {horas} horas y {minutos} minutos.")

    except ValueError:
        print("Error: Ingrese un valor numérico entero válido.")

if __name__ == "__main__":
    main()
