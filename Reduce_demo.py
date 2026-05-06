###Reduce:
#1. Performs operation on iterable with return and value
#2. Need to import

#Syntax
#Reduce(function, iterable)
from functools import reduce
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = reduce(lambda x,y : x+y , data)
print(res)

res = reduce(lambda x,y : x*y , data)
print(res)

res = reduce(lambda x,y : x-y , data)
print(res)

res = reduce(lambda x,y : x/y , data)
print(res)

