"""
Question:


Please write assert statements to verify that every number in the list [2,4,6,8] is even.



Hints:
Use "assert expression" to make assertion.
"""
numbers = [2,4,6,8,10]
for x in numbers:
    assert x%2 == 0, "Expected an even number."
    print(x)