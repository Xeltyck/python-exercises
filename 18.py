"""
Level 3

Question: A website requires the users to input username and password to register. Write a program to check the validity of password input by users. 
Following are the criteria for checking the password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma. 
Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

"""

import re

expressionRegexCheck = re.compile(r"[a-zA-Z0-9]")
especialRegexCheck = re.compile(r"[@#$]")
passwords = [x for x in (str(input("Enter yout paswords in a comma-separated sequence: "))).split(",")]
correctPasswords = []

for item in passwords:

    mo = expressionRegexCheck.search(item)
    me = especialRegexCheck.search(item)

    try:
        if mo.group() != 0 and me.group() != 0 and len(item) >= 6 and len(item) <= 12:
            correctPasswords.append(item)

    except:
        continue

print(",".join(correctPasswords))

"""
Web page's solution:

import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))

"""

