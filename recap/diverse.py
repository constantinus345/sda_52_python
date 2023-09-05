#functie care calculeaza suma cifrelor dintr-un string

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