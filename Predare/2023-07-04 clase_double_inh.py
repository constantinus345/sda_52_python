class Om:
    def __init__(self, prenume, an_nastere):
        self.prenume = prenume
        self.an_nastere = an_nastere

class Robot:
    def __init__(self, producator, nr_membre):
        self.producator = producator
        self.nr_membre = nr_membre

class Angajat:
    def __init__(self, cost, rol):
        self.cost = cost
        self.rol = rol

class OmAngajat(Om, Angajat):

    def __init__(self, prenume, an_nastere, cost, rol, tip_contract):
        Om.__init__(self, prenume, an_nastere)
        Angajat.__init__(self, cost, rol)
        self.tip_contract = tip_contract

class RobotAngajat(Robot, Angajat):
    def __init__(self, producator, nr_membre, cost, rol, nr_reparatii):
        Robot.__init__(self, producator, nr_membre)
        Angajat.__init__(self, cost, rol)
        self.nr_reparatii = nr_reparatii

elena = OmAngajat(prenume = "Elena",
                  an_nastere = 1980,
                  cost= 20000,
                  rol = "ospatar",
                  tip_contract = "3 luni")

print(elena.rol)

robo = RobotAngajat(producator = "Bosch",
                    nr_membre = 8,
                    cost = 10000,
                    rol = "ospatar",
                    nr_reparatii = 2)

print(robo.nr_reparatii)
print(robo.nr_membre)

# nr = input("Zi ceva  = ")
# print(f"Ai ales {nr}")