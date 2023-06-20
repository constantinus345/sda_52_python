dx = {"prenume":["Ion", "Vasile", "Elena"],
      "varste":[23, 29, 48]}

dx["prenume"].append("Andrei")
dx["varste"].append(50)
print(dx)

dx["prenume"].extend(["Ion Senior", "Elena Senioara"])
dx["varste"].extend([78, 90])
print(dx)

alti_bunici = {"prenume": ["George", "Anastasia"],
               "varste":[89, 90]}

dx["prenume"].extend(alti_bunici["prenume"])
dx["varste"].extend(alti_bunici["varste"])
print(dx)