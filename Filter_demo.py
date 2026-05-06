### Filter:
#1. Used to filter values from iterables
#syntax:
#filter(function, iterables)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = tuple(filter(lambda x : x % 2 == 0, data))
print(res)


