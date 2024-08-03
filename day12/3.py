# Write a program to find the sum until the user enters a negative number or 0.


# Get a float input from the user.
# Create a variable total with value 0.
# Loop as long as n is not negative and not 0.
# Inside the loop, add the value of n to total and take the float input again.
# Outside the loop, print total.

#// jaba samma user le -ve or 0 haldaina, user sanga input magna parxa, sum
#Write a program to find the sum until the user enters a negative number or 0.
num = float(input("Enter the number: "))

sum = 0

while num != 0:
    if num>0:
        sum = sum + num
        num = float(input("Enter the number again: "))

print(sum)
    