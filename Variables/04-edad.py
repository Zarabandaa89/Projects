def edad():
    try: 
        Año_actual = int(input("Digite el año actual: "))
        
        Año_nacimiento = int(input("Digite su año de nacimiento: "))
        
        calculo_edad = Año_actual - Año_nacimiento
        
        print("Su edad actual es: ", calculo_edad)
        
    except ValueError:
        print("ERROR: digite valores validos para calcuar su edad")
        
if __name__ == "__main__":
    edad()