var_1 = "Text, adica str"
var_2 = 2
var_3 = True #bool
var_4 = 4.5
var_5 = 7 + 9j

#Colectii de date
#List

Nume = ["Ion", "Maria", "Elena", "Vasile"]
Date_diverse = [var_1, var_2, var_3, var_4, var_5]

#Cuvinte cheie
# ex: str, list, int, float ... - evitam in declararea variabilelor sau orice alte denumiri

listx = [] #lista goala
listx.append("hello")
listx.append(9.3)
print(listx)

#In liste putem pune diverse tipuri de date
#inlusiv liste in liste

listx = ['hello', 9.3, [True, False, 8, "ceva string", 3+4j], 15]
print(listx, type(listx))
#len - functie care ne zice lungimea listei
print(len(listx))
print(f"Lista are {len(listx)} elemente")

str_1 = "ceva text"
str_2 = 'ceva text'
str_3 = """
ceva text
pe mai 
multe 
randuri
"""

listx = ['hello',
         9.3,
         [True, False, 8, "ceva string", 3+4j],
         15]

primul = listx[0] #parantezele [] sunt folosite pentru a defini o lista
#dar si pentru a accesa elementele dupa index (ex- elementul al x-lea)
print(primul)

ultimul = listx[3] #indexul 3 = al 4-lea element, python incepe indexarea de la 0
#SAU
ultimul = listx[len(listx) - 1] #lungimea listei - 1 !!! Nu e forma recomandata
#SAU
ultimul = listx[-1] #forma recomandata pentru accesarea ultimului element
print(ultimul)

elem_penultimul = listx[-2]
print(elem_penultimul)

opt = listx[-2][2]
print(opt)

listx_2 = ['hello',
         9.3,
         [True, False, 8, [1,2,3,[9,11,23]], "ceva string", 3+4j],
         15]

unspe = listx_2[-2][3][3][1] #accesarea elemented "nested"/etajate
print(unspe)

nume = ["Ion", "Jan", "Ana", "Bob", "Felix", "Elena", "Ionel"]
primele_3 = nume[:3] #pana la indexul 3 EXCLUSIV, pana la al 4-lea element EXCLUSIV
# :3 = elementele de la index-ul 0, 1, 2 fara 3
# 3: = elementele de la index-ul 3, 4 ...
print(primele_3)
dupa_el_i3 = nume[3:] #de la indexul 3 (el al 4-lea) INCLUSIV 3
print(dupa_el_i3)

nume_1_4 = nume[1:5] #de la indexul 1 inclusiv pana la indexul 5 exclusiv 5
#1:5 = elementele cu index 1,2,3,4
print(nume_1_4)

nume = ["Ion", "Jan", "Ana", "Bob", "Felix", "Ana", "Elena", 'Ana', "Ionel"]
index_ana = nume.index("Ana") #indexul primei aparitii a valorii "Ana"
print(index_ana) #3

count_ana = nume.count("Ana") #numarul de aparitii a valorii "Ana" in lista
print(count_ana)

nume_2 = ["Ion", "Jan", "Ana", "Bob", "Felix", "Ana", ["Elena", 'Ana'], "Ionel"]
count_ana = nume_2.count("Ana") #detaliu- count numara doar la primul nivel!
print(count_ana) #2

nume = ["Ion", "Jan", "Ana", "Bob", "Felix", "Ana", "Elena", 'Ana', "Ionel", "Zinaida"]
nume.sort(reverse=True) #reserve este un argument al functiei, adica un fel de settings
print(nume)

ani = [23, 87, 12, 2, 76, 34]
ani.sort() #sortare ascendenta
print(ani)

ani.sort(reverse=True) #sortare descendenta
print(ani)

#[87, 76, 34, 23, 12, 2]
ani.pop(3) #pop sterge elementul la un anumit index
print(ani)

ani = [23, 87, 12, 2, 76, 34]
ani.remove(87) #remove sterge un element dupa valoarea sa
print(ani)

ani = [23, 87, 12, 87, 2, 76, 87, 34, 87]
ani.remove(87) #sterge doar prima valoare intalnita, nu pe toate deodata
print(ani)

#inversarea listei
nume = ["Ion", "Jan", "Ana", "Bob", "Felix", "Elena", "Ionel"]
#v1
print(nume[::-1])
#v2
nume = ["Ion", "Jan", "Ana", "Bob", "Felix", "Elena", "Ionel"]
nume.reverse()
print(nume)

#Tip de colectii - tuple
tupx = tuple()
tupx = (1, 2, "Hello", 4.5, False) #tuple se defineste cu ()
lisx = [1, 2, "Hello", 4.5, False] #lista se defineste cu []

lisx[1] = 99
print(lisx)

tupx[1] = 99
print(tupx) #tuple nu poate modifica elementele din el.
#tuple este "rigid"/de beton, pentru ca elementele odata populate nu mai pot fi schimbate

tupx = tupx + (22,33) #adaugam elemente in tuple
print(tupx)

#Dictionare
#tip de date ce contin chei si valori

contact = {"Nume": "Andrei",
           "emailuri": ["a@b.c", "aa@b.c", "y@c.h"],
           "nr_telefoane": ["+40-123", "+333456"],
           "adresa": {"nume_strada": "StCM", "nr": 55, "apt": 123}}

#un dictionar cu datele de contact (partiale) al u34nei persoane fictive

numele = contact["Nume"] #putem accesa valorile dictionarului dupa cheile sale, nu dupa index
#dictionarul nu este ordonat, adica nu putem sti care este elementul al x-lea
print(numele)

nr_strazii = contact["adresa"]["nr"]
print(nr_strazii)

del contact["emailuri"] #modalitate de stergere a cheilor cu valorile asociate
print(contact)

contact["cheie_noua"] = "valoare noua"
#am creat o cheie noua cu o valoare, ambele de tip string
print(contact)

contact[45] = 7.8 #am creat o cheie noua 45 de tip int cu valoarea 7.8 de tip float
print(contact)

print(contact.keys()) #accesam cheile dictionarului
print(contact.values()) #accesam valorile dictionarului

print(contact["Nume"])
print(contact["Prenume"]) #eroare, pentru ca nu am cheia "Prenume"
print(contact.get("Prenume")) #nu da eroare, ci doar valoarea None
#contact[] - pentru accesarea unei chei direct
#contact.get() - get este o metoda pentru procesarea dictionarului
#get da valoarea daca exista, iar daca nu exista returneaza doar None, fara a intra in eroare

print(3+5)
print(contact["Nume"])
print(contact.get("Prenume"))
print(7**2)
print(12/4)

#incearca instructiune, daca nu merge, fa altceva. Detalii la intermediate!
try:
    print(contact["Preumeeeee"])
except:
    print("Nu merge ce zici")