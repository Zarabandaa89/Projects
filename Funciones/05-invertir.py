def invertir(cadena):
    
    resultado = ""
    for i in range(len(cadena) -1, -1, -1):
        resultado += cadena[i]
    return resultado


cadena = "1234abcd"

resultado = invertir(cadena)

print("lista al reves:(123abcd):",resultado)
