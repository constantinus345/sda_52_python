dictionar = {"nume":"Andrei",
             "localitate": "Budapesta",
             "inaltime": 178}

#cheile
for cheie in dictionar.keys():
    print(cheie)

#valorile
for valoare in dictionar.values():
    print(valoare)

#cheile & valorile
for cheie, valoare in dictionar.items():
    print(f"Cheia {cheie} are valoare {valoare}")
    print("---------")