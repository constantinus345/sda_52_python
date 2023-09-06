import threading
from time import sleep #stopeaza executia programului pentru x secunde
from random import uniform as random_rational
# print(random_rational(1.3, 2.4))

def printeaza_litere(nume, prenume):
    for litera in f"{nume}{prenume}":
        print(litera)
        sleep(random_rational(0.1, 0.3))

# printeaza_litere("Ion", "Ionescu")
# printeaza_litere("Ailenei", "Ana")

#pentru a executa mai multe functii in acelasi timp, V1 - folosim multithreading

thread_1 = threading.Thread(target=printeaza_litere, args=("Ionescu", "Ion"))
thread_2 = threading.Thread(target=printeaza_litere, args=("Ailenei", "Ana"))

thread_1.start()
thread_2.start()
