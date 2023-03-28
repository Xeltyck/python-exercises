
# Question 45:
"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""

string = str(input("Enter the string sequence: "))
if string == "yes" or string == "YES" or string == "Yes":
    print("Yes")
else:
    print("No")