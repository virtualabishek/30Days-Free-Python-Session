#Write a program to check whether a number is odd or even by creating a function.

def checkNum(a):
    if(a%2 == 0):
        return True
    else:
        return False

num = int(input("Enter the number: "))
result = checkNum(num)

if result:
    print("The number is even.")
else:
    print("The number is odd")