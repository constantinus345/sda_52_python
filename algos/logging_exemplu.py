#logging se foloseste pentru a loga raportul de executare a unui program

import logging
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")
print(f"Astazi este data de {today}")
# #https://www.w3schools.com/python/python_datetime.asp

folder_logs = "B:/pyx/SDA/SDA_52/Logs" #locatia folderului unde voi pune logs-urile
logging.basicConfig(
                    filename=f"{folder_logs}/loguri_{today}.log",
                    format="%(asctime)s -- %(levelname)s -- %(message)s ",
                    filemode="a"
                    )
#documentatie logging  https://docs.python.org/3/howto/logging.html oficiala
obiect_logger = logging.getLogger() #am creat obiectul de logging
obiect_logger.setLevel(logging.DEBUG)
"""
Niveluri de logging (conventie)
debug
info 
warning
error
critical
"""

def operatii_mate(a, b):
    try:
        suma = a + b
        produsul = a * b
        impartirea = a / b
        rezultat = f"Suma = {suma}, prod= {produsul}, impart = {impartirea}"
        print(rezultat)
        obiect_logger.info(f"Programul s-a executat cu succes pentru variabilele {a} si {b}")
    except Exception as e:
        print(e)
        obiect_logger.warning(f"Pentru vars {a} si {b} programul a intampinat o eroare: {e}")

operatii_mate(18,9)
operatii_mate(18,0)
operatii_mate(18,2)

obiect_logger.critical("Aoleu, programul sta degeaba #Dorel")