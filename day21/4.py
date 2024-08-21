# roblem Description
# Assign the dictionary below to a variable named prices.

# {'apple': 2.5, 'kiwi': 3.4}
# Then,

# Change the value of the 'apple' key to 3.5.
# Print the dictionary.
# Add an item (key: 'banana', value: 3) to the dictionary.
# Print the dictionary again.

prices = {'apple': 2.5, 'kiwi': 3.4};
prices['apple'] = 3.5;
prices['banana'] = 3;
del prices['kiwi']
print(prices)

del prices
print(prices)
