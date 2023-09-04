a=45+89 #nu este estetic
a = 45 + 89 #recomandat estetic

#pentru denumirea functiilor folosim snake_case
def adunare_numere(a,b):
    return a + b

#pentru denumirea claselor, folosim CamelCase
class AdunareNumere:
    pass

#https://peps.python.org/pep-0008/ -PEP8 sugestiile de stil in python oficiale
#https://google.github.io/styleguide/pyguide.html

l_1 = [1,2,3]
l_2 = l_1 #shallow copy of an object, am creat 2 etichete pentru acelasi obiect in memorie
print(l_1 == l_2)
l_1.append(23)
print(l_1 == l_2)
print(l_1 is l_2) #True, adica aceste 2 variabile/etichete ocupa acelasi spatiu in memorie
print(id(l_1)) #accesez id-ul obiectului in memorie
print(id(l_2)) #l_1 si l_2 au acelasi id

from copy import deepcopy
l_3 = deepcopy(l_1)
print(l_1 == l_3)
print(l_1 is l_3) #False, doua obiecte diferite
print(id(l_1))
print(id(l_3))

a: int = 1
a: str = 'unu' #type hints sunt mai mult info pentru developeri, nu si restrictii in executarea codului
print(a)

def multiplicare_numar(numar: int, lista: list[float]) -> float:

    rez = 0
    for el in lista:
        rez += numar * el

    return rez

print(multiplicare_numar(2, [3.0, 4]))
print(type(3*3.0)) #int * float = float

exemplu_path =  "B:\nume_folder\SDA"
print(exemplu_path)

#Operatiuni cu fisiere
folder = r"B:\pyx\SDA" #raw string, nu interpreteaza caracterele precum \n

#Modul python de a scrie path (o adresa in memoria calculatorului) este cu /
folder = "B:/pyx/SDA"

#Creez un folder
import os
os.mkdir(f"{folder}/SDA_52")

text_de_scris = "Salut, ce mai faci?"
with open(f"{folder}/SDA_52/fisier_text_1.txt", "w") as fisier:
    fisier.write(text_de_scris)
    #"w"- write, cand scriu cu w, se sterge tot textul apoi se scrie in el


text_de_scris = "Cum a fost azi pentru tine"
with open(f"{folder}/SDA_52/fisier_text_1.txt", "a") as fisier:
    fisier.write(text_de_scris) #"a"-append

text_de_scris = "\nHai sa mergem la plimbare"
with open(f"{folder}/SDA_52/fisier_text_1.txt", "a") as fisier:
    fisier.write(text_de_scris) #"a"-append

""" 
In operatiunea cu fisiere, putem avea mai multe tipuri de operatii:
"r"-read
"w"-write
"a"- append
"b" -bytes
"""
#Aici un alt mod
#de a scrie
#comentariu multi-line

a = 5
b = 6
c = 9
a, b, c = 5, 6, 9
print(b)

lis_1 = [1,2]
print(f"Lista {lis_1} are {len(lis_1)} elemente")
lis_1.append([4,5])
print(f"Lista {lis_1} are {len(lis_1)} elemente")
lis_1.extend([11,22,33])
print(f"Lista {lis_1} are {len(lis_1)} elemente")

sters = lis_1.pop(2) #sterge dupa index, si poate stoca valoarea stearsa intr-o variabila
print(f"Elementul sters este {sters} si noua lista = {lis_1}")
lis_1.remove(33) #sterge dupa valoare
print(lis_1)

lis_2 = [11, 22, 33, 22, 33]
lis_2.remove(33) #sterge doar un singur element din lista
#in caz ca nu mai avem elemente, eroare
#ValueError: list.remove(x): x not in list
print(lis_2)

lis_2 = [11, 22, 33, 22, 33]
del lis_2[2]
print(lis_2)

lis_2 = [11, 22, 33, 22, 33, 44,33]
lis_2 = [x for x in lis_2 if x != 33]
print(lis_2) # O solutie prin care sterge toate elementele cu valoarea 33

def adauga_element(numar, lista = []):
    #Nu folositi argumente default listele
    lista.append(numar**2)
    return lista

print(adauga_element(3)) #rezultat asteptat = [9], printat de fapt = [9]
print(adauga_element(4)) #rezultat asteptat = [16], printat de fapt = [9, 16]

def adauga_element_v2(numar, lista = None):
    #in loc sa declar valoarea default lista = []
    if not lista: #in cazul asta not None = True
        lista = []
    lista.append(numar**2)
    return lista

print(adauga_element_v2(3)) #rezultat asteptat = [9], printat de fapt = [9]
print(adauga_element_v2(4)) #rezultat asteptat = [16], printat de fapt = [16]




