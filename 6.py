"""Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] 
Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. 
Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24"""

from cmath import sqrt
from email.policy import strict
from queue import Empty

# sqrt((2*C*(List[index]))/(H))

C = 50
H = 30
List = []
List2 = []
valuesOfD = str(input("Enter the D values separeted by a comma: "))

#Separamos los valores del String usando el método de ingreso. 
List = valuesOfD.split(",")

#Convertimos los valores de la lista de str a int. 
for index in range(0,(len(List))):
   List[index] = int(List[index])

#Se imprimen los resultados en la lista 2.

for value in List:
    #Usar (Expression).real me permite elminar los resultados complejos. 
    List2.append(int((sqrt((2*C*(value))/(H))).real))

#Para usar join, debo convertir los números a str nuevamente.

for value in range(0,len(List2)):
    List2[value] = str(List2[value])

results = ",".join(List2)
print(results)

"""
Page's answer:

c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

"""
