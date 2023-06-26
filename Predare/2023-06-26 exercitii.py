#functie care genereaza reversul unui string
def reversul(textul):
    return textul[::-1]

strx = "Ionel e baiat bun"
print(reversul(strx))

#secventa collatz
# pentru orice numar, daca facem urmatoarele operatii cu el, oricand ajungem la 1
#Luam numarul N, daca e par -> /2, altfel 3*N + 1
N = 9
print(N, end= ", ")
while N != 1:

    if N % 2 == 0:
        N = N // 2
    else:
        N = N*3 + 1
    print(N, end=", ")

def collatz_numar(nr):
    Listx = [nr]
    while nr != 1:
        if nr % 2 == 0:
            nr = nr // 2
        else:
            nr = nr * 3 +1
        Listx.append(nr)
    return Listx

print(collatz_numar(7))




