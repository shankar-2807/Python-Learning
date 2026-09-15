# Q.11. Explain recursive function. 

''' A recursive function is a function that calls itself inside its own body.
It is used for solving problems that can be divided into smaller sub-problems of the same type.
Every recursive function must have a base condition to stop infinite calling.
Python uses a call stack to keep track of recursive calls.
Recursion is commonly used in mathematical operations like factorial, Fibonacci series, trees, and searching. '''

# Example 1: Factorial using recursion

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))   # Output: 120


# Example 2: Sum of numbers 1 to n
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))   # Output: 15


def fact (n):
    if n ==1 :
        return 1
    return n * fact(n-1)

print(fact(5))