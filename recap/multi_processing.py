import multiprocessing
from time import sleep #stopeaza executia programului pentru x secunde
from random import uniform as random_rational
# print(random_rational(1.3, 2.4))

def printeaza_litere(nume, prenume):
    for litera in f"{nume}{prenume}":
        print(litera)
        sleep(random_rational(0.4, 0.9))


if __name__ == "__main__":
    proces_1 = multiprocessing.Process(target=printeaza_litere,
                                       args=("Ionescu", "Ion"))
    proces_2 = multiprocessing.Process(target=printeaza_litere,
                                       args=("Ailenei", "Ana"))
    proces_3 = multiprocessing.Process(target=printeaza_litere,
                                       args=("Vasilescu", "Vasile"))
    proces_4 = multiprocessing.Process(target=printeaza_litere,
                                       args=("Abdncs", "Georgiana"))

    proces_1.start()
    proces_2.start()
    proces_3.start()
    proces_4.start()

    #join() este optional
    #roul join este de a se asigura ca procesul/ threadul a fost executat inainte sa mearga la
    # urmatoarele instructiuni
    #fara join() print("Whatever") se poate executa inainte ca procesele de thread/mp sa se finalizeze

    proces_1.join()
    proces_2.join()
    proces_3.join()
    proces_4.join()

    print("Whatever")


