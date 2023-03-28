
# Question 40:
"""
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list.
"""

def function():
    list = []
    for element in range(1,21):
        list.append(element**2)
    print(list[-5:])
function()