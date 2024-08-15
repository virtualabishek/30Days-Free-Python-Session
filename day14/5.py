#we created an example to calculate the sum of numbers until the user enters 0.


# num - 1,2,3 -> 1+2+3+4 0-> 
num = int(input("Enter the number: "))

total = 0

while(num!=0):
    total = total + num
    num = int(input("Enter the number again: "))


print(total)

