#functie care calculeaza suma cifrelor dintr-un string
import re


def suma_cifrelor(stringx):
    suma = 0
    for caracter in stringx:
        try:
            cifra = int(caracter)
            suma += cifra
            #print(f"cifra = {cifra}, suma = {suma}")
        except ValueError:
            pass
    return suma

strx = '1h2nhb-98'
print(suma_cifrelor(strx))

lista = ['1h2nhb-98', 'hfsd755']
lista_suma = [suma_cifrelor(x) for x in lista]
print(lista_suma)

#pattern matching l;a cuvintele care ioncep cu A sau B
text_localitati = "Anul acesta am vizitat Brasov, Bucuresti, Iasi si Arad"
pattern_ab = r'\b[A|B]\w+\b'
#\b incepe sau se termina cu...
#[A|B] A sau B, un singur caracter by default = [A|B]{1}
#\w+ orice caracter a-Z sau 0-9, + inseamna 1+ repetari

matches = re.findall(pattern_ab, text_localitati)
print(matches)

