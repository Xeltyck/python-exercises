from queue import Empty


Number = 8
Dictionary = {}
for X in range(1,(Number+1)):
    Dictionary.setdefault(X, X*X)

print(Dictionary)
