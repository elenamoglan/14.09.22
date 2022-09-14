def creare_lista():
    n = int(input('Numarul de elemente: '))
    lista_locala = []
    for i in range(n):
        element = eval(input(f'Elementul {i} este: '))
        if isinstance(element, float) == True:
            lista_locala.append(element)
    return lista_locala

print(creare_lista())