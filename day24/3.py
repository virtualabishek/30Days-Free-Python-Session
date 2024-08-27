# Program to check if number is prime or not
# WAP to print Prime Numbers Between 50 and 100
# 50 - 100 -> range(50,101) 

# Check whether a number enter by user is a prime or not.

number = int(input("Enter the number: ")) # 7 
primeNumber = True
for i in range(2, number): # ->2,3,4,5,6
    if(number%i)==0: # 7%2, 7%3, 7%4, 7%5 .... 7%7 ==0
        primeNumber = False
        break
if primeNumber:
    print("The Number is prime")
else:
    print("The number is not prime.")




