nume = ["Ion", "Vasile", "Elena", "Ana"]
#Creati o lista cu numele in CAPS

#V1
nume_CAPS = []
for n in nume:
    nume_CAPS.append(n.upper())
print(nume_CAPS)

#V2 - list comprehension, o solutie pe o singura linie
nume_CAPS = [n.upper() for n in nume]
print(nume_CAPS)

"""
Sintaxa list comprehension, fara conditii
lista = [element_procesat for element in alta_lista]
"""

nume = ["Ion", "Vasile", "Elena", "Ana", "Bo", "Jan", "Bob"]
#Creeaza o lista doar cu nume ce au lungimea de 3 caractere
#V1
nume_3 = []
for n in nume:
    if len(n) == 3:
        nume_3.append(n)
print(nume_3)

#V2 cu list comprehension
nume_3_v2 = [n for n in nume if len(n) == 3]
print(nume_3_v2)
"""
Sintaxa list comprehension, cu conditii
lista = [element_procesat for element in alta_lista if conditie]
"""
prenume = ["Ion", "Vasile", "Elena", "Ana", "Bo", "Jan", "Bob"]
#Adaugati acelasi nume de familie (ex: Ionescu) la fiecare prenume, pentru ca sunt din aceiasi familie
nume_prenume = [f"{n} Ionescu" for n in prenume]
print(nume_prenume)

#Ceati o lista cu patratele fiecarui numar de la 5 la 15 inclusiv
#V1 clasica
lista_patrate = []
for n in range(5, 16):
    lista_patrate.append(n**2)
print(lista_patrate)

#V2 comprehension
lista_patrate_v2 = [n**2 for n in range(5,16)]
#list comprehension este o solutie eleganta pentru implementari simple
#NU se recomanda list comprehension pentru solutii complexe
print(lista_patrate_v2)

prenume = ["Ion", "Vasile", "Elena", "Ana", "Bo", "Jan", "Bob"]
#Creati o alta lista cu numele ce nu contin litera b sau j
prenume_filtrat = [n for n in prenume if "b" not in n.lower() and "j" not in n.lower()] #jan, bob
#O lungime aprox maxim acceptata pentru ca list compr. sa fie considerata solutie eleganta
print(prenume_filtrat)

#Dict comprehension
#Construiesc un dictionar cu numarul si patratul lui, de la 20 la 28
#V1
dx = dict()
for n in range(20, 29):
    dx[n] = n**2
print(dx)

#V2
dx_v2 = {n: n**2 for n in range(20, 29)}
print(dx_v2)


prenume = ["Ion", "Vasile", "Elena", "Ana", "Bo", "Jan", "Bob"]
#Creati un dictionar cu prenumele: lungimea lui
#V1
dx = dict()

# SAU dx = {}
# lisx = [] - 2 metode de initializare a unei liste goale
# lisx = list()

for n in prenume:
    dx[n] = len(n)
print(dx)

#V2 dict comprehension
dx_v2 = {n : len(n) for n in prenume}
print(dx_v2)

#tuple comprehension
#Creez un tuple cu cuburile numerelor de la 3 la 9
lisx = [x**3 for x in range(3,10)]
tupx = (x**3 for x in range(3,10)) #<generator object <genexpr> at 0x0000014EAC8C35E0>
#Adica a stocat logica elementelor, nu si elementele propriu-zise
tupx = tuple(x**3 for x in range(3,10)) #Am extras toate elementele din generator
print("list = ", lisx)
print("tuple = ", tupx)

#Set comprehension
#Genereaza un set cu toate cuvintele unice din acest text, case-insensitive
strx = "Afara ploua, dar cine a mai fost afara"
print(strx.split()) #['Afara', 'ploua,', 'dar', 'cine', 'a', 'mai', 'fost', 'afara']
setx = {word.lower() for word in strx.split()}
print(setx) #{'ploua,', 'afara', 'mai', 'cine', 'dar', 'a', 'fost'}
#lower transforma in lowercase

#setx = {word for word in strx.split()} #{'ploua,', 'Afara', 'mai', 'afara', 'cine', 'dar', 'a', 'fost'}
