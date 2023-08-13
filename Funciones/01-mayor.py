def numero_mayor():
    a = int(input("Ingrese el valor 1: "))
    b = int(input("Ingrese el valor 2: "))
    c = int(input("Ingrese el valor 3: "))
    
    
    if a > b and c : 
      print("El valor 1 es mayor")
    elif b > a and c :
        print("El valor 2 es mayor")
    elif c > a and b :
        print("El valor 3 es mayor")
    else:
        print("Digite valores validos")
    
if __name__ == "__main__":
    numero_mayor()