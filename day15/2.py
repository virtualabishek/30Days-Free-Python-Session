# Write a program to print odd numbers between 1 and n, where n is a positive integer entered by the user.
num = int(input("Enter the number: "))
for i in range(1,num+1):
    if(i%2 == 0):
        continue
    print(i)