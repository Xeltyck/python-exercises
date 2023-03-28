
# Question 53:
"""
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 
"""

class Rectangle():
    
    def __init__(self,l,w):
        self.length = l
        self.width = w
    
    def compute_area(self):
        print(self.length*self.width)

rectangle1 = Rectangle(5,10)
rectangle1.compute_area()