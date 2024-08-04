# Can you write the program to find the sum of natural numbers we just wrote?

num = int(input("Enter the number: "))
total = 0
for i in range(0, num+1):
    total = total + i


print(f" Total is: {total}")
0