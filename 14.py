"""Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""

from queue import Empty
from tokenize import Number

Upper  = 0
Lower = 0
sentence  = str(input("Enter your sentence: "))

for character in sentence: 
    if character.isupper() == True:
        Upper = Upper+1
    elif character.islower() == True:
        Lower = Lower +1
    
    print(character)
print(f"Upper = {Upper}, Lower = {Lower}")
