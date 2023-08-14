""" 
    Assignment:

    Write a program that does the following in order:
    1. Asks the user to enter a number “x”
    2. Asks the user to enter a number “y”
    3. Prints out number “x”, raised to the power “y”.
    4. Prints out the log (base 2) of “x”.

"""
#import packages
import numpy


# create variables
x = int(input("Please enter a whole number for 'x': "))
y = int(input("Please enter a whole number for 'y': "))

# Output 1 - display x to the power of y
print(f"x to the power of y: {x**y}")