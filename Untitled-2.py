m = int(input("Introduceti m: "))
n = int(input("Introduceti n: "))

def factorial(x):
    if (x != 1):
        return x * factorial(x - 1)
    else:
        return 1

def combinedFactorial(m, n):
    return factorial(n) / factorial(m) * factorial(n - m)

print(combinedFactorial(m,n))