class Om:
    def __init__(self, prenume):
        self.prenume = prenume

class Angajat(Om):
    def __init__(self, prenume, functie):
        super().__init__(prenume)
        self.functie = functie

class Student(Om):
    def __init__(self, prenume, materii_studiate):
        super().__init__(prenume)
        self.materii_studiate = materii_studiate

class AngajatStudent(Angajat, Student):
    #double inheritance
    def __init__(self, prenume, functie, materii_studiate, nr_max_ore):
        Angajat.__init__(self,prenume, functie)
        Student.__init__(self, prenume, materii_studiate)
        self.nr_max_ore = nr_max_ore

    def intro_as(self):
        intro = f"""
        Salut, ma numesc {self.prenume}. Am doua joburi:
        1. Student, invat {self.materii_studiate}
        2. Angajat, am functia {self.functie}
        Fiind student, am voie sa lucrez maxim {self.nr_max_ore}
        """
        print(intro)

Ionica = AngajatStudent(prenume= "Ion",
                        functie= "Ospatar",
                        materii_studiate= "Geografie, Economie",
                        nr_max_ore= 20)

Ionica.intro_as()