import math
print("Calculadora de áreas")

def cuadrado(lado):
    return lado*lado


def rectangulo(base,altura):
    return base * altura


def triangulo(base,altura):
    return (base * altura) / 2


def circulo(radio):
    return math.pi * radio**2


def rombo(diagonal_mayor,diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2


def trapecio(base_menor,base_mayor, altura):
    return((base_mayor+base_menor)* altura) / 2



def areas_figuras():
    
    print("1. Calcular área de cuadrado")
    print("2. Calcular área de rectángulo")
    print("3. Calcular área de triángulo")
    print("4. Calcular área de círculo")
    print("5. Calcular área de rombo")
    print("6. Calcular área de trapecio")
    
numero_calculo = int(input("Digite el numero de operacion a realizar: "))
 
if numero_calculo == 1:
   lado = float(input("Ingrese un lado del cuadrado:"))  
   print("El área del cuadrado es:", cuadrado)   
   
   
elif numero_calculo == 2:
    base=float(input("ingrese la longitud de una base"))
    altura=float(input("ingrese la altura de una parte del rectangulo"))
    print("El área del rectangulo es:", triangulo)   
    
elif numero_calculo == 3:
    base=float(input("ingrese la base de una parte trinagulo"))
    altura=float(input("ingrese la altura de una parte del trinagulo"))
    print("El área del triangulo es:", triangulo)   


elif numero_calculo == 4:
    radio=int(input("ingrese el radio del circulo: "))/10
    print("El área del circulo es: ", circulo)   


elif numero_calculo == 5:
    diagonal_mayor= float(input("ingrese la diagonal mayor del rombo"))
    diagonal_menor= float(input("ingrese la diagonal menor del rombo"))
    print("El área del rombo es:", rombo)   
  
elif numero_calculo == 6:
    base_menor= float(input("ingrese la base menor del trapecio"))
    base_mayor= float(input("ingrese la base mayor del trapecio"))
    print("El área del trapecio es:", trapecio)   
else:
    print ("Opcion no valida, intente nuevamente.")
    
if __name__ == "__main__":
         areas_figuras()