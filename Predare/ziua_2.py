var_1 = "Vasile"
var_2 = "Elena"

print(var_1, "este casatorit cu", var_2)

print("Prima varianta:")
var_3_formatare = f"var_1 este casatorit cu var_2"
print(var_3_formatare) #var_1 este casatorit cu var_2

print("A doua varianta, corecta")
var_3_formatare_v2 = f"{var_1} este casatorit cu {var_2}"
print(var_3_formatare_v2)  #Vasile este casatorit cu Elena

print("A treia varianta fara f")
var_3_formatare_v3 = "{var_1} este casatorit cu {var_2}"
print(var_3_formatare_v3) #{var_1} este casatorit cu {var_2}

#Alternative la formatare
var_4_formatare = "%s este casatorit cu %s"%(var_1, var_2)
print(var_4_formatare)

var_5_formatare = "{} este casatorit cu {}".format(var_1, var_2)
print(var_5_formatare)

# Parere- pe departe consider f-strings cel mai elegant mod de formatare
# Pentru ca variabilele sunt mentionate doar o data unde sunt si apelate

#Story time
nume = "Andrei"
ani = 4
suma_totala = 150000
voucher = suma_totala * ani * 0.01

email = f"""
Salut {nume},
Ne bucuram ca esti client la noi deja de {ani} ani, si 
ai facut cumparaturi in total de {suma_totala} lei. 
Pentru care iti oferim cadou un voucher de {voucher} lei, valid pana la sfarsitul lunii.

Merci, ciao.
"""

print(email)


var_1 = "Vasile"
var_2 = "Elena"

print(var_1, end=", ") #end este "argument"/optiune a functiei print
print(var_2, end="!") #end este argument optional, seteaza cu ce se termina printul

nr = 7/2.3
print(f"Numarul v_1 = {nr:.4f}") #formatarea din acolada este valida doar cu f-string si pt numere float
#SAU
print(f"Numarul v_2 = {round(nr, 4)}") #round are ca prim argument un numar float, al doilea arg este nr decimale
#SAU
print("Numarul v_3 = ", round(nr, 4))

pr = 0.07125412841
print(f"procent v_1 = {pr:.2%}")
print(f"procent v_2 = {round(pr*100, 2)}%")

strx = "Ceva text aici salut ce faci"
strx_lungime = len(strx)
print(f"Lungimea textului >>{strx}<< este de {len(strx)} caractere")

strx_nr_3 = strx[3] #[] se folosesc inclusiv la accesarea indexului unui/unor elemente
print(strx_nr_3) #!!! indexarea/numerotarea in python este de la 0 ZERO

print(strx.count("a")) #count(sub-string) calculeaza de cate ori un sir sub-string se gaseste intr-un alt string

#string slicing
#caracterele 6-19
print(strx[6:20]) #extrage o bucata de text, de la caracterul 6 inclusiv pana la 20 Exclusiv
print(strx[0:12:2]) #extrage textul de la indicele 0 inclusiv pana la 12 exclusiv din 2 in 2 caractere
print(strx[::-1]) #scrie in ordine inversa

print(strx[-1])  #ultimul caracter
print(strx[3:]) #printeaza de la caracterul al 4-lea INCLUSIV = indicele 3 pana la final
print(strx[:3]) #printeaza pana la caracterul al 4-lea EXCLUSIV = indicele 3

#Daca vrem sa referim caracterul X de la coada
print(strx[-3]) #al 3-lea caracter de la coada
print(strx[:-3]) #: inainte = pana la, va printa pana la al 3-lea caracter de la coada, EXCLUSIV
print(strx[-3:]) #: dupa = dupa, va printa de la al 3-lea caracter de la coada inclusiv

#Exercitiu practic
#CNP
CNP = "6851112567890"
cnp_bsauf = CNP[0]

if cnp_bsauf == "1" or cnp_bsauf == "3" or cnp_bsauf == "5":
    cnp_bsauf_valoare = "barbat"
elif cnp_bsauf == "2" or cnp_bsauf == "4" or cnp_bsauf == "6":
    cnp_bsauf_valoare = "femeie"
else: #orice alta varianta
    cnp_bsauf_valoare = "CNP invalid!"

if cnp_bsauf_valoare == "CNP invalid!":
    print(f"CNP-ul {CNP} este invalid")
else:
    cnp_anul = CNP[1:3]
    cnp_luna = CNP[3:5]
    cnp_ziua = CNP[5:7]
    cnp_judet = CNP[7:9]
    cnp_unic = CNP[9:]
    print(f"cnp_bsauf = {cnp_bsauf_valoare}")
    print(f"cnp_anul = {cnp_anul}")
    print(f"cnp_luna = {cnp_luna}")
    print(f"cnp_ziua = {cnp_ziua}")
    print(f"cnp_judet = {cnp_judet}")
    print(f"cnp_unic = {cnp_unic}")


#Verificam daca un numar este par
nrx = 78

if isinstance(nrx, int):
    print("Numarul este integer")
else:
    print("Numarul nu e integer")

if nrx == 0:
    print("Number is zero")
elif nrx % 2 == 0:
    print("Numar par")
else:
    print("numar impar")
