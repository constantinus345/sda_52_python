"""
Functii
Creează o funcție care primește un șir de caractere și returnează un dicționar care conține numărul de apariții ale fiecărui caracter din șir.
Creează o funcție care primește două liste și returnează o listă care conține elementele comune din cele două liste.
Creează o funcție care primește un numar și returnează o listă care conține toate perechile de numere din listă care au produsul egal cu un număr dat. Ex: pentru 12 avem [(1,12), (2,6), (3,4)]
Creează o funcție care primește un șir de caractere și returnează adevărat dacă șirul este format din caractere consecutive în ordine alfabetică și fals în caz contrar. De exemplu ars - True, arde - False.
Scrieti o functie care accepta ca parametri o lista de numere si un numar, iar rezultatul sa fie produsul fiecarui element din lista + nr. De exemplu pentru [2,3,4] si numarul 5 avem rezultatul = (2+5)(3+5)*(4+5)
Scrieti o functie care calculeaza factorialul unui numar
Scrieti o functie care calculeaza al n-lea numar in sirul lui Fibonacci. (Șirul lui Fibonacci este un șir de numere în care fiecare număr este suma celor două numere anterioare. Șirul începe cu 1 și 1, iar primele câteva numere din șir sunt: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...)
Scrieti o functie care calculeaza sin(x)+cos(x)
Scrieti o functie care verifica daca un numar e patrat perfect
Scrieti o functie care primeste o lista de nume si returneaza o alta lista cu nume unice ordonate alfabetic.
Scrieti o functie care verifica daca un string e palindrom (citit in ambele directii e acelasi, de exemplu ana e palindrom)

12. Scrieti un program care ghiceste un numar, zicand daca esti foarte departe,
departe sau foarte aproape de numarul de ghicit
13.
Creati un program care scrie cate secunde au mai ramas, gen countdown timer.
Hint: folositi from time import sleep
14.
Aveti 2 liste de nume: studenti inscrisi la curs si studenti prezenti azi.
Creati o functie care face prezenta.
(Nu dau instructiuni detaliate, va las sa fiti creativi)
15.
Creati o functie care valideaza un email (daca string-ul respectiv e valid pentru a fi considerat email)
16.
Aveti o un dictionar cu nume si varsta, fiecare are cate 4 elemente.
Creati un fisier care sa contina text cu numele si varsta fiecarei persoane, in modul urmator, exemplu:
Andrei are 20 ani, deci e nascut in 2003
Ion are...
...
...
17.
Aveti acest fisier cu notele a 3 elevi.
Creati alt fisier care scrie media aritmetica a fiecarui elev.
"""

numar_de_ghicit = 12
print("Am ales un numar de la 1 la 100. Acum ghiceste numarul!")

while True: #bucla tehnic infinita, trebuie sa iesim din ea manual la o anume conditie
    numar_ghicit = input("Introdu un numar 1-100 = ")
    try:
        numar_ghicit = int(numar_ghicit) #incearca sa converteasca in integer
    except:
        print("Mai da un numar valid")
        continue
        #cu ty-except ma asigur ca numarul e convertibil din str in int
    #numar_ghicit = int(numar_ghicit)
    diferenta = abs(numar_de_ghicit - numar_ghicit) #abs(x) = |x|, de ex |5| = |-5| = 5

    if diferenta > 20:
        print("Foarte departe! Mai incearca!")
    elif diferenta > 5: #intre 5 exclusiv si 20 inclusiv
        print("Departe si totusi aproape")
    elif diferenta > 0: #intre 0 exclusiv si 5 inclusiv
        print("Foarte foarte aproape")
    else: #adica diferenta = 0, a ghicit
        print(f"Bravo! Numarul era {numar_de_ghicit}")
        break

print("Uraaaa")

#15.Creati o functie care valideaza o adresa de email

email_ex = "andrei@sda.ro"
# print(email.split("@")) #['andrei', 'sda.ro'], desprate dupa un caracter
#daca scriu a, b = ["val_1", "val_2"], atunci fiecare variabila isi ia valoarea respectiva

#Reguli de validare, non-exhaustive (doar cateva reguli)
#are un singur @
#username are lungime >= 3
#domeniu (ex- sda) sa aiba lungime >= 2
#.something are lungime >= 2

def validare_email(email):
    if email.count("@") != 1:
        return False
    #functia returneaza o singura data, daca se returneaza la primul return, tot ce e mai departe e ignorat

    username, dupa_arond = email.split("@")
    domeniul, dupa_punct = dupa_arond.split(".")
    #fiindca email.split("@") are doua elemente, le putem desface "unpacking" in 2 variabile direct

    if len(username) < 3:
        return False
    if len(domeniul) <2:
        return False
    if len(dupa_punct)<2:
        return False

    if domeniul in ["gmail", "yahoo", "outlook"]: #excludem anumite domenii
        return False

    return True

email_exemplu = "ionel@sda.ro"
print(validare_email(email_exemplu))

text = "Ionel, Mia, Ioana"
lista_nume = text.split(", ")
print(lista_nume)# split a creat o lista cu 3 elemente, despartind dupa ", ", adica ['Ionel', 'Mia', 'Ioana']
nume_1, nume_2, nume_3 = lista_nume
#echivalent cu
nume_1 = lista_nume[0]
nume_2 = lista_nume[1]
nume_3 = lista_nume[2]
print(nume_1)

un_email = "andreea.ionescu@gmail.com"
print(un_email.split("@")) #['andreea.ionescu', 'gmail.com']

inainte_arond, dupa_arond = un_email.split("@")
inainte_p, dupa_p = dupa_arond.split(".")

print(f"inainte_arond = {inainte_arond}")
print(f"dupa_arond = {dupa_arond}")
print(f"inainte_p = {inainte_p}")
print(f"dupa_p = {dupa_p}")

text_localitati = "Iasi-Paris Sector 1 -Bucuresti-New York"
localitati_lista = text_localitati.split("-")
print(localitati_lista)

email_rau = "ion@gmail.com@guvern"
print(email_rau.split("@")) #['ion', 'gmail.com', 'guvern']

text_2 = "ion.ionel.ionescu"

## 16. Aveti o un dictionar cu nume si varsta, fiecare are cate 4 elemente.
# Creati un fisier care sa contina text cu numele si varsta fiecarei persoane, in modul urmator, exemplu:
# Andrei are 20 ani, deci e nascut in 2003
from datetime import datetime
anul = datetime.now().year #getting current year


folder = "B:/Dropbox/SDA/SDA_52"
def scrie_persoane(un_dictionar, path_file = f"{folder}/studentii_ex16.txt"):
    #path_file este o variabila default, pot sa o schimb

    with open(path_file, "w", encoding="utf-8") as f:
        #encoding="utf-8" - pentru a folosi o arie mai vasta de caractere, inclusiv diacritice RO
        for cheie, valoare in un_dictionar.items():
            f.write(f"{cheie} are {valoare} ani, deci e nascut(ă) în {anul - valoare}\n")

persoane = {"Andrei":20, "Ioana":23, "Vasile": 12, "Ana":24, "Jean":29, "Marc":35}
scrie_persoane(persoane)

# 17.
# Aveti acest fisier cu notele a 3 elevi.
# Creati alt fisier care scrie media aritmetica a fiecarui elev.
from statistics import mean
#am importat o functie care imi calucleaza media la o lista de numere intregi

def citire_linii_din_txt(folder, fisier_note = "fisier_cu_note.txt"):
    path_fisier_note = f"{folder}/{fisier_note}" #full path la fisier
    with open(path_fisier_note, "r") as f:
        linii = f.readlines() #imi returneaza toate liniile intr-o lista, o linie=element din lista
    return linii

def extragere_nume_note(folder):
    linii = citire_linii_din_txt(folder) #am apelat functia precedenta ca sa imi accesez liniile
    list_nume = []
    list_notele = [] #am initializat listele de nume si note, ca sa le umplu/append ulterior
    for l in linii:
        Numele = l.split(" ")[0]
        Notele =  l.replace(Numele, "")
        Notele = Notele.replace("\n", "") #am inlocuit "\n" cu nimic ""
        Notele = Notele.replace(" ","") #am inlocuit fiecare spatiu cu ""
        Notele = Notele.split(",") #am despartit notele dupa virgula
        list_nume.append(Numele)
        list_notele.append(Notele)
    # print(list_nume)
    # print(list_notele)
    return {"names": list_nume, "grades": list_notele} #returnat un dictionar cu numele si notele

def functie_convertire_lista_str_int(lista_de_convertit):
    #v1 forma lunga
    # lista_convertita = []
    # for el in lista_de_convertit:
    #     lista_convertita.append(int(el))
    #return lista_convertita
    #SAU
    #["7", "8"] se transforma in [7, 8]
    return [int(el) for el in lista_de_convertit]

def returneaza_text_cu_mediile(lista_nume, list_notele):
    text_de_creat = ""
    for index, el in enumerate(lista_nume):
        #pentru ca am lista de strings la medie, adica ['4', '10', '9', '4']
        #trebuie sa convertesc valorile in int
        list_notele_int = functie_convertire_lista_str_int(list_notele[index])
        #codul de mai sus converteste fiecare element din list_notele in integer
        #print(list_notele_int) #[4, 10, 9, 4]
        media = mean(list_notele_int) #am calculat media notelor
        #ca sa rotunjesc, folosesc functia round(numar, decimale)
        #print(f"{el} are notele {round(media, 2)}")
        text_de_creat += f"{el} are media notelor {round(media, 2)}\n"
    return text_de_creat

#Scriu in text ce am rezultat
folder = "B:/Dropbox/SDA/SDA_52"
path_text_medii = f"text_medii.txt"
#B:/Dropbox/SDA/SDA_52/text_medii.txt

with open(f"{folder}/{path_text_medii}", "w") as f:
    nume_medii_dict = extragere_nume_note(folder)
    # print(nume_medii_dict)
    textul = returneaza_text_cu_mediile(nume_medii_dict["names"], nume_medii_dict["grades"])
    # print(textul)
    f.write(textul)

