### Map:
#1. Used to perform iterable operations
#syntax:
#map(function, data)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#By lambda function
res = list(map(lambda x: x * x, data))
print(res)

#By user defined function
def sq(i):
    return i * i

res = list(map(sq, data))
print(res)

