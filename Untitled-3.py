a = int(input("Introduceti a: "))
b = int(input("Introduceti b: "))
c = int(input("Introduceti c: "))
d = int(input("Introduceti d: "))

def fractionOperations():
    print(f'Suma este {((a*d) + (c*b)) / (b*d)}, iar produsul este {(a*c) / (b*d)}')

fractionOperations()