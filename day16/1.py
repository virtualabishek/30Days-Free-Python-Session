#Write a program to continuously ask for integer input from the user using an infinite while loop.

#If the number is between 1 and 100 (inclusive), print the number.
#If the number is outside of this range, terminate the loop.
while True:
       num = int(input("enter the number:"))
       if 1 <= num <= 100:
              print(f"The number is :{num}")
       else:
              print("The number is outside of this range")
              break