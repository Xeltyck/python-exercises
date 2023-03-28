"""Question: Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. 
Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,9,25,49,81"""

numbers = str(input("Enter a comma-separated sequence of numbers: "))
list = [number for number in numbers.split(",")]
square = []
for number in list:
    if int(number)%2 != 0:
        square.append(str(int(number)*int(number)))
print(",".join(square))

"""
Web page's solution

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))

"""