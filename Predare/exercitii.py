#FOR
# Afișează toate numerele întregi de la 0 la 10
for numar in range(0,11):
    print(numar)

# Afișează toate numerele pare de la 1 la 20.
for nr in range(1, 21):
    if nr % 2 == 0:
        print(nr, end=", ")

# Afișează toate numerele impare de la 1 la 20.
for nr in range(1, 21):
    if nr % 2 != 0: #SAU if nr % 2 == 1:
        print(nr, end=", ")

#Calculează suma tuturor numerelor de la 1 la 100
#V1
suma = 0
for nr in range(1,101):
    suma += nr

print(suma)

#V2
suma = sum(range(1,101))
print(suma)

#V3
suma = (100*101)/2
print(suma)

#Calculează suma tuturor numerelor pare de la 1 la 100
suma = 0
for nr in range(1,101):
    if nr %2 == 0:
        suma += nr
print(suma)

#Afișează toate literele unui șir de caractere.
sir = 'Salut ce mai faci astazi'
lit = set(sir) #setul fiind elemente unice, imi extrage toate elemenetele unice din sir
print(lit) #set returneaza o colectie neordonata/ haotica
listx = list(lit)
listx.sort()
print(listx)
# Afișează toate literele unui șir de caractere, cu exceptia literelor: f,g,a,w,t,r,y,c

list_litere = []
for lit in sir:
    if lit not in "f,g,a,w,t,r,y,c ":
        #print(lit, end=", ")
        list_litere.append(lit.lower())

print(set(list_litere))

# Afișează toate valorile dintr-o listă.
lisx = [1, 2.3, "Hello", {2,3,4}, [44,55,66]]
for el in lisx:
    print(el)

# Afișează toate cheile și valorile dintr-un dicționar.
dictionarul_meu = {"k1":12,
                "k2":19.2,
                "k3":[4,5,6]}

for key, value in dictionarul_meu.items():
    print(f"Cheia {key} are valoarea {value}")

#Afișează produsul tuturor elementelor dintr-o listă de numere întregi.

numere_intregi = [1,45,23,2,199]
produs = 1
for nr in  numere_intregi:
    produs *= nr
print(f"Rezultatul = {produs}")

#WHILE
# Afișează toate numerele întregi de la 0 la 10.
#V1
nri = 0
while True:
    print(nri)
    nri += 1
    if nri > 10:
        break

#V2
nri = 0
while nri <= 10:
    print(nri)
    nri += 1

#Afișează toate numerele pare de la 1 la 20.
nri = 0
while nri <= 20:
    if nri % 2 == 0:
        print(nri)
    nri += 1

#Calculează suma numerelor de la 1 la 100.
suma = 0
nr = 1
while nr <= 100:
    suma += nr
    nr += 1
print(suma)

#Calculează suma numerelor pare de la 1 la 100
suma = 0
nr = 1
while nr <= 100:
    if nr % 2 == 0:
        suma += nr
    nr += 1
print(suma)

#. Afișează primele 10 numere al caror predecesor e divizibil cu 5 si succesor divizibil cu 13

nr_max = 10 #numarul de numere ce il va printa, adica vom avea doar 10 numere printate
nr = 0
while True:
    if ((nr - 1) % 5 == 0) and ((nr + 1) % 13 == 0):
        print(nr)
        nr_max -= 1
    nr += 1
    if nr_max ==0:
        break

# Folosind o variabilă index, parcurge toate literele unui string și afișează-le.
strx = "Salutare ce mai faci"
ix = 0
while ix < len(strx): #daca lungimea unui iterabil (str, list ...) este de 14 elemente, ultimul index va fi 13
    print(strx[ix])
    ix += 1

print(len('A B C')) #5, pentru ca " " este si el element

#Cerere de parolă: setează o parolă și folosește while pentru a cere utilizatorului să introducă parola,
# până când aceasta este ghicita corect.

parola_de_ghicit = "SDAhello"

while True:
    ghiceste_parola = input("Ce parola crezi ca este = ")
    if ghiceste_parola != parola_de_ghicit:
        print("Nu ai ghicit")
    else:
        print("Ai ghicit corect")
        break



