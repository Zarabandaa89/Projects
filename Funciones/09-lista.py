def lista1(lista):
    
    lista_unica = list(set(lista))
    return lista_unica

digitos = [14,27,14,27,14,54,54,14,27]


print("La lista DUPLICADA: [14,27,14,27,14,54,54,14,27]")

lista_sin_duplicados = lista1(digitos)

print("Lista sin duplicar: ",lista_sin_duplicados)