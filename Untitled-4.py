def creare_lista():
    n = int(input('Numarul de elemente: '))
    lista_locala = []
    for i in range(n):
        element = input(f'Elementul {i} este: ')
        if isinstance(element, element) == True:
            lista_locala.append(element)
    return lista_locala

print(creare_lista())