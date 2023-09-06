#iteratori

lista = [1,3,4]
for element in lista:
    print(element)

#prin metoda iter si apoi next putem sa extragem elementele doar atunci cand avem nevoie de urmatorul
lista_iter = iter(lista)
print(next(lista_iter))

def suma_1_to_x(pana_la):
    suma = 0
    for nr in range(1, pana_la + 1):
        suma += nr
        yield suma

suma_10 = suma_1_to_x(10)
print(suma_10)

#pentru a extrage componentele dintr-un generator, putem itera pe el
for el in suma_10:
    print(el)

#Exemplu de functie care returneaza toata lista, VS un generator
#Verificam spatiul in memorie
from time import perf_counter, sleep
from random import randint, choices
import string
def lista_elemente_random_lista(size):
    lista = [] #list()
    for i in range(size):
        lungimea_cuv = randint(3,12)
        cuvant_random = "".join(choices(string.ascii_letters, k=lungimea_cuv))
        lista.append(cuvant_random)
    return lista

def lista_elemente_random_lista_generator(size):
    for i in range(size):
        lungimea_cuv = randint(3,12)
        cuvant_random = "".join(choices(string.ascii_letters, k=lungimea_cuv))
        yield cuvant_random
        #yield este specific generatoarelor, returneaza un singur element doar cand avem nevoie de el

un_milion_lista = lista_elemente_random_lista(10**7)
un_milion_gener = lista_elemente_random_lista_generator(10**7)

print(un_milion_lista[:3])
nr_el = 0
for el in un_milion_gener:
    print(el)
    nr_el += 1
    if nr_el >= 3:
        break

from sys import getsizeof
#getsizeof - cat spatiu ocupa in memorie un obiect in bytes
print(f"un_milion_lista ocupa {getsizeof(un_milion_lista)} bytes")
print(f"un_milion_gener ocupa {getsizeof(un_milion_gener)} bytes")
print(f"Diferenta de memorie lista/generator este de {getsizeof(un_milion_lista) // getsizeof(un_milion_gener) } ori")