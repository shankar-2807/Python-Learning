## With recursive Function ##


#### define firstc n number factorial (multiplication)...

def factorial(n):
    if n == 1 or n== 0:
        return 1
    else:
        return(n * factorial(n-1))

num = factorial(int(input('Enter a factorial number: '))) 
print(num)

