
# Question 51:
"""
Define a class named American and its subclass NewYorker.
"""

class American():
    
    def printNationality(self,nationality):
        print(nationality)

class NewYorker(American):
    pass

jeff = NewYorker()
jeff.printNationality("American")