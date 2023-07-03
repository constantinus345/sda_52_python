class Contact:

    def __init__(self, prenume = None, telefon = None):
        #__init__ -este o metoda speciala a Clasei care imi initializeaza parametrii obiectului ce il voi crea
        #obiect = instanta a clasei, de exempu un contact anume pentru Clasa Contact.
        #self - parametru special utilizat in definitia si accesarea parametrilor unui obiect
        #self se foloseste independent in alte metode, fara a mai declara inca o data parametrii clasei

        self.prenume = prenume
        self.telefon = telefon

    def afisare_contact(self):
        #metode - functii care imi da voie sa procesez parametrii Clasei, efectueaza operatii cu parametrii
        #de ce aici am doar self
        print(f"{self.prenume} are telefonul {self.telefon}")

    def afisare_in_telefon(self):
        if self.prenume: #daca i-am dat valoare prenumelui
            print(f"suna pe {self.prenume}")
        else:
            print(f"suna pe {self.telefon}")

Ion = Contact(prenume="Ionica",telefon="+40777444555")
#Ion = ... am initializat un obiect al clasei
Ion.afisare_contact() #Am apelat metoda afisare_contact a clasei Contact pentru obiectul Ion

Elena = Contact(prenume="Lenuzza",
                telefon="+40777888999")

Elena.afisare_contact()
Elena.afisare_in_telefon()

Cineve_fara_nume = Contact(prenume = None, telefon="0788899955")

Cineve_fara_nume.afisare_in_telefon()


class ContactCuOrigine:

    def __init__(self, prenume, telefon, originea_apelantului):
        # __init__ -este o metoda speciala a Clasei care imi initializeaza parametrii obiectului ce il voi crea
        # obiect = instanta a clasei, de exempu un contact anume pentru Clasa Contact.
        # self - parametru special utilizat in definitia si accesarea parametrilor unui obiect
        # self se foloseste independent in alte metode, fara a mai declara inca o data parametrii clasei

        self.prenume = prenume
        self.telefon = telefon
        self.originea_apelantului = originea_apelantului

    def afisare_contact(self):
        # metode - functii care imi da voie sa procesez parametrii Clasei, efectueaza operatii cu parametrii
        # de ce aici am doar self
        print(f"{self.prenume} are telefonul {self.telefon}")

    def afisare_in_telefon(self, prenume):
        if self.prenume:  # daca i-am dat valoare prenumelui
            print(f"suna pe {self.prenume}")
        else:
            print(f"suna pe {self.telefon}")

    def numar_corect(self):

        if self.telefon.startswith(("+40", "00")):
            return self.telefon
        else:
            if self.telefon.startswith("0"):
                telefonx = self.telefon[1:]
            return f"{self.originea_apelantului}{telefonx}"

Andrei = ContactCuOrigine("Andrei", "077774412", "+40")
print(Andrei.numar_corect())

Andreea = ContactCuOrigine("Andreea", "+4077774412", "+40")
print(Andrei.numar_corect())

class Animal:

    def __init__(self, dieta: str, varsta: int, domestic: bool, vertebrat: bool):
        self.dieta = dieta
        self.varsta = varsta
        self.domestic = domestic
        self.vertebrat = vertebrat

    def botez(self):
        numele = input("Cum il cheama pe animal ? = ")
        print(f"{numele} este un animal {'vertebrat' if self.vertebrat else 'nevertebrat'}")
        #'vertebrat' if self.vertebrat else 'nevertebrat' = adica imi va da "vertebrat"
        #daca self.vertebrat = True, in caz invers = "nevertebrat"
        #Putem folosi in acelasi f-string ghilimele " si ', doar ca una trebuie sa fie in interiorul alteia

Ursuletul = Animal(dieta ="omnivor",
                   varsta = 12,
                   domestic = False,
                   vertebrat = True)

print(Ursuletul) #<__main__.Animal object at 0x000001B7A0B9BED0>
Ursuletul.botez()

Râma_mea = Animal(dieta ="pământ",
                  varsta=0.3,
                  domestic=False,
                  vertebrat=False)

Râma_mea.botez()
