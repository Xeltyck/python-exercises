"""
Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.
"""


class Error():

    def __init__(self, message):
        self.message = message

error = Error("Something happened, Ups.")