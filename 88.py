"""
Question:

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.
"""
from operator import itemgetter
l1 = [12,24,35,70,88,120,155]
"""
numbers = [12,35,155]
for number in numbers:
    l1.remove(number)
print(l1)
"""
#enumerate is sugested because it enumerates the items first, abd then that enumeration can be used to delete the items. Not possible via indexation because every
#tieme a loop excecutes and deletes an item, the indexes order change.

for x,y in enumerate(l1):
    if x == 0 or x == 2 or x == 4 or x == 6:
        l1.remove(y)
print(l1)