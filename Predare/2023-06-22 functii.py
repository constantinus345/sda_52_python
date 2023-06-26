a = 5
b = 7
# print(a**2 + b**2)

def patratul_sumelor(a,b):
    rezultat = a**2 + b**2
    return rezultat

print(patratul_sumelor(a,b))

def email_personalizat(prenume, suma_cumparat):
    emailul = f"""
    Salut {prenume}, 
    Iti multumim ca ai cumparat de la noi pana acum in valoare de {suma_cumparat} lei.
    Vrem sa iti oferim un voucher in valoare de {suma_cumparat * 0.1} lei valabil pana
    saptamana viitoare.
    """
    return emailul #asa returneaza functia o valoare

l_prenume = ["Ion", "Elena", "Ana"]
l_sume = [123, 12345, 54635]
for index, prenume in enumerate(l_prenume):
    print(email_personalizat(prenume, l_sume[index]))

#enumerate- ne ofera posibilitatea de a accesa indexul si valoarea
prenume = ["Ion", "Elena", "Ana", "Ion"]

for ix, p in enumerate(prenume):
    print(p, ix)
print(list(enumerate(prenume))) #[(0, 'Ion'), (1, 'Elena'), (2, 'Ana'), (3, 'Ion')]

angajati = [("Ion", 29, 12300), ("Ana", 27, 14000), ("Elena", 25, 11000)]
for prenume, varsta, salariu in angajati:
    print(f"{prenume} are {varsta} ani si salariul = {salariu}")
#Echivalent cu
for el in angajati:
    print(f"{el[0]} are {el[1]} ani si salariul = {el[2]}")

#(x**2+1) * (y**2+1)*....
n_1 = 2
n_2 = 3
rez = (n_1**2 + 1) * (n_2**2 +1)

def produsul_patr_1(n1, n2):

    #rez = 1
    rez = (n1**2 + 1) * (n2**2 +1)
    return rez

print(produsul_patr_1(2,3))

def produsul_patr_nedeterminat(*args):
    rez = 1
    #*args inseamna un numar nedeterminat de argumente
    #pentru a le accesa, trebuie sa iteram pe ele
    for a in args:
        rez *= (a**2 +1)
        #print(rez)
    return rez

var_1 = produsul_patr_nedeterminat(1,2,34,345,246)
#daca nu avem return ceva_valoare, atunci functia returneaza None
print(var_1)

def suma_numere(*args):
    rez = 0
    for a in args:
        rez += a
    return rez

print(suma_numere(1,2,3,4,19,2345))

print(suma_numere) #aici functia nu a fost apelata, va returna simplu locatia in memorie a functiei

def salutare(): #functia nu are nici un argument
    print("Salutare la toata lumea")

val = salutare() #val are valoare none, pentru ca functia nu a returnat nimic
print(val)

def salutare_nume(nume):
    print(f"Salutare {nume}, ce mai faci?")

salutare_nume("Ana")

def salut_lung_scurt(nume):
    #salutam diferit in dependenta de lungimea numelui
    #Returnam salutarea, nu o vom printa!
    if len(nume) < 7:
        salutarea = f"Salut {nume}, ai un nume usor de pronuntat"
    else:
        salutarea = f"Salut {nume}, ai un nume lung dar interesant"

    return salutarea

hello = salut_lung_scurt("Alexandru")
print(hello)

#Varianta simplificata
def salut_lung_scurt_v2(nume):
    # salutam diferit in dependenta de lungimea numelui
    # Returnam salutarea, nu o vom printa!
    if len(nume) < 7:
        return f"Salut {nume}, ai un nume usor de pronuntat"
    else:
        return f"Salut {nume}, ai un nume lung dar interesant"

hello = salut_lung_scurt_v2("Alexandru")
print(hello)

#V3 si mai simplificat
def salut_lung_scurt_v3(nume):
    # salutam diferit in dependenta de lungimea numelui
    # Returnam salutarea, nu o vom printa!
    if len(nume) < 7:
        return f"Salut {nume}, ai un nume usor de pronuntat"
    #daca s-a facut return o data, nu se mai executa nimic mai departe si functia iese din executie
    return f"Salut {nume}, ai un nume lung dar interesant"

hello = salut_lung_scurt_v3("Alexandru")
print(hello) #al doilea return
hello = salut_lung_scurt_v3("Ion")
print(hello) #intra in primul return

print("Ana", "Ion", "Bob", sep="--")
print("Ana", "Ion", end = ", ", sep = "--")
print("Bob", "Jan", end = ", ", sep = "--")

def email_personalizat_argumente(prenume, suma_cumparat, magazinul = "Nr2"):
    #magazinul = "Nr2" - aegument default/implicit
    #daca nu dam valoare la variabila magazinul, va fi automat = "Nr2"
    emailul = f"""
    Salut {prenume}, 
    Iti multumim ca ai cumparat de la noi pana acum in valoare de {suma_cumparat} lei.
    Vrem sa iti oferim un voucher in valoare de {suma_cumparat * 0.1} lei valabil pana
    saptamana viitoare.
    
    Cu respect,
    Magazinul {magazinul}
    """
    return emailul #asa returneaza functia o valoare

print(email_personalizat_argumente("Andrei", 1000))
print(email_personalizat_argumente(prenume = "Andrei", suma_cumparat = 1000))
print(email_personalizat_argumente(prenume = "Andrei",
                                   suma_cumparat = 1000,
                                   magazinul = "Alt Magazin"))