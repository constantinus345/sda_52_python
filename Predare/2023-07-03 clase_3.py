from datetime import datetime
year = datetime.now().year
class Om:
    MAX_MODIFICARE_NUME = 3
    def __init__(self, prenume, an_nastere, numar_modificari=0):
        #numar_modificari va fi by default = 0, adica nu trebuie sa-l mai initializam daca nu avem nevoie
        #__metoda__ se numesc dunder methods
        self.prenume = prenume
        self.an_nastere = an_nastere
        self.numar_modificari = numar_modificari

    def intro_yourself(self):
        print(f"Ma numesc {self.prenume} si am {year - self.an_nastere} ani.")

    def modificare_nume(self, nume_nou):
        if self.numar_modificari >= Om.MAX_MODIFICARE_NUME:
            raise Exception("Gata, ai modificat de prea multe ori!") #mesaj ca nu se mai poate modifica
        #raise Exception - ne returneaza o eroare. Detalii - intermediate
        #redenumesc un parametru al functiei, si anume prenumele
        self.prenume = nume_nou
        self.numar_modificari += 1

Vasile = Om(prenume = "Vasilica",
            an_nastere=23)

print(Vasile.prenume)
Vasile.modificare_nume("V_1")
print(Vasile.prenume)
Vasile.modificare_nume("V_2")
print(Vasile.prenume)
Vasile.modificare_nume("V_3")
print(Vasile.prenume)
Vasile.modificare_nume("V_4")
print(Vasile.prenume)
Vasile.modificare_nume("V_5")
print(Vasile.prenume)
