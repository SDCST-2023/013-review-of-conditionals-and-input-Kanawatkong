"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

print("Enter 2 number")
x = str(input("First number"))
y = str(input("Second number"))
z = input("if one of the numbers is the hypotenuse of a right triangle y/n")
if z == "n":
    print(math.sqrt(x**2 + y**2))
else:
    if x > y:
        print(math.sqrt(x**2 - y**2))
    else:
        print(math.sqrt(y**2 - x**2))
    