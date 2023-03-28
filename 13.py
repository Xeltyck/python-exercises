"""Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""



from queue import Empty
from tokenize import Number

Letters  = 0
number = 0
sentence  = str(input("Enter your sentence: "))

for character in sentence: 
    if character.isalpha() == True:
        Letters = Letters+1
    elif character.isdecimal() == True:
        number = number +1
    
    print(character)
print(f"Letters = {Letters}, Numbers = {number}")


