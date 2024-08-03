# Write a program to find the sum until the user enters a negative number or 0.

num = float(input("Enter the number: "))

sum = 0

while True:
    num = float(input("Enter the number: "))
    if(num<=0):
        break
    sum = sum + num
print(sum)