#Creeaza o lista cu numerele pătrate de la 1 la 100 divizibile cu 3, cu 2 metode.

#v list comprehension
lista_mea = [n**2 for n in range(1,101) if n % 3 == 0]
print(lista_mea)

#v2 clasica
lista_mea_clasic = []
for n in range(1,101):
    if n % 3 == 0:
        lista_mea_clasic.append(n**2)
print(lista_mea_clasic)