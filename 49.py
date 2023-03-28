
# Question 49:
"""
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""
list1 = [x for x in range(1,21)]
mapped = list(map(lambda x: x**2,list1))
print(mapped)