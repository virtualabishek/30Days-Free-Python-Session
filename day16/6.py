#  Create a function to print a person's information.

# Step 1

# Create a function named display_info().
# This function must accept two arguments: name and location.
# Print name and location in two separate lines.
# Step 2

# Outside of the function:

# Get a string input from the user and assign it to the country variable.
# Call the display_info() with arguments: the "Taylor" string and the country variable, respectively.

def display_info(name, location):
    print(name)
    print(location)

country = input("Enter your country: ")

display_info("Taylor", country)