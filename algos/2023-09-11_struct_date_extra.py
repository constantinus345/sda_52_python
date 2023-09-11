dicx = dict()
dicx["cheie_1"] = "val_1"
dicx["cheie_2"] = "val_2"
dicx["cheie_3"] = "val_3"
dicx["cheie_4"] = "val_4"
print(dicx)
#Cheile si valorile pot aparea in alta ordine in dictionar, decat ordinea in care au fost adaugate

from collections import OrderedDict
#ajuta sa creem un dictionar cu cheile in ordinea in care au fost adaugate
dict_ordered = OrderedDict()
dict_ordered["cheie_1"] = "val_1"
dict_ordered["cheie_2"] = "val_2"
dict_ordered["cheie_3"] = "val_3"
dict_ordered["cheie_4"] = "val_4"
print(dict_ordered)

#la dictionarele clasice nu avem garantata ordinea cheilor
#pot fi printate haotic, mai ales dupa operatiuni pe acel dictionar

for key, value in dict_ordered.items():
    print(f"Cheia {key} are valoarea {value}")

#frozensets
listx = [1,2,3,2,3,3,3,4]
setx = set(listx)
print(setx)
setx.add(5)
print(setx)

#daca dorim sa cream un set care nu se poate modifica, folosim frozenset
set_frozen = frozenset(listx)
print(set_frozen, type(set_frozen))
set_frozen.add(5) #AttributeError, frozenset nu se mai poate modifica

#lista poate fi "appended" doar din capatul din dreapta
from collections import deque

lista_deque = deque()
lista_deque.append(2)
lista_deque.append(3)
lista_deque.append(4) #adauga elemente in dreapta
print(lista_deque)
lista_deque.appendleft(-4) #adauga elemente in stanga listei deque
print(lista_deque)
lista_deque.appendleft(100)
print(lista_deque)