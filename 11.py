"""Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: 
Assume the data is input by console."""

from queue import Empty


sequence = str(input())
numbers = [number for number in sequence.split(",")]
divisible = []

# Se puede usar binarios en str y pasarlos a int haciendo uso de int("numero binario",base 2 en este caso)

print(numbers)

for number in numbers:
    if (int(number,2)%5 == 0):
        divisible.append(number)

print(",".join(divisible))