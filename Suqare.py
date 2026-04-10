def Square(n):
    sqr = {}
    for i in range(1, n+1):
        sqr[i] = i * i
    return sqr

n = int(input("Enter a number : "))
Squares = Square(n)
print(Squares)





