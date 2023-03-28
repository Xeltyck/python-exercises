"""Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""

number = str(input("Enter number: "))
sum = int(number) + int(number*2) + int(number*3) + int(number*4)  
print(sum)

