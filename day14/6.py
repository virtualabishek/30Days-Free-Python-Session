#we created an example to calculate the sum of numbers until the user enters 0.


# num - 1,2,3 -> 1+2+3+4 0-> 
num = int(input("Enter the number: "))

total = 0

while True:
    num = int(input("Enter the number again: "))
    if(num==0):
        break
        total = total + num



print(total)

