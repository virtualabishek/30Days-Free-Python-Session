# print sum of number:

num = int(input("Enter the number: "))

sum = 0

count = 1

while count<=num:
    sum = sum + count
    count = count + 1


print(sum)
# count = 1 + 1 => 2 + 1 => 3
# sum 1 + 0 = 1 -> 1 + 2 => 3 + 3 => 6
# 6 -> 1 + 2 + 3 + 1 => 4

#  4 -> 1,2,3,4,