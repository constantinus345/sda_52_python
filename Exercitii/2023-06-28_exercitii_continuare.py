# 20. Creati o functie care verifica daca un numar e prim
from math import sqrt

def este_prim(nr):
    if nr < 2:
        return False

    #trebuie sa verific de la 2 pana la radical(n) +1
    for i in range(2, int(sqrt(nr)) + 1):
        if nr % i == 0:
            return False

    return True

print(este_prim(187428364923))

print(7/0)


