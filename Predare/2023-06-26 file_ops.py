main_path = 'B:/Dropbox/SDA'

#Creez Folder SDA_52
import os

sda_52 = f"{main_path}/SDA_52"
os.mkdir(sda_52)

#Creez un fisier txt in care scriu text_1
text_1 = "Afara este frumos, dar noi invatam programare!"
operatiunea_scriere = "w"
with open(f"{sda_52}/primul_fisier.txt", operatiunea_scriere) as filex:
    #filex este un alias la operatiunile care le facem cu fisierul
    filex.write(text_1)

studenti = ["Andrei", "Ana", "Maria"]
fisier_studenti = "studentii_mei.txt"

with open(f"{sda_52}/{fisier_studenti}", operatiunea_scriere) as f:
    for nume in studenti:
        f.write(f"{nume}\n")

studenti_2 = ["Ion", "Elena", "Ioana"]
operatiunea_append = "a"
with open(f"{sda_52}/{fisier_studenti}", operatiunea_append) as f:
    for nume in studenti_2:
        f.write(f"{nume}\n")

#operatiuni de lucru cu fisiere
"""
r - read 
w- write, sterge tot si scrie intr-un fisier nou
a - append, scrie mai departe la textul existent
b - byte reading, pentru fisiere non-text
"""

operatiunea_citire = "r"
fisier_studenti = "studentii_mei.txt"
with open(f"{sda_52}/{fisier_studenti}", operatiunea_citire) as alias:
    liniile = alias.readlines()
    print(liniile)

#Fisiere excel
#Vom instala o librarie externa numita pandas
#In terminal vom scrie >>pip install pandas<<
#pip e o comanda care instaleaza librarii externe (mai multe la python technologies)
#mai avem nevoie de >>pip install openpyxl<< in terminal

main_path = 'B:/Dropbox/SDA'
sda_52 = f"{main_path}/SDA_52"
#Mai sus am folderul unde imi scriu informatia. La voi va fi putin diferit main_path

studenti = {"prenume": ["Elena", "Ana", "Ion"],
            "varsta": [23, 39, 20],
            "localitate":["Brasov", "Timisoara", "New York"]}

nume_excel = "studentii_mei.xlsx"

import pandas
#import libraria externa pandas care am instalat-o cu >>pip install pandas<<
#si eventual  >>pip install openpyxl<<

tabel = pandas.DataFrame(studenti)
#am creat un tabel din dictionarul de mai sus
print(tabel)

tabel.to_excel(f"{sda_52}/{nume_excel}", index=False)
#am salvat tabelul in fisierul excel
#index= False inseamna ca liniile/rows nu vor fi numerotate

#Citire din excel
tabel_citit = pandas.read_excel(f"{sda_52}/{nume_excel}")
#pandas.read_excel(full_path_of_excel_file) - citeste un fisier excel
print(tabel_citit)

loc = tabel_citit["localitate"].tolist()
#citeste doar o singura coloana si o transforma in lista
print(loc)

tabel_grupa_42 = pandas.read_excel(f"{sda_52}/{nume_excel}", sheet_name="grupa_42")
print(tabel_grupa_42)
