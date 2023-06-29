def email_personalizat(nume, voucher_procent, *args, **kwargs):
    # in args imi stockez valoarea cumparaturilor, ca apoi sa calculez totalul
    suma_totala = 0
    for cump in args:
        suma_totala += cump

    # Magazinele unde poate primi un voucher de voucher_procent% din suma totala cumparata pana acum
    magazinele = ""  # am initializat un string gol
    for key, value in kwargs.items():
        magazinele += f"Magazinul {key} la adresa {value}\n"

    email_promo = f""" 
    Salut {nume}, 
    
    Iti multumim ca pana acum ai facut cumparaturi in valoare totala de {suma_totala} lei. 
    Pentru asta iti multumim cu un voucher de {round(suma_totala * voucher_procent,1)} lei.
    Acest voucher poate fi folosit la urmatoarele magazine:
    {magazinele}
    Cu respect, 
    Ion Ionescu
    Manager Carefour
    """.replace("  ","")
    return email_promo


promo_1 = email_personalizat("Vasile Cumparescu",
                             0.02,
                             45, 670, 1000,
                             Bucuresti="Stada Vasile Alecsandri",
                             Brasov="Piata Mare")

# print(promo_1)

promo_2 = email_personalizat("Shakira",
                             0.12,
                             3000, 20000, 100000, 67890, 1889203,
                             Paris = "L'Arc du Triomphe",
                             New_York = "Manhattan",
                             Tokyo = "The Big Square",
                             Bucuresti = "Piata Obor",
                             Stockholm = "Strada Gustav cel Mare"
                             )
#*args - numar nedefinit de valori
#**kwargs - numar nedefinit de cheie&valoare

print(promo_2)

