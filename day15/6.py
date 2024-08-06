#Write a program to find the multiplication table of an integer (entered by the user) from 6 to 9.

num = int(input("Enter the number: "))
product = 1;
for i in range(6,10):
    product = num * i
    print(f"{num} * {i} = {product}")
