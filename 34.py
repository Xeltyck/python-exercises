
# Question 35:
"""
Question:
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
"""
def function():
    dictionary = {}
    for x in range(1,21):
        dictionary[x] = x**2
    print(dictionary)
function()