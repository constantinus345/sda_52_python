#radacina patrata a unui numar
print(25**0.5)

import math
print(math.sqrt(25))

#sin
print(math.sin(2))

#Ce fisere am intr-un folder
import os #os- Operating System

path = "B:/Dropbox/SDA/SDA_51"
#https://pathcopycopy.github.io/

print(r"ceva\aici\nu\e\bine")
print(os.listdir(path)) #['ceva_text_creat.txt', 'fisier_2.txt', 'fisier_cu_note.txt', 'primul_text.txt']

#In python sunt module built-in, adica care nu trebuie instalate
#de exemplu math, os, statistics
# import statistics
from statistics import mean
print(mean([1,2,3,4]))

#Moduri de a importa module
import math #importa toata librarie, astfel putem folosi toate metodele/functiile din libraria math
print(math.factorial(5))

from math import factorial #import o singura functie din librarie

from math import factorial as fact
#as fact inseamna ca am redenumit functia, alias
print(fact(5))

from math import * #CODE SMELL - importa totate functiile si incarca memoria cu ele!
#NOT OK!

import time
import random

def functie_complicata():
    print(7)
    timp_random = random.randint(2,5)
    print(f"Intervalul random = {timp_random}")
    time.sleep(timp_random)
    #pune codul pe pauza 3 secunde
    print(9)

timp_start = time.perf_counter() #perfomance counter
functie_complicata()
timp_took =  time.perf_counter() - timp_start
print(f"Operatiunea a durat {timp_took} secunde")

#Varianta mai curata a codului

from time import sleep, perf_counter
from random import randint

def functie_complicata():
    print(7)
    timp_random = randint(2,5)
    print(f"Intervalul random = {timp_random}")
    sleep(timp_random)
    #pune codul pe pauza 3 secunde
    print(9)

timp_start = perf_counter() #perfomance counter
functie_complicata()
timp_took =  perf_counter() - timp_start
print(f"Operatiunea a durat {timp_took} secunde")


