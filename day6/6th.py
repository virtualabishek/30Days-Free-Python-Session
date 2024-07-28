""" Problem Description

Suppose a, b, and c are three sides of a triangle. Then, the area of a triangle is given as:

s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5

Write a program to calculate the area of a triangle.

    Get three numeric inputs from the user and store them in variables a, b, and c.
    Compute semiperimeter s and then the area of the triangle using the above formula.
    Print the area. """


a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print(area)

