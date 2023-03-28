"""
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.
"""

l1 = [5,6,77,45,22,12,24]
filtered_list = filter(lambda x: x%2!=0, l1)
print(list(filtered_list))