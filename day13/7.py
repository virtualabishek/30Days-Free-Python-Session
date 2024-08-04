# Write a program to find the factorial of an integer entered by the user.

num = int(input("Enter the number: "))
fact = 1
for i in range(1, num+1):
    print(i)
    fact = fact * i

print(fact)