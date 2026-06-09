# Write a program to calculate the sum of following series where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

n = int(input("Enter the value of N: "))
sum = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    sum = sum + (i / fact)

print("The sum of the series is:", sum)

