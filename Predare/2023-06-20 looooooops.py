
varsta = 0
while varsta <= 50:
    if varsta % 4 == 0:
        print(varsta)
    varsta += 1
#While loops executa un bloc de instructiuni atat timp cat se respecta o conditie

#Atentie la infinite loop
numar = 12
while True: #while conditie - codul se executa atat timp cat conditia este True
    print(numar)
    numar += 1
    if numar > 1000:
        break #break iese din loop/bucla
    #putem iesi din bucla fie din conditia de la while, fie dintr-o conditie din interiorul buclei
    print("Ok")

numar = 5
while numar <= 102:
    numar += 1
    if numar % 10 == 0:
        continue #merge la inceputul buclei, si ignora codul de mai departe
    print(numar)

numar = 5
while numar <= 102:
    numar += 1
    if numar % 10 == 0:
        pass #pass nu face nimic, folosit ca umplutura work-in-progress, cod la care vei reveni
    print(numar)

#for
varste = [2, 3, 78, 49, 15, 67]
# print(varste[0])
# print(varste[1])
# print(varste[2])

for vr in varste:
    print(vr)
    #for merge pe fiecare element din lista
    #while este nedeterminat, for este determinat de lista/iteratorul pe care il accesam

nume = "Alexandru"
# print(nume[0])
for litera in nume:
    print(litera)

numar = 3456789
for cifra in numar:
    print(cifra)

#Obiecte iterabile in python- sunt acele care au mai multe elemente individuale
#Si putem itera asupra lor. A itera - extragem elementele unul cate unu cu for loop

tupx = ("Ana", "Ion", "Elena")
for el in tupx:
    print(el)

numar_rational = 345.98
for cifra in numar_rational:
    print(cifra)

dictx = {"nume":"ion",
         "varsta":12,
         "adresa":{"str":"ABC", "nr":12}}

for cheie in dictx.keys():
    print(cheie)

for valoare in dictx.values():
    print(valoare)
    print("_________")

for cheia, valoare in dictx.items():
    #items ne ofera posibilitatea sa accesam cheile si valorile simultan
    print(f"Cheia este = {cheia}, Valoarea = {valoare}")

print(dictx.items())

"""
Obiecte iterabile in python sunt de urmatoarele tipuri:
List
Tuple
String
Dictionare
Set
Generatoare - intermediate

Interable - un obiect in python poate fi parcurs pe fiecare element in parte cu for loop.
Interation - procesul prin care accesam fiecare element
"""

varste = [2, 3, 78, 49, 15, 67, 65, 99, 40]
for nr in varste:
    if nr % 5 != 0: #daca restul impartirii la 5 nu este 0, adica nu e divizibil cu 5
        continue #daca conditia e indeplinita, merge la urmatorul element fara a executa codul de jos
    print(nr)

for nr in varste:
    if nr % 5 == 0:
        break #iese din bucla imediat ce ajunge la un element divizibil cu 5, adica restul impartirii la 5 =0
    print(nr)

for nr in varste:
    if nr % 5 == 0:
        pass #pass-ul e ignorat
    print(nr)

cuv = "Alexandrul cel mare"
#print toate literele care nu sunt vocale din cuvant
for litera in cuv:
    if litera.lower() in 'aeiou':
        continue
    print(litera, end = ", ")

#print toate literele care nu-s vocale, fara duplicate
cuv = "Alexandrul cel mare"
lista_litere_non_vocale = []
for litera in cuv:
    if litera.lower() in 'aeiou ':
        continue
    lista_litere_non_vocale.append(litera)

print(set(lista_litere_non_vocale))

lisx = [1,2,3,1,1,2,3,2,1]
print(lisx)
print(set(lisx))

listx = [1,2,3,4,5,6,7]
for el in listx:
    if el % 3 == 0:
        print(f"{el} este divizibil cu 3")
        continue
    print(f"{el} nu este divizibil cu 3")

#printeaza de la 1 la 20 din 2 in 2
# for el in [1,3,5..] #manual! NONO

nr = 1
while nr <= 20:
    print(nr)
    nr += 2

for el in range(1, 200, 13): #range construieste ~o lista cu elemente de la start pana la end din step in step
    #range(start, end, step)
    print(el, end = ", ") #1, 14, 27, 40, 53, 66, 79, 92, 105
    #range(1, 200, 13) - de la 1 inclusiv la 200 exclusiv din 13 in 13

for el in range(1, 20): #step by default este 1, adica putem sa nu-l punem si va avea valoarea implicita 1
    print(el) #va printa de la 1 inclusiv pana la 20 exclusiv, adica pana la 19 inclusiv

for el in range(200, 1, -4): #de la 200 inclusiv pana la 1 exclusiv din 4 in 4 descrescator
    print(el, end=", ") #200, 196, 192, 188, 184

ceva_range = range(1,10, 2)
print(ceva_range) #range(1,10,2), un obiect cu logica de range.
#ca sa extragem lista din obiectul range, folosim functia list
print(list(ceva_range))

nume = ["Ion", "Andreea", "Ion", "Ana", "Ana"]
for n in nume:
    indexul_n = nume.index(n) #PRIMUL index unde se gaseste valoare
    print(f"Elementul cu indexul {indexul_n} are valoarea = {n}")
    #Modul incorect de a accesa indexul

for index, n in enumerate(nume):
    print(f"Elementul cu indexul {index} are valoarea = {n}")

print(enumerate(nume))# obiect logic (generator) care imi stocheaza logica de accesare a indexului si valorii
print(list(enumerate(nume))) #[(0, 'Ion'), (1, 'Andreea'), (2, 'Ion'), (3, 'Ana'), (4, 'Ana')]

lista_index = [(0, 'Ion'), (1, 'Andreea'), (2, 'Ion'), (3, 'Ana'), (4, 'Ana')]
for el_1, el_2 in lista_index:
    print(f"el_1 = {el_1}, el_2 = {el_2}")

studenti = [("Ion", 46, "Mecanic Auto"),
            ("Elena", 48, "Miner")]

for nume, varsta, profesie in studenti:
    print(f"{nume} are {varsta} si ocupatia de {profesie}")

#Data viitoare
#exemple impreuna- loops, control flow - b,c,p, comprehension, ex indiv cu ajutor.

#liste [ : listax = [1,2,3]
#index [ : element = listax[1] -al doilea element din listax
#elemente din dictionar [: in dictionarul dx = {"nume":"Andrei"}, putem accesa valoarea cheii cu valoare = dx["nume"]
#dictionarul se defineste prin { si cheie:valoare.
#set { : sx = {1,2,3}
#tuple ( : tx = (1,2,3)
#functii (: print(123), range(1,20), string.lower()...
sx = "ceva text"
ix = 123456
fx = 1234.243
bx = True

