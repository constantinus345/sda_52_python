from time import perf_counter, sleep
from random import randint, choices
import string
"""
randint ma ajuta sa aleg un numar random de la a la b
print(randint(3,12))
"""


def masoara_performanta(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        rezultatul = func(*args, **kwargs)
        end_time = perf_counter() #este valoarea de "acum"
        took_time = end_time - start_time
        print(f"Functia s-a executat in {round(took_time,4)} secunde")
        return rezultatul
    return wrapper

@masoara_performanta
def f_1():
    print("S-a inceput")
    #iau o pauza de la executare
    sleep(3)
    print("S-a executat")

f_1()

#1,1,2,3,5,8,13,21...
@masoara_performanta
def fibonacci_recursiv(n):
    if n in [1,2]:
        return 1
    else:
        return fibonacci_recursiv(n-1) + fibonacci_recursiv(n-2)

print(fibonacci_recursiv(20))
#decoratorul de masurare a performantei nu functioneaza pentru functii recurente,
#adica care se apeleaza pe ele insasi

#creez o functie cu un numar de elemente avand litere random
#["abc", "fergfdfher", "fsedgew"]
@masoara_performanta
def lista_elemente_random(size):
    lista = [] #list()
    for i in range(size):
        lungimea_cuv = randint(3,12)
        cuvant_random = "".join(choices(string.ascii_letters, k=lungimea_cuv))
        lista.append(cuvant_random)
    return lista

l_1 = lista_elemente_random(4*10**6)
print(l_1[:3])


#Decorator care imi zice la ce ora s-a inceput executarea functiei si la ce ora s-a terminat
from datetime import datetime
# now = datetime.now()
# print(now)

def inceput_final_ora(func):
    #func este functia care o voi decora
    def wrapper(*args, **kwargs):
        #*args, **kwargs - sunt argumentele functiei care o voi decora
        ora_inceput = datetime.now()
        print(f"Executarea {func.__name__} s-a inceput la ora {ora_inceput}")

        rez = func(*args, **kwargs)

        ora_final = datetime.now()
        print(f"Executarea {func.__name__} s-a terminat la ora {ora_final}")
        return rez
    return wrapper

@inceput_final_ora
def lista_elemente_random(size):
    lista = [] #list()
    for i in range(size):
        lungimea_cuv = randint(3,12)
        cuvant_random = "".join(choices(string.ascii_letters, k=lungimea_cuv))
        lista.append(cuvant_random)
    return lista

l_3 = lista_elemente_random(3*10**6)


@inceput_final_ora
def f_1():
    print("S-a inceput")
    #iau o pauza de la executare
    sleep(3)
    print("S-a executat")

f_1()

#Arhitectura unui decorator, in mare parte este copy-paste + logica sa

def denumire_decorator(functie_decorata):
    # func este functia care o voi decora
    def wrapper(*args, **kwargs):
        # *args, **kwargs - sunt argumentele functiei care o voi decora
        #logica_1
        rez = functie_decorata(*args, **kwargs)
        #logica_partea_2, optional
        return rez

    return wrapper

@denumire_decorator #asa decoram functia
def o_functie():
    pass



#Decorator care incearca sa execute o functie de mai multe ori

#Un numar specific de ori, 3

def retry_3(functie_decorata):
    def wrapper(*args, **kwargs):
        for incercare in range(1,4):
            try:
                rez = functie_decorata(*args, **kwargs)
                return rez
            except Exception as mega_eroarea:
                print(f"Eroarea este {mega_eroarea}")
                sleep(incercare * 2) #fumez o tigara
        return "Functia nu s-a executat"
    return wrapper

@retry_3
def impartirea(a,b):
    return a/b

print(impartirea(3,5))
print(impartirea(3,0))

def retry_multiple(number_of_tries):
    def decorator_secund(functie_decorata):
        def wrapper(*args, **kwargs):
            for incercare in range(1,number_of_tries+1):
                try:
                    rez = functie_decorata(*args, **kwargs)
                    return f"Rezultatul este {rez}"
                except Exception as mega_eroarea:
                    print(f"Eroarea este (incercarea {incercare}) {mega_eroarea}")
                    sleep(incercare * 2) #fumez o tigara
            return "Functia nu s-a executat"
        return wrapper
    return decorator_secund

@retry_multiple(4)
def impartirea(a,b):
    return a/b

print(impartirea(3,5))
print(impartirea(3,0))

