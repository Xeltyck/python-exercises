"""Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. 
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""

import string

counter = 0
listofnumbers = [str(number) for number in range(1000,3001)]
chosen = []
for number in listofnumbers:
    #print(number)
    for digit in number:
        #print(digit)
        if int(digit)%2==0 and int(digit) != 0:
            counter = counter+1
            if counter == 4: #Counter takes into account the number of digits. For instance 10-20 range, counter must be setup at 2.
                chosen.append(number)
        else:
                counter = 0
    #print(counter)

print(chosen)

"""

values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))"

"""

# More efficient alternative solution. 