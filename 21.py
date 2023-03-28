""" 
### Question 21
Level 3

Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""
import math
xAxix = 0
yAxix = 0
while True:
    log = input("Enter the sentence according to the accepted format: ")
    if log == "":
        break
    else:
        list = log.split(" ")
        if list[0] == "UP":
            yAxix = yAxix + int(list[1])
        elif list[0] == "DOWN":
            yAxix = yAxix - int(list[1])
        elif list[0] == "LEFT":
            xAxix = xAxix - int(list[1])
        elif list[0] == "RIGHT":
            xAxix = xAxix + int(list[1])

distance = math.sqrt(((abs(xAxix))**2)+((abs(yAxix))**2))
print(distance)
