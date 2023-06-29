def email_personalizat(nume, voucher_procent, *args, **kwargs):
    # in args imi stockez valoarea cumparaturilor, ca apoi sa calculez totalul
    suma_totala = 0
    for cump in args:
        suma_totala += cump

    # Magazinele unde poate primi un voucher de 20% din suma totala cumparata pana acum
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

print(promo_1)