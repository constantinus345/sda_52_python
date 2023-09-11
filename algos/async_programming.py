from time import sleep, perf_counter
from random import randint
import asyncio
def printeaza_doua(a,b):
    print(a)
    timp_asteptare = randint(1,5)
    print(f"Pentru valorile {a} si {b} programul va astepta {timp_asteptare} secunde")
    sleep(timp_asteptare)
    print(b)



async def printeaza_doua_asyncrona(a,b):
    print(a)
    timp_asteptare = randint(1,5)
    print(f"Pentru valorile {a} si {b} programul va astepta {timp_asteptare} secunde")
    await asyncio.sleep(timp_asteptare) #sleep care nu blocheaza codul din afara functiei
    print(b)

async def executare():
    await asyncio.gather(printeaza_doua_asyncrona(1,2),
                         printeaza_doua_asyncrona(3,4),
                         printeaza_doua_asyncrona(5,6),
                         printeaza_doua_asyncrona(7,8),
                         ) #am colectat instructiunile care vreau sa ruleze asincron

if __name__ == "__main__":
    #executare clasica
    start = perf_counter()
    printeaza_doua(1, 2)
    printeaza_doua(3, 4)
    printeaza_doua(5, 6)
    printeaza_doua(7, 8)
    print(f"A durat {round(perf_counter() - start, 4)} sec.")

    #executare cu async
    start_async = perf_counter()
    asyncio.run(executare())
    print(f"Async a durat {round(perf_counter() - start_async, 4)} sec.")

