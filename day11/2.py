# Problem Description
# Write a program to find the factorial of an integer entered by the user.

# The factorial of a positive integer n is equal to 1 * 2 * 3 * ... * n. For example, the factorial of 4 is 1 * 2 * 3 * 4, which is 24.

# Get an integer input from the user and assign it to the variable n.
# Create a variable named total to store the result.
# Create another variable i with initial value 1.
# Run a while loop until the value of i becomes greater than n.
# Inside the loop multiply the value of i and total and assign the result to total.
# Increase the value of i in each iteration.
# Outside the loop, print the value of total.

n = int(input("Enter the number: "))
total = 1
i = 1

while(i<=n):
    total = total * i
    i = i + 1


print(total)