def mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0
    
    for caracter in cadena:
        if caracter.isupper():
            mayusculas += 1
            
        elif caracter.islower():
            minusculas += 1
    return mayusculas, minusculas

frase = str(input("Ingrese una frase ya sea que contenga minusculas o mayusculas: "))

mayusculas, minusculas = mayusculas_minusculas(frase)

print(f"Número de letras mayúsculas: {mayusculas}")

print(f"Número de letras minúsculas: {minusculas}")
