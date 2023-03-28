from tokenize import Number
from typing import List


Numbers = str(input("Enter numeric sequence separated by a comma: "))
print(Numbers)
List = Numbers.split(",")
Tpl = tuple(List)

print(List,Tpl)