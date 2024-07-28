""" Quadratic Equation and Formula Problem
WAP to use this formula. Take a input of a,b,c from user itself, and show the result
"""


# Taking input from users.

a = int(input("Enter a value of a: "))
b = int(input("Enter a value of b: "))
c = int(input("Enter a value of c: "))

# Intepreting formula]

x = (-b+((b**2 - 4*a*c)**0.5)/2*a)

xnew = ((-b+(b**2 - 4*a*c)** 0.5)/2*a)
xn2 =(-b+((b**2-4*a*c)**1/2))/2*a
print(x)
print(xnew)
print(xn2)