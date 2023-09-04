#args, kwargs
def suma_1(a,b):
    return a+b

print(suma_1(2,3,6))

def suma_2(*args):
    #*args inseamna un numar nedeterminat de argumente
    suma = 0
    for a in args:
        suma += int(a)
    return suma

print(suma_2(2,3,6, 32,32,32))

def catalog(**kwargs):
    #**kwargs - keyword arguments, un fel de dictionar
    #la fel- un numar nedeterminat de elemente
    for key, value in kwargs.items():
        print(f"{key} are varsta de {value} ani")

catalog(Ion=20,
        Ana=22,
        Elisa=21)

dictx = {"cheie_1":1,
         "cheie_2":True,
         "adresa":{"strada":"Unirii",
                   "nr": 23}}

#pentru a accesa o valoare a dictionarului, o facem prin accesarea cheii
print(dictx["cheie_1"])
print(dictx["adresa"]["nr"])


import json

print(dictx)
dictx_frumos = json.dumps(dictx, indent=2)
print(dictx_frumos)

folder = "B:/pyx/SDA/SDA_52"
#operatiunea de scriere a dictionarului ca string intr-un fisier
#folderul poate fi oriunde la tine pe calculator
with open(f"{folder}/exemplu_json.txt", "w") as f:
    json.dump(dictx, f)

#operatiunea de citire a unui string dictionar-valid
with open(f"{folder}/exemplu_json.txt", "r") as f:
    datele_citite = json.load(f)

print(datele_citite)
print(type(datele_citite))

import os
print(os.getcwd())
#printeaza current working directory, adica locatia unde se executa codul
"""
B:/pyx/SDA/SDA_52/exemplu_json.txt - Full Path
SDA_52/exemplu_json.txt -relative path
"""

#list comprehension
#Creez o lista cu cuburile de la a la b

lista_cuburi = []
for x in range(2, 10):
    lista_cuburi.append(x**3)
print(lista_cuburi)

lista_cuburi_v2 = [x**3 for x in range(2,10)]
#in varianta 2 am folosit list comprehension
print(lista_cuburi_v2)

#Creez o lista cu numerele divizibile cu 7 intr-un range
lista_7 = [x for x in range(2, 100) if x % 7 == 0]
print(lista_7)

#sau
lista_7 = []
for x in range(2,100):
    if x % 7 == 0:
        lista_7.append(x)

#cream o lista cu elementele comune din alte 2 liste
lista_1 = [2,3,4,5,6,7]
lista_2 = [1,2,7,8,9]
comune = [x for x in lista_1 if x in lista_2]
#pentru fiecare element din lista_1 verific daca exista in lista 2

#Extargem toate literele majuscule dintr-un string
sx = "Afara ploua, dar Umbrela mea e la Vasile"
majuscule = [x for x in sx if x.isupper()]
print(majuscule)

#Dict comprehension
#Cream un dictionar cu cheile numere de la a la b, iar valorile patratele sale pentru nr pare
numere_dict = {x: x**2 for x in range(2,10) if x % 2 == 0}
print(numere_dict) #{2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#creez un dictionar care imi scrie lungimea fiecarui cuvant dintr-o propozitie
sx = "Afara ploua, dar Umbrela mea e la Vasile"
print(sx.split(" "))
dict_lungime_cuv = {x : len(x) for x in sx.split(" ")}
print(dict_lungime_cuv)

matrice = [[1,2,3], [4,5,6], [11,22,33]]
#rez = [1,2,3,4,5,6,11,22,33]
flattened = [x for linie in matrice for x in linie]
print(flattened)

#break, continue, pass

for x in range(2,10):
    if x == 5:
        continue #cand ajunge la continue, sare la urmatoarea valoare, fara a executa codul ramas
    print(x)

for x in range(2,10):
    if x == 5:
       break #atunci cand ajunge la break, iese brusc din bucla
    print(x)

for x in range(2,10):
    if x == 5:
       pass #pass nu are nici o actiune/influenta
    #pass se foloseste pentru a reveni la cod mai tarziu, nu face nimic
    print(x)


#functii lambda
def suma_patratelor_1(a,b):
    return a**2 + b*b

suma_patratelor_2 = lambda a, b: a**2 + b*b
print(suma_patratelor_1(3,4))
print(suma_patratelor_2(3,4))

divizibil_23_check = lambda nr: nr % 23 == 0
print(divizibil_23_check(49))

ultimele_x_chars = lambda strx, ultimele_x : strx[(len(strx) - ultimele_x):]
str_ex = "Afara ploua, dar Umbrela mea e la Vasile"
print(ultimele_x_chars(str_ex, 5))

lista = [1,2,"abc", "salut", 3]
suma_numere_lista = lambda listx : sum([x for x in listx if isinstance(x, int)])
print(suma_numere_lista(lista))



