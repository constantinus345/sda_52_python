#problema- avem de cautat un numar intr-o lista sortata

#S1- linear search
def search_linear(lista, target):
    for index, el in enumerate(lista):
        if lista[index] == target:
            return f"Am gasit {target} in lista la indexul {index}(linear)"
    return f"Nu a gasit  elementul {target} in lista(linear)"



def search_binary(lista, target):
    #Atentie! lista trebuie sa fie ordonata!
    #initializam indexul de start si final
    start = 0
    final = len(lista) -1

    #implementam un while in care impartim lista in 2 si determinam in care sub-lista cautam
    while start <= final:
        #calculam indexul din mijloc
        mijloc = (start+final) // 2

        #Compar elementul din mijloc cu target value
        if lista[mijloc] == target:
            return f"Am gasit elementul {target} in lista la indexul {mijloc}(binary)"
        elif lista[mijloc] < target:
            #daca elementul din mijloc e mai mic decat target, ne uitam doar la lista din dreapta
            start = mijloc + 1
            #am modificat indexul unde incepem cautarea
        else:
            final = mijloc - 1 #adica voi considera lista din stanga pentru cautarea target
            #am modificat indexul unde se termina cautarea

    return f"Nu a gasit {target} in lista(binary)"

lisx = [1,2, 45, 55, 66, 77, 89, 97, 103, 120]
tx = 46
print(search_linear(lisx, tx))
print(search_binary(lisx, tx))

