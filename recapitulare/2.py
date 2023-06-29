#Librariile din python
#librariile built-in
import os
import pandas



path_folder = 'B:/Dropbox/SDA/SDA_52'
new_folder_name = "Iunie 29"
new_folder_path = f"{path_folder}/{new_folder_name}"
print(new_folder_path)
os.mkdir(new_folder_path)

fisiere = os.listdir(path_folder)
print(fisiere)

print(os.cpu_count()) #Numarul de sub-procesoare/threads in CPU-procesorul calculatorului

help(os.listdir()) #help imi printeaza documentatia tehnica a unei librarii sau metode

import math

print(math.sqrt(125))
print(math.factorial(5))

#SAU
from math import sqrt, factorial
print(sqrt(125))
print(factorial(5))

#alias la toata libraria
import math as matematica
print(matematica.sqrt(125))

from math import sqrt as radical
from math import factorial as produsul_pana_la_n
print(radical(125))
print(produsul_pana_la_n(5))

import statistics
print(statistics.mean([2,3,4]))

#in venv/lib/site-packages gasesc ce librarii am deja instalate
import time

#pentru a calcula performanta unui program/instructiuni, folosesc perf_counter
start = time.perf_counter()
print("abcf") #o instructiune banala
time.sleep(1)
print(f"A durat {time.perf_counter() - start} secunde")
#time.perf_counter() - start -> masoara diferenta de timp intre acum-start

import datetime

now = datetime.datetime.now()
print(now)
print(now.year)

timp_formatat = now.strftime("%A %d-%B-%Y")
print(timp_formatat)

#LIBRARII EXTERNE
#Se intaleaza in terminal cu comanda pip install
#pip este un sistem de instalare/management a librariilor in python


#Instalam alte librarii, ex psutil pentru RAM
import psutil

ram = psutil.virtual_memory()
print(ram) #svmem(total=102832586752, available=63391006720, percent=38.4, used=39441580032, free=63391006720)
ram_giga = ram[0] / 2**30 #calculez in GB
print(ram_giga)

#pandas ne ajuta sa interactionam cu date tabelare, inclusiv din fisiere excel
#pip install pandas
#daca e instalat precedent nu trebuie sa mai instalati cand importati


data = {"nume_elevi":["Ion", "Ana"],
        "materie_preferata": ["Fotbal", "Muzica"]}

tabel = pandas.DataFrame(data)
print(tabel)

path_folder = 'B:/Dropbox/SDA/SDA_52'
tabel.to_excel(f"{path_folder}/recap_excel_1.xlsx", index=False)

#Pentru importuri, best practice
"""
- Se importa toate la inceputul programului
- Librariile built-in si instalate se importa primele
- Apoi importam modulele, functiile, variabilele create de noi in alte fisiere
- Incercati sa importati doar ce aveti nevoie, de exemplu from math import factorial, nu import math
- Evitati sa importati asa: from math import *
- Aliasuri: cat mai putine, de ex: from math import factorial as produs_de_la_1_la_n
- etc: https://realpython.com/python-import/
"""

"""
In python exista style guide, care face codul usor de citit, oarecum standartizat
Official Style Guide: https://peps.python.org/pep-0008/ PEP-8
Google python style guide: https://google.github.io/styleguide/pyguide.html
"""
