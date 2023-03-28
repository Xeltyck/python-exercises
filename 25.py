"""
Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later
"""

from unicodedata import name


class Dog():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def giveInformation(self):
        print(f"My name is {self.name} and my age is {self.age}.")

max = Dog("Max",15)
max.giveInformation()