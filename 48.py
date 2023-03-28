
# Question 48:
"""
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""
list1 = [x for x in range(1,21)]
filtered = list(filter(lambda x: x%2==0,list1))
print(filtered)