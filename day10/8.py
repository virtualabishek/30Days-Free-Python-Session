# Write a program to print a set of information for a fixed number of iterations.

# Get an integer input from the user and store it in variable n.
# Create a variable i with the initial value 0.
# Start a while loop that will run as long as i is less than n.
# In each iteration, print the current value of n, the current value of i, and the separator ###.
# Increase the value of i by 1 in each iteration.
# Decrease the value of n by 1 in each iteration.
# Outside the while loop, print The loop ends.

n = int(input("Enter the number: "))
i = 0
while(i<n):
    print(n)
    print(i)
    print(f"###")
    i = i + 1
    n = n -1


