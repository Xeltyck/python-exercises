"""
Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
from operator import itemgetter

dictionary = {}
sentence = str(input("Enter the sentence according to the  structured format: "))
wordList = sentence.split(" ")
for word in wordList:
    dictionary.setdefault(word,0)
    dictionary[word] = dictionary[word]+1
dictionary = sorted(dictionary.items()) # This line saves me the two next  lines. 
#listItems = list(dictionary.items())
#sortedDictionary = sorted(listItems,key=itemgetter(0)) 

for item in dictionary:
    print(item[0],":",item[1])


