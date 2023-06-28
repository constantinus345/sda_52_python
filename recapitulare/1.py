a = 7
#int
print(type(a))
b= 7.3 #float
c = "string text" #str
d = True #bool

e = "7"
f = int(e)
print(f, type(f))

#Vericam tipulde date
#v1
print(type(a) is str)
#v2
print(isinstance(a, str))
#!
print(isinstance(True, int)) #print(isinstance(True, int)) echivalent cu print(isinstance(1, int))

listx = ["b", 1, False, [1,2,3]]
tuplex = ("b", 1, False, [1,2,3])
listx[1] = "Altceva"
print(listx)
tuplex[1] = "Altceva"
print(tuplex) #Nu putem schimba elementele tuple-ului

setx = {2,3,45,66}
#set e tip de date unice, ne-ordonate (nu le putem accesa dupa index)
print(setx[2]) #TypeError: 'set' object is not subscriptable

lis_2 = [1, 2,"   3",2,  3,2,45]
lis_2_unice = list(set(lis_2))
print(lis_2_unice)

dictx = {"cheie_1": 12,"Andrei":25,
         "Ionel":[23,23],
         "adresa":{"strada":"Fericirii", "nr":12}}

#accesarea datelor
#prin indexare
listx = ["b", 1, False, [1,2,3]]
print(listx[0])
tupx = tuple(["b", 1, False, [1,2,3]])
print(tupx[0])

nume_strada_dictionar = dictx["adresa"]["strada"]
print(nume_strada_dictionar)
#json = dictionar

#prin iterare
for el in listx:
    print(el)

#enumerate ne ofera posibilitatea sa accesam index si valoare in acelasi timp
for indexul, el in enumerate(listx):
    print(f"Elementul cu indexul {indexul} are valoarea {el}")

print(list(enumerate(listx))) #[(0, 'b'), (1, 1), (2, False), (3, [1, 2, 3])]

#nu conteaza cun denumim variabilele la iterare, conteaza ordinea si logica lor
for al_catalea, cum_te_cheama in enumerate(listx):
    print(f"Elementul cu indexul {al_catalea} are valoarea {cum_te_cheama}")

lista_complexa = [["Ana", 23, "skiul"], ["Elena", 27, "șahul"], ["Ion", 29, "Video games"]]
for nume, varsta, hobby in lista_complexa:
    #list unpacking - functioneaza doar daca toate sub-listele au 3 valori nume, varsta, hobby
    print(f"nume = {nume}, varsta ={varsta}, hobby={hobby}")

listx = ["b", 1, False, [1,2,3]]
print(3 in listx) #False pentru ca [1,2,3] este un element unitar/nedivizibil in modul in care am apelat

dictx = {"cheie_1": 12,"Andrei":25,
         "Ionel":[23,23],
         "adresa":{"strada":"Fericirii", "nr":12}}

#iterearea pe dictionar
#doar cheile
for cheie in dictx.keys():
    print(cheie)
#doar pe valori
for val in dictx.values():
    print(val)
#iterare atat pe chei cat si pe valori
for cheie, val in dictx.items():
    print(f"Cheia {cheie} are valoarea {val}")

#pentru a itera pe dictionarul ce apartine de cheia adresa
for cheie, val in dictx["adresa"].items():
    print(f"Cheia {cheie} are valoarea {val}")

text_1 = "salut ion"
print(text_1.capitalize())
print(text_1.upper())
listx = ["b", 1, False, [1,2,3]]
print(len(listx))
print(len(text_1))
nr = 86778548
print(len(str(nr)))

#operatori aritmetici: +,-, *,/,
# // - impartire fara rest
# % - restul impartirii
# ** ridicare la putere
print(171 % 10)
print(171 // 10)
print(171 ** 10)

check_1 = 5 > 7 #la variabile putem sa le dam valori, dar si expresii de calculat
print(check_1)

#slicing
strx_1 = "Ana e eleva cuminte"
print(strx_1[5:9]) #elementul de la indexul 5 la indexul 8,
# adica al 6-lea element pana la al 9-lea numarat de la 1+
lis_1 = [1,2,3,4,5,6,7]
print(lis_1[2:5]) #de la indexul 2 pana la indexul 4, adica de la al 3-lea element la al 5-lea inclusiv
print(strx_1[::-1]) #[::-1] inverseaza un string/ lista

#range imi creeaza un fel de liste de la numar pana la numar, cu un step
#range(from, to, step)
for i in range(1, 101, 3): #de la 1 inclusiv pana la 101 exclusiv din 3 in 3
    print(i)

for i in range(1, 11):
    print(i) #de la 1 la 10 inclusiv, step este by default =1

for i in range(10,0,-1): #avand step negativ, inseamna descrescator
    print(i)



relative_path = 'Exercitii/alt_folder'
absolute_path = "C:\Users\const\PycharmProjects\SDA_52\Exercitii\alt_folder" #\- e caracter special
#Corect
absolute_path = r"C:\Users\const\PycharmProjects\SDA_52\Exercitii\alt_folder"
#r = raw string, anuleaza semnificatia \
#sau
absolute_path = "C:/Users/const/PycharmProjects/SDA_52/Exercitii/alt_folder"

#De ce nu merge \ in path-uri
exemplu_path = "C:\nicolae" #\n = newline
print(exemplu_path) #printeaza pe doua linii C: & icolae




