"""
Question:

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def generator(n):
    i = 0
    while i < n+1:
        if i%2==0 or i==0:
            yield(i)
        i = i+1

lista = [str(x) for x in generator(20)]
print(",".join(lista))

