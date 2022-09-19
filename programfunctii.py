nr1 = int(input('Introduceti primul numar intreg: '))
nr2 = int(input('Introduceti al doilea numar intreg: '))


def suma(nr1, nr2):
    return nr1 + nr2


def produs(nr1, nr2):
    return nr1 * nr2


def medie(nr1, nr2):
    return (nr1 + nr2) / 2


def divizori(x):
    divisors = []

    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            divisors.append(i)

    return divisors


def divizoriComuni(nr1, nr2):
    divisors = divizori(nr1)
    comuni = []

    for i in range(len(divisors)):
        if nr2 % divisors[i] == 0:
            comuni.append(divisors[i])

    return comuni


def maxDivizor():
    divisors = divizoriComuni(nr1, nr2)
    maxdiv = 0

    for i in range(len(divisors)):
        if divisors[i] > maxdiv:
            maxdiv = divisors[i]

    return maxdiv


def multipliComuni(nr1, nr2):
    multiplesnr1 = []
    multiplesnr2 = []
    comuni = []

    for i in range(1, max(nr1, nr2)):
        multiplesnr1.append(nr1*i)
        multiplesnr2.append(nr2*i)

    for element in multiplesnr1:
        if element in multiplesnr2:
            comuni.append(element)

    return comuni[0:5]


def minMultiple():
    multiples = multipliComuni(nr1, nr2)
    multiples.sort()

    return multiples[0]


def minim(nr1, nr2):
    if (nr1 < nr2):
        return nr1
    else:
        return nr2


def maxim(nr1, nr2):
    if (nr1 > nr2):
        return nr1
    else:
        return nr2


def sumaScrisa(nr1, nr2):
    return f'{nr1} + {nr2} = {nr1 + nr2}'


def produscris(nr1, nr2):
    return f'{nr1} * {nr2} = {nr1 * nr2}'


def cifreComune(nr1, nr2):
    cifre = []

    for i in str(nr1):
        for j in str(nr2):
            if i == j:
                cifre.append(i)

    return cifre


def cifreDiferite(nr1, nr2):
    cifre = []

    for i in str(nr1):
        if i not in str(nr2):
            cifre.append(i)

    return cifre


def prietene(nr1, nr2):
    if len(divizori(nr1)) == len(divizori(nr2)):
        return "PRIETENE"
    else:
        return "Numerele nu sunt prietene"


print(f'{suma(nr1, nr2)}\n{produs(nr1, nr2)}\n{medie(nr1, nr2)}\n{maxDivizor()}\n{minMultiple()}\n{minim(nr1, nr2)}\n{maxim(nr1, nr2)}\n{sumaScrisa(nr1, nr2)}\n{produscris(nr1, nr2)}\n{divizoriComuni(nr1, nr2)}\n{multipliComuni(nr1, nr2)}\n{cifreComune(nr1, nr2)}\n{cifreDiferite(nr1, nr2)}\n{prietene(nr1, nr2)}')
