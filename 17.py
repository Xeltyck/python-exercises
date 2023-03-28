"""Question: Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following: D 100 W 200

D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console input."""

import re

log  = input("Enter the transaction log: ")
depositRegex = re.compile(r'D\s\d+') # Finds Deposit pattern.
withdrawalsRegex = re.compile(r'W\s\d+') # Finds withdrawal pattern.

depositlist = depositRegex.findall(log) # Creates a list with the deposits, including the letter D.
withdrawalslist = withdrawalsRegex.findall(log) # Creates a list with the withdrawals, including the letter W.

justNumberRegex = re.compile(r'\d+') # Takes the numbers from any string. For this particular case, both lists (gottta convert them to strings first.)

#print(depositlist)
#print(withdrawalslist)

# Deposits process:
totalDeposit = 0 
depositsString = ",".join(depositlist)
#print(depositsString)
depositNumber = justNumberRegex.findall(depositsString)
#print(depositNumber)
for item in depositNumber:
    totalDeposit = totalDeposit + int(item)
print(f"The amount to be deposited is: {totalDeposit}")

# Withdrawal process:
totalWithdrawal = 0
withdrawalString = ",".join(withdrawalslist)
#print(withdrawalString)
withdrawalNumber = justNumberRegex.findall(withdrawalString)
#print(withdrawalNumber)
for item in withdrawalNumber:
    totalWithdrawal = totalWithdrawal + int(item)
print(f"The amount to be withdrawn is: {totalWithdrawal}")

currentBalance = totalDeposit - totalWithdrawal
if currentBalance >= 0:
    print(f"The current balance on this account is: {currentBalance} $")

else:

    print("Is not possible to continue with the operation due to insufficient funds.")

"""
Web page's solution: (Input is not a one liner, but one after another. W - number or D - number, subsequently.)

etAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)

"""