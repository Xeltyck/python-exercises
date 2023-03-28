#Question 33:

"""
Question:
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
"""

def function(number):
    if number%2 == 0:
        print(f"The number {number} is an odd number.")
    else:
        print(f"The number {number} is not an odd number.")

function(10)