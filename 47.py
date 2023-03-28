
# Question 47:

"""
Question:
Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""

list1 = [x for x in range(1,11)]
mapped = list(map(lambda x : x**2,list1))
filtered = list(filter(lambda x: x%2==0,mapped))
print(filtered)