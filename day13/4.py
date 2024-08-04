# Problem Description
# Write a program to print a sequence of numbers.

# Get an integer input from the user and store it in a variable: number.
# Using a for loop, print the sequence of numbers from 1 to number (number exclusive).

"""
n, user-> int, input
4 1,2,3,4


"""

number = int(input("Enter the number: "))
for i in range(1, number):
    print(i)