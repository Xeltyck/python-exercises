
#Question 44:
"""
Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)
"""

tup = (1,2,3,4,5,6,7,8,9,10)
list = []
for item in tup:
    if item%2==0:
        list.append(item)
print(tuple(list))