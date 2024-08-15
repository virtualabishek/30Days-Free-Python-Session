# Write a program that prints numbers if they're both the multiple of 3 and 5.

"""
n = 30

output = > 15,30

"""


num = int(input("Enter the number: "))

for i in range(1,num+1):
    if(i%3==0 and i%5==0):
        print(i)
