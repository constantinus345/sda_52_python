#pip install matplotlib
import matplotlib.pyplot as plt

#o simpla reprezentare grafica pe axele x si y
# x = [1,2,3,4,5]
# y = [62,72,82,92,102]
# plt.plot(x,y)
# plt.xlabel("Axa X")
# plt.ylabel("Axa Y")
# plt.title("Titlu ex_1")
# plt.show()

#Bar Chart
# x = ["Iasi", "Cluj", "Constanta", "Bacau"]
# y = [300000, 400000, 350000, 254000]
# plt.bar(x,y) #tipul de diagrama Bar Chart
# plt.xlabel("Orase")
# plt.ylabel("Populatie")
# plt.title("Populatia Oraselor Cool din Romania")
# plt.show()

#Scatter plot
x = [1,2,3,4,5]
y = [62,72,82,92,3]
plt.scatter(x,y)
plt.xlabel("Axa X")
plt.ylabel("Axa Y")
plt.title("Exemplu scatter plot SDA 52")
#plt.show()

folder = "B:/pyx/SDA/SDA_52"
# plt.savefig(f"{folder}/exemplu_scatter_1.png")
plt.savefig(f"{folder}/exemplu_scatter_1.pdf", format = "pdf")

