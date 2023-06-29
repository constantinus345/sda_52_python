suma = 3 + 4+ 5
print(suma)

def suma_3(a, b, c):
    suma = a + b + c
    print(suma)

suma_3
print(suma_3) #<function suma_3 at adresa_memorie>
#functia trebuie apelata cu ()
suma_3(3,5,9)

def suma_3_cu_default(a, b=1, c=2):
    #b si c au valori default, daca nu dau alte valori, acestea sunt predefinite cu 1, resp. 2
    suma = a + b + c
    print(suma)

suma_3_cu_default(3) #3+1+2
suma_3_cu_default(3,5) #3+5+2
suma_3_cu_default(10,20,30) #60

#functiile pot fi predefinte in python, precum len, sum, dict, append ...
#...sau pot exista din librariile importate, de exemplu math.factorial(x)
#... sau pot fi create de mine, cum am facut mai sus

#O functie poate executa doar cod, sau poate si returna o valoare

var_1 = suma_3_cu_default(1,2,3)
print(var_1) #va printa 6, None- adica executa comenzile din functie, dar nu returneaza nimic

#Functie care calculeaza suma unor numere, apoi *2
def suma_numere_x2(*args):
    #*args inseamna numar nedefinit de argumente, adica pot da functiei 2,3 sau 13.. argumente
    suma = 0
    for a in args:
        suma += a
    print("un print")
    print("alt print")
    return suma * 2
    #in return pot pune atat o valoare calculata, cat si o operatie de calculat

var_2 = suma_numere_x2(1,2,3)
print(var_2) #va executa tot codul, plus returneaza valoare.

#scriu o functie care returneaza 3 valori
#suma, produsul si media a unui numar nedefinit de argumente intregi
def suma_produs_media(*args):
    suma = 0
    produs = 1
    for a in args:
        suma += a
        produs *= a
    media = suma/len(args)
    return {"suma":suma, "produs": produs, "media": media}
    #am returnat o singura valoare, adica un dictionar

var_3 = suma_produs_media(2,3,4)
print(var_3)

#Alta metoda de return
def suma_produs_media_v2_return(*args):
    suma_variabila = 0 #am initializat cu 0, ca apoi sa adunam fiecare argument cu 0, ex: 0+2+5+8
    produs = 1
    for a in args:
        suma_variabila += a
        produs *= a
    media = suma_variabila/len(args)
    #len(args) - numar de argumente care le dam functiei
    return suma_variabila, produs, media
    #am returnat 3 valori deodata care constituie un tuplu ordonat

var_4 = suma_produs_media_v2_return(2,3,4)
print(var_4) #(9, 24, 3.0)- tuplu cu (suma, produs, media)

var_5 = suma_produs_media_v2_return(3,4,5,6,7,8)
print(var_5) #(33, 20160, 5.5)

#cum dam unei functii un numar nedefinit de argumente cu chei
def exemplu_keywords(**kwargs):
    #kwargs = key-word argument
    for key, value in kwargs.items():
        print(f"Cheia = {key}, valoarea = {value}")

exemplu_keywords(nume="Ion", varsta=15, localitate="Brasov")

def suma(a,b):
    suma_mea = a +b
    print("Rezultatul este")
    print(f"rezultatul din functie = {suma_mea}")
    print("Gata")

    return suma_mea

var_8 = suma(3,4)
print(f"Rezultatul stocat in variabila = {var_8}")

def comanda_restaurant(**kwargs):
    for produs, cantitate in kwargs.items():
        print(f"Produsul {produs} a fost pregatit cu {cantitate} portii")

    #return "Pofta mare"

mananc_azi = comanda_restaurant(icre=3, paste=2)
if mananc_azi is None: #is None -> nu are valoare, adica nu am dat return vreo valoare
    print("Produsele sunt gata, dar sunt la bucatarie (nu avem return)")
else:
    print(mananc_azi)
