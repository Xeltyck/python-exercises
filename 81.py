
# Question 6

"""
Question:

Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

"""

import random

print(random.sample([x for x in range(100,201) if x%2 ==0],k=5))

