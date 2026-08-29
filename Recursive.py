## With recursive Function ##

####addition of first n number 

def sum_n(n):
    if n == 0:
        return 0
    else:
        return (n + sum_n(n-1))

num = sum_n(int(input("Enter a number: ")))  
print(num)




# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return(n * factorial(n-1))
    
# print(factorial(5))

