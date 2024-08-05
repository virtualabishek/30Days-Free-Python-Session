# Write a program to print odd numbers between 1 and n (entered by the user).

num = int(input("Enter the number: "))

for n in range(1, num+1):
    if(n%2 !=0):
        print(n)
