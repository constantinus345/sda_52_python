# print(7+9)
# print("Salut ce mai faci")

# Comentariile in python incep cu #, inseamna ca putem scrie orice, nu se va executa

#functia print ne afiseaza rezultatul sau textul din paranteza
#orice functie in python este urmata de paranteze print(ceva)

#TIPURI DE DATE
#numere intregi
a = 7
#a este variabila, este o eticheta care o dam unei valori stocate in memoria calculatorului
#7 este numar intreg, eng. integer
print(a, type(a)) #va printa ... int, adica a este tip de date integer

b = 7.2
print(b, type(b)) #float, adica numar rational/real, cu virgula (in pythin se foloseste . ca delimitator de intreg)

c = "Ceva text"
print(c, type(c)) #str = string = text. Tipul de date text este mereu cu ghilimele

d = 'Ceva text 2'
print(d, type(d)) #ghilimele " si ' sunt fix la fel pentru strings, adica tipul de date text

e = """Iata aici
am ceva 
text pe mai 
multe randuri"""
print(e, type(e))

# f = "ceva aici
# pe mai multe
# randuri" #pentru text pe mai multe randuri putem folosi doar ghilimele triple """
# print(f, type(f))

#Pentru a comenta mai multe linii deodata, selectam randurile si apasam CTRL+/

"""
Comentarii pe mai multe linii cu triple ghilimele
Codul in comentarii va fi ignorat de program, este pentru utilizator
Niciodata comentariile nu se vor executa
print(2+3) nu se va executa pentru ca e comentariu
"""

g = True
print(g, type(g)) #bool, adica tip de date True sau False

h = False
print(h, type(h)) #la fel e tip de date bool, adica tip de date logic adevarat/false

i = None
print(i, type(i)) #NoneType, adica este tip de date gol

# int, float, str, bool, NoneType

nr_complex = complex(3,4) #3 + 4i
print("Partea reala a numarului complex este = ", nr_complex.real)
print("Partea imaginara cu i este egala = ", nr_complex.imag)

nr_complex_v2 = 3 + 4j #o alternativa de a scrie un numar complex
print(nr_complex_v2, type(nr_complex_v2))

#Denumirea Variabilelor
#Doar a-Z, 0-9, _
#Nu pot incepe cu cifra

abc9 = "Salut"
print(abc9)

#Dpv estetic, variabilele cu mai multe cuvinte sunt:
snake_case = ""
CamelCase = ""
# %hg = "HG"
# print(%hg) - un mod invalid de a denumi variabilele

var_1 : int = 5 # : int este un type hint, adica un indiciu al tipului de date intentionat
print(var_1, type(var_1))
var_1 : str = "cinci"
print(var_1, type(var_1))
var_1 : str = 4.567 # type hinting NU este o restrictie, cu doar indiciu non-obligatoriu
print(var_1, type(var_1))

var_2 = 3
var_3 = 4.5
var_4 = "text"
print(var_2 * var_3)
# print(var_3 * var_4)
print(var_2 + var_4)

print("text" * "ceva")


