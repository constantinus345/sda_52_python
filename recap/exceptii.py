lista = ["Ion", "Ana", "Elena"]
x = 1


try:
    print(lista[x])
# except:
#     print(f"A aparut o eroare") - worst case de gestionare a erorilor
# except Exception as eroare: - am stocat denumirea erorii in variabila eroare
#     print(f"A aparut o eroare = {eroare}")
except IndexError:
    print(f"Ati incercat sa accesati elementul cu indexul {x}, dar lista are doar {len(lista)} elemente")
finally:
    #se executa indiferent ca s-a executat mai sus try sau except
    print("Se executa no matter what")

print("Ce frumos este afara")