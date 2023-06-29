def creeaza_fisiere_cu_nume(folder, *nume):
    #*args e o conventie, dar putem pune si alta denumire
    for n in nume:
        with open(f"{folder}/{n}.txt", "w") as file:
            #f"{folder}/{n}.txt" - am creat full path la fisier
            #de exemplu daca folder = "B:/Dropbox/" si numele este vasile,
            #atunci rezultatul va fi f"{folder}/{n}.txt" = "B:/Dropbox/vasile.txt"
            file.write(f"{n} are {len(n)} caractere")

path_folder = "B:/Dropbox/SDA/SDA_52/Iunie 29"
creeaza_fisiere_cu_nume(path_folder, "ion", "Ana", "Nathan", "Catalin")

def adauga_text_in_fisiere(folder, *args):
    for file in args:
        with open(f"{folder}/{file}.txt", "a") as fisier_existent:
            fisier_existent.write("\n2Astazi e o zi faina")

adauga_text_in_fisiere(path_folder, "ion", "Ana", "Nathan")