from datetime import datetime

year = datetime.now().year
class Om:
    def __init__(self, prenume, an_nastere):
        #__metoda__ se numesc dunder methods
        self.prenume = prenume
        self.an_nastere = an_nastere

    def intro_yourself(self):
        print(f"Ma numesc {self.prenume} si am {year - self.an_nastere} ani.")

    def modificare_nume(self, nume_nou):
        #redenumesc un parametru al functiei, si anume prenumele
        self.prenume = nume_nou

class Cetatean(Om):
    #(Om) - astfel am mostenit / inheritance caracteristicile de la clasa Om, adica parametrii si metodele
    def __init__(self, prenume, an_nastere, nationalitate):
        super().__init__(prenume, an_nastere) #am mostenit parametrii clasei de la care mostenesc- Om
        #initializeaza din clasa superioara
        self.nationalitate = nationalitate

    def ce_nationalitate(self):
        print(f"Sunt de nationalitate {self.nationalitate}")

class AngajatLaStat(Cetatean):
    def __init__(self, prenume, an_nastere, nationalitate, pensie_speciala, **kwargs):
        super().__init__(prenume, an_nastere, nationalitate)
        self.pensie_speciala = pensie_speciala
        self.kwargs = kwargs

    def ce_pensie_speciala(self):
        print(f"Pensia mea speciala este {self.pensie_speciala}")

    def altceva_despre(self):
        Text = ""
        for key, val in self.kwargs.items():
            Text += f"{key} -> {val}\n"
        print(f"Altceva despre mine: \n{Text}")

Angajat_Vasilica = AngajatLaStat(prenume="Vasile",
                                 an_nastere = 1980,
                                 nationalitate ="român",
                                 pensie_speciala = 20000)

Angajat_Vasilica.intro_yourself() #apeleaza metoda de la "clasa bunic" Om
Angajat_Vasilica.ce_nationalitate() #apeleaza de la clasa "parinte" Cetatean
Angajat_Vasilica.ce_pensie_speciala() #apeleaza metoda de la clasa proprie

Angajat_Vasilica.modificare_nume("Vasile II")
Angajat_Vasilica.intro_yourself()

#Apelez la valorile Obiectului creat
print(Angajat_Vasilica.prenume)
print(Angajat_Vasilica.nationalitate)
print(Angajat_Vasilica.pensie_speciala)

Angajata_Ileana = AngajatLaStat(prenume="Elena",
                                an_nastere = 1970,
                                nationalitate ="român",
                                pensie_speciala = 40000,
                                copii = 3,
                                absolvent = "Scoala de Administratie Publica",
                                vechime_munca = 32,
                                hobby = "Alpinism")

Angajata_Ileana.modificare_nume("Ilenuzza")
Angajata_Ileana.intro_yourself()

Angajata_Ileana.altceva_despre()