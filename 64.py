"""
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55
"""
result = 0
number = int(input("Enter an integer number: "))
for x in range(1,number+1):
    result = x/(x+1) + result
print(round(result,3))