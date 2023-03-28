
# Question 52:
"""
Question:
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
"""
import math
class Circle():
    
    def __init__(self,radius):
        self.radius = radius
    
    def computeArea(self):
        print((3.14)*(self.radius**2))

circulo = Circle(5)
circulo.computeArea()