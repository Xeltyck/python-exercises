
# Question 36:

"""
Question:
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the values only.
"""
def function():
    dictionary = {}
    for x in range(1,21):
        dictionary[x] = x**2
    print(str(list(dictionary.values())))
function()
