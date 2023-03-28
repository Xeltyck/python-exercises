"""
Question: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. 
The tuples are input by console. The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: Then sort by score. 
The priority is that name > age > score. 

If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the program should be: 
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use itemgetter to enable multiple sort keys.

"""

from operator import itemgetter
from queue import Empty

list = []
sortedTuples = []
while True:

    log = input("enter the values according to the valid format: ")

    if log == "":
        break

    else:
        items = log.split(",")
        dictionary = {"Name":items[0],"Age":items[1],"Height":items[2]}
        list.append(dictionary)

sortedList = sorted(list,key=itemgetter("Name","Age","Height"))

for item in sortedList:
    sortedTuples.append(tuple(item.values()))
    
print(sortedTuples)