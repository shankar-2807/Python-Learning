def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):  
        total = total + i
    return total

n = int(input("Enter a number: "))

result = sum_of_odds(n)
print("sum of odd number: ", result)

