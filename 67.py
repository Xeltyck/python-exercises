"""
The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13

"""
flist = []
def fibonacci(x):
    
    if x == 0:
        return 0
    elif x ==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

number = int(input("Enter a number to calculate the sequence: "))
for number in range(0,number+1):
    flist.append(str(fibonacci(number)))
print(",".join(flist))

# flist = [fibonacci(x) for x in range(0,x+1)] Another way to create the list.