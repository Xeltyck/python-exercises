"""
Question:

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john
"""
email = str(input("Enter the email: "))
name = []
for letter in email:
    if letter != "@":
        name.append(letter)
    else:
        break
print("".join(name))

"Using REGEX:"

"""
Solution:
import re
emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print (r2.group(1))
"""