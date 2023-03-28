
# Question 38:

"""
Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
"""

def function():
    list = []
    for number in range(1,21):
        list.append(number**2)
    print(list)
    
function()