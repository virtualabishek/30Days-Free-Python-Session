# Sum of Natural Numbers From 1 to n
def sumOfNatural(num):
    total = 0
    for i in range(1,num+1):
        total = total + i
    return total

num1 = int(input("Enter a number: "))
ans = sumOfNatural(num1)
print(ans)