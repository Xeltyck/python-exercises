
# Question 46:
"""
Question:
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
"""
list1 = [x for x in range(1,11)]
mappedList = list(map(lambda x: x**2,list1))
print(mappedList)