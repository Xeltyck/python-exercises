
# Question 7

"""
Question:

Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints:
Use random.sample() to generate a list of random values.


"""

import random

print(random.sample([x for x in range(1,1000) if x%7==0 and x%5==0],k=5))

