# Problem Description

# You are given a string to indicate the color of the traffic light. Write a program to display a warning signal if the traffic light is red.

#     Write an if statement that checks if the user entered red.
#     Inside the if block, print "The red light is on."
#     In another line, print "Stop the vehicle.".
#     Outside the if clause, print "Have a good day!".

trafficSignal = input("Enter the signal: ")

if trafficSignal == "red":
    print("The red light is on.")
    print("Stop the vehicle.")

print("Have a good day!")
