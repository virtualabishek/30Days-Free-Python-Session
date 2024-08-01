## Write a program to check whether number is even or odd.

number = int(input("Enter the number: "))

if(number % 2 == 0):
    print("The number is even.")
elif(number % 2 !=0):
    print("The number is odd.")
else:
    print("The number is incorrect.")

