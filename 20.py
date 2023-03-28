"""
### Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
"""

def divSeven(n):
    for x in range(0,n):
        if x%7==0:
            yield x

instance = divSeven(30)
print(instance)
print(list(instance))