class Contact:
    def __init__(self, prenume, email, telefon):
        self.prenume = prenume
        self.email = email
        self.telefon = telefon

    def intro(self):
        return f"Salutare, acesta este contactului lui {self.prenume}"

    def trimite_email(self, to_x, subject_x, text_body_x, from_x, client_email):
        if client_email == "gmail":
            return f"Se trimite email catre {self.email} prin google email"
        else:
            return f"Se trimite email catre {self.email} prin alt operator decat gmail"


contact_1_ion = Contact("Ion", "i@abc.ro", "+40787821")
contact_2_ana = Contact(prenume="Ana",
                        telefon="07514",
                        email="a@abc.ro")

print(f"Primul contact este {contact_1_ion.prenume} cu emailul {contact_1_ion.email}")
print(f"{contact_2_ana.prenume} are numarul de telefon {contact_2_ana.telefon}")

contact_1_ion.intro()
contact_1_ion.trimite_email("gmail")


#inheritance / mostenire a claselor din alte clase
class Animal:
    def __init__(self, greutate, sunet):
        self.greutate = greutate
        self.sunet = sunet

    def sunet_propriu(self):
        return f"Animalul acesta are sunetul {self.sunet}"

class Mamifere(Animal):
    def __init__(self, greutate, sunet, perioada_gestatie, tip_animal):
        self.perioada_gestatie = perioada_gestatie
        self.tip_animal = tip_animal
        #super().__init__(greutate, sunet)
        Animal.__init__(self, greutate, sunet)

    def gestatie(self):
        return f"Perioada de gestatie la {self.tip_animal} este de {self.perioada_gestatie}"

cimpanzeu = Mamifere(59, "ikihihaha", "243 days", "cimp")
cimpanzeu.sunet_propriu()
cimpanzeu.gestatie()

#class pisici inherits from Mammal
class Pisici(Mamifere):
    def __init__(self, greutate, sunet, perioada_gestatie, tip_animal, prada_preferata):
        self.prada_preferata = prada_preferata
        #Animal.__init__(self, greutate, sunet)
        Mamifere.__init__(self,  greutate, sunet, perioada_gestatie, tip_animal)

    #method overload
    def sunet_propriu(self):
        return f"Pisica asta de tip {self.tip_animal} face un sunet feroce = {self.sunet}"

Leu = Pisici(200, "Roar", "110 zile", "Ditamai Leul", "Antilope")
print(f"{Leu.tip_animal} are prada preferata {Leu.prada_preferata} delicioase")
Leu.sunet_propriu()



#private and protected attributes
class Masini:
    def __init__(self, brand):
        #acestea sunt atributele obiectului
        self.brand = brand
        #private attribute, __ face atributul privat
        self.__material_secret = "Metal din Meteorit"
        #protected attribute, _ - este o conventie! Adica putem accesa aceast atribut
        self._fabrica_secreta = "Brasov"

    #functiile in interiorul clasei se numesc metode
    def lungimea_material_secret(self):
        return f"Materialul secret are {len(self.__material_secret)} caractere. Prin aceasta metoda am demonstrat ca putem accesa totusi atributele private"

masina_mea = Masini("Audi")
print(masina_mea.brand)
print(masina_mea.__material_secret)
print(masina_mea._fabrica_secreta)
masina_mea.lungimea_material_secret()

#class variables
class Masini:
    variabila_clasei = "O variabila accesibila clasei"
    def __init__(self, brand):
        self.brand = brand

masina_1 = Masini("Audi")
masina_2 = Masini("BMW")
print(masina_2.brand)
print(masina_2.variabila_clasei) #putem accesa variabila clasei prin fiecare obiect
print(Masini.variabila_clasei) #sau direct prin clasa propriu-zisa, fara a crea un obiect
print(Masini.brand) #AttributeError


#classmethod, staticmethod - decoratori
class Masina:
    variabila_clasei = 1

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def creste_valoarea_variabilei_clasei(cls):
        #cls - acceseaza variabilele clasei
        #self -acceseaza variabilele obiectului creat
        cls.variabila_clasei += 2

Masina.creste_valoarea_variabilei_clasei()
print(Masina.variabila_clasei)


class Masina:
    variabila_clasei = 1

    def __init__(self, brand):
        self.brand = brand

    @staticmethod
    #de obicei functii utilitate, care nu au nevoie de a accesa proprietarile
    #obiectului self, sau a clasei cls
    def zi_ceva_frumos():
        return "Wow ce masina ai"

#ABC - Abstract Base Class
from abc import ABC, abstractmethod
from math import pi
# print(pi)
class FiguraGeometrica(ABC):
    @abstractmethod
    def perimetru(self):
        pass

    @abstractmethod
    def arie(self):
        pass

class Patrat(FiguraGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def perimetru(self):
        return f"Perimetru patratului cu latura de {self.latura} este = {self.latura * 4}"

    def arie(self):
        return self.latura ** 2

class Cerc(FiguraGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def perimetru(self):
        return 2*pi* self.raza

    def arie(self):
        return pi * self.raza * self.raza

un_patrat_1 = Patrat(10)
un_patrat_1.arie()
un_patrat_1.perimetru()

un_cerc_1 = Cerc(5)
un_cerc_1.arie()
un_cerc_1.perimetru()

#dunder methods
#__ceva__
# print(__name__)
class Masina:
    def __init__(self, brand, serie_sasiu):
        self.brand = brand
        self.serie_sasiu = serie_sasiu
    #metodele __ = dunder methods, magic methods
    def __str__(self):
        return f"Masina asta este de la compania {self.brand}"

    def __eq__(self, other):
        if self.serie_sasiu == other.serie_sasiu:
            return "Este aceeasi masina"
        return "Masinile sunt diferite"

masina_mea_1 = Masina("No brand", "456")
masina_mea_2 = Masina("Audi", "456")
print(masina_mea_1 == masina_mea_2)

#Creez o clasa de bani cu diverse valute, si definesc ce inseamna adaugarea lor dupa cursul de schimb
class Bani:
    def __init__(self, amount, valuta, cursul_ron):
        self.amount = amount
        self.valuta =valuta
        self.cursul_ron = cursul_ron

    def __add__(self, other):
        if self.valuta == other.valuta:
            amount = (self.amount + other.amount) * self.cursul_ron
            return Bani(amount, "RON", self.cursul_ron)
        else:
            #daca avem doua valute diferite
            amount_1 = self.amount * self.cursul_ron
            amount_2 = other.amount * other.cursul_ron
            amount = amount_1 + amount_2
            return Bani(amount, "RON", 1)

bani_1 = Bani(100, "USD", 4.5)
bani_2 = Bani(50, "USD", 4.5)
bani_1_2 = bani_1 + bani_2
print(f"In RON avem {bani_1_2.amount} RON")

bani_3 = Bani(200, "EUR", 5)
bani_1_3 = bani_1 + bani_3
print(f"{bani_1.amount} {bani_1.valuta} + {bani_3.amount} {bani_3.valuta} = {bani_1_3.amount} RON")