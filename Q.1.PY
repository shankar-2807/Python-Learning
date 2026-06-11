# Write a function which we pass parameter and print factors of a given number.
# for eg : factor of 12 : 1,2,3,4,5,12

n = int(input("Enter a number:"))
def print_factors(n):
    print(f"Factors of {n}:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

print_factors(n)

