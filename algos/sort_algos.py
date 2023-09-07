
#in python exista deja un mod simmplu de sortare
lis2 = [234,342,135,4352,3422,144,1,45,2,-23, -2, 0, 123545]
lis2.sort()
print(lis2)

#
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] #am schimbat cu locul elementele
    return lista

lis2 = [234,342,135,4352,3422,144,1,45,2,-23, -2, 0, 123545]
print(bubble_sort(lis2))

def insertion_sort(lista):
    #Traversam lista, incepand cu al doilea element
    for i in range(1, len(lista)):
        #selectam elementul curent, la indecele i
        el = lista[i]
        j = i - 1 #pentru a calcula indicele elementului precedent celui cu indicele i
        while el < lista[j] and j >= 0:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = el

    return lista

lis2 = [234, 342, 135, 4352,3422,144,1,45,2,-23, -2, 0, 123545]
print(f"Lista acum este {lis2}")
print(f"Lista sortata cu insertion = {insertion_sort(lis2)}")

def selection_sort(lista):
    lung = len(lista)
    for i in range(lung):
        i_2 = i
        for j in range(i+1, lung):
            if lista[j] < lista[i_2]:
                i_2 = j
        lista[i], lista[i_2] =  lista[i_2], lista[i] #swap, schimbat locul reciproc

    return lista

lis2 = [234, 342, 135, 4352,3422,144,1,45,2,-23, -2, 0, 123545]
print(f"Lista acum este {lis2}")
print(f"Lista sortata cu selection sort este {selection_sort(lis2)}")
#https://visualgo.net/en/sorting
#https://www.toptal.com/developers/sorting-algorithms


