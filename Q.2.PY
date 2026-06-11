# Write a program to find factorial of given number using recursion

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("enter a factor: "))
print(factorial(n))

