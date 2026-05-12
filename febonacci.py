n = int(input("Enter number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci sequence:", a)
else:
    print("Fibonacci sequence:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


