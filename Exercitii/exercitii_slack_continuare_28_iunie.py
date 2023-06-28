#Calculez (a*b*c*...) + (a+b+c+...)
#Despartim problema in doua sub-capitole

def inmultire_num(*args):
    produs = 1
    for arg in args:
        if isinstance(arg, int):
            produs *= arg
    return produs

def adunare_num(*args):
    suma = 0
    for arg in args:
        if isinstance(arg, int):
            suma += arg
    # print("Ceva aici")
    return suma

