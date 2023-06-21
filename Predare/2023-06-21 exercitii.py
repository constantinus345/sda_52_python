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

#Daca vreau ca patratele sa fie intre 1 si 100 inclusiv, divizibil cu 3
lista_patrate_100 = [n**2 for n in range(1,101) if (n**2 <= 100) and (n % 3 == 0)]
print(lista_patrate_100)

#3. Creati o lista cu lungimea fiecarui cuvant dintr-un string
propozitia = "Ce mai faci mai Ionele"
list_cuv = [len(cuv) for cuv in propozitia.split()]
#propozitia.split() imi extrage fiecare cuvant din propozitie
print(list_cuv)