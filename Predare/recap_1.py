var_1 = 7
print(var_1)

var_2 = 4.5
print(var_2, type(var_2)) #float- adica numar rational, cu virgula

var_3 = "Text 1 blac 43543&(^&*"
print(var_3)
print(type(var_3)) #str = string = text

var_4 = 'Text v2'
var_5 = """Aici 
text pe 
mai multe linii
Wow
"""
print(var_5)

var_6 = True
var_7 = False
print(var_6, var_7, type(var_6)) #bool = tip de date logic True/False

var_complex = 8 + 2j
print(type(var_complex))
print("Partea reala a numarului complex = ", var_complex.real)

snake_case = ""
CamelCase = ''
altaVariabila = """"""

var_1 :int = 7
print(var_1, type(var_1))
var_1 :str = 8
print(var_1, type(var_1))
var_1 :bool = "Ceva"
print(var_1, type(var_1))

print(4*3.2)
print("8ceva" * 3)
print("8" * 3.2)

print(2**3)
print(17 // 7)
print(17 % 7)

assignment_x = 18

print(17 == (16+3))
print(17 < 8)
print(17 <= 8)
print(17 != 19)

num_1 = 7
# num_1 = num_1 +3
# print(num_1) #Ctrl+/ face randul comentat

"""
num_1 = num_1 +3
print(num_1) 
"""

num_1 += 3
print(num_1)

var_1 = 7 > 8 #False
print(var_1)
var_2 = 7 >6 #True

#and, or, not
print(var_1 and var_2) #True and False = False, False and False = False, True and True = True
print(var_1 or var_2) #True or False = True
print(not var_2)

#in, not in
print("ceva" in "Am ceva frumos") #True
print("ceva" in "Am Ceva frumos") #False, pentru ca avem Ceva

var_1 = 5
Var_1 = 7
print(var_1) #sunt doua variabile diferite pentru ca difera case-ul

# print(3 in 23454) eroare, in nu functioneaza cu integer sau float, ci doar cu str (sau alte tipuri de date mai avansate)

