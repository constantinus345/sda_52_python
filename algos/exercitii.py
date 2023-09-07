
#like algo cu formatare adecvata

def likes(lista_care_au_dat_like):
    lung = len(lista_care_au_dat_like)
    if lung == 0:
        return "Nimeni nu a apreciat"
    elif lung == 1:
        return f"{lista_care_au_dat_like[0]} a apreciat"
    elif lung == 2:
        return f"{lista_care_au_dat_like[0]} si {lista_care_au_dat_like[1]} au apreciat"
    else:
        return f"{lista_care_au_dat_like[0]}, {lista_care_au_dat_like[1]} si alti {lung-2} au apreciat"

aprecieri = ["Ion", "Ana", "Anastasia"]
print(likes(aprecieri))

def likes_case(lista_care_au_dat_like):
    lung = len(lista_care_au_dat_like)
    #case este o meoda alternativa la if/elif/else
    match lung:
        case 0: return "Nimeni nu a apreciat",
        case 1: return f"{lista_care_au_dat_like[0]} a apreciat",
        case 2: return f"{lista_care_au_dat_like[0]} si {lista_care_au_dat_like[1]} au apreciat",
        case _: return f"{lista_care_au_dat_like[0]}, {lista_care_au_dat_like[1]} si alti {lung-2} au apreciat"

aprecieri = []
print(likes_case(aprecieri)[0])

strx = "acbdar"
print(sorted(strx))

def verifica_anagrama(c_1, c_2):
    anagrama = sorted(c_1.lower()) == sorted(c_2.lower()) #valoare bool True/False
    if anagrama:
        return f"Cuvintele {c_1} si {c_2} SUNT anagrame"
    return f"Cuvintele {c_1} si {c_2} NU sunt anagrame"

cuv_1 = "night"
cuv_2 = "thing"
print(verifica_anagrama(cuv_1, cuv_2))

# from collections import Counter
# print(Counter(cuv_1))