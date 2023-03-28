
# Question 54:

"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
Both classes have an area function which can print the area of the shape where Shape's area is 0 by default.
"""

class Shape():
    
    def __init__(self):
        pass
    def print_area(self):
        self.area = 0
        return self.area

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def print_area(self):
        print(self.length**2)
        

square1 = Square(5)
square1.print_area()

    
    