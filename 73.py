"""
Question:

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
"""
array = [x for x in range(1,11)]
def binary_search(array,number):
    mid = round(len(array)//2)-1
    if array[mid] == number:
        print(number)
    elif array[mid] > number:
        if number in array[:mid]:
            print(number)
        else:
            print("Number is not on the list.")
    elif array[mid] < number:
        if number in array[mid:]:
            print(number)
        else:
            print("Number is not on the list.")
        
binary_search(array,5)