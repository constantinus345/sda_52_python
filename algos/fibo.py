#Fibonacci - 3 solutii
# 1,1,2,3,5,8,13,21,34....

def fibo_clasic(n_th):
    nr_1 = 0
    nr_2 = 1
    nr_3 = nr_2
    count = 3
    while count <= n_th:
        count += 1
        nr_1, nr_2 = nr_2, nr_3
        nr_3 = nr_1 + nr_2

    return f"Al {n_th} numar fibonaci este {nr_3}"

print(fibo_clasic(50))

def fibo_recursiv(n_th):
    if n_th <= 1: #conditia de iesire din recursie
        return n_th
    return fibo_recursiv(n_th-1) + fibo_recursiv(n_th-2)

print(fibo_recursiv(9))

#ca sa vedem de cate ori s-a apelat recursiv functia, facem in felul urmator
def fibo_recursiv_count(nth, count=0):
    count += 1
    if nth <= 1:
        return nth, count #va returna un tuple cu 2 elemente (nth, count)
    else:
        fib_m1, count_m1 = fibo_recursiv_count(nth -1, count)
        fib_m2, count_m2 = fibo_recursiv_count(nth -2, count)
        return fib_m1 + fib_m2, count_m1+count_m2

#Al 9 numar fibonaci este 34
from time import perf_counter
start_time = perf_counter()
al_x_fibo = 38
rez_recursiv_count = fibo_recursiv_count(al_x_fibo)
print(rez_recursiv_count)
print(f"Al {al_x_fibo} element fibonacci este {rez_recursiv_count[0]}; functia s-a apelat pe sine de {rez_recursiv_count[1]}")
print(f"A durat {round(perf_counter()- start_time, 3)} secunde")

#Dynamic programming approach
#pe masura ce rezolvam problema, stocam solutia intr-o lista, ca apoi sa o folosim cand avem nevoie de ea
def fibo_dinamic(nth):
    #Initializam lista fibonacci
    lista_elemente = [1,1]
    for i in range(2, nth):
        lista_elemente.append(lista_elemente[i-1] + lista_elemente[i-2])

    return lista_elemente[nth-1]

print(fibo_dinamic(9))

#factorial 4! = 1*2*3*4