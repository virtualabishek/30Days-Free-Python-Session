""" Suppose you are a university student and you need to pay 1536 dollars as your tuition fee.

    The college is offering a 10% discount on early payments.To solve this problem,

    Create a variable named fee and assign 1536 to it.
    Create another variable discount_percent and assign 10 to it.
    Compute the discount by using the formula (discount_percent / 100) * fee and assign it to the discount variable.
    Compute and print the fee you have to pay by subtracting discount from fee. """

fee = 1536
discount_percent = 10

discount = (discount_percent / 100) * fee
pay = fee - discount
print(pay)

