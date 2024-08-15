#Write a program to find the first even number greater than 10 in a given list.

#Use a for loop to iterate through the given list of numbers.
#If the number is 10 or below, use the continue statement to skip that number.
#If the number is greater than 10 and even, print that number and exit the loop with break.
num = int(input("enter the number :"))
for i in range(10,num+1):
    if(i<=10):
        continue
    if(i>10 and i%2 == 0):
        print(i)