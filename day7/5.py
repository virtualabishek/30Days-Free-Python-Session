""" Problem Description

Write a program to print True if the number is divisible by 5. If not, print False.

    Get an integer input from the user.
    Check if the input is divisible by 5 or not.
    If it's divisible by 5, print True.
    If not, print False. """

num = int(input("Enter a number to check whether it is dividible by 5 or not: "))

print(num%5 == 0)