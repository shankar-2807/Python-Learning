#WAP to add element in tuple.
tu = (10, 20, 30, 10, 40, 20, 40,)
list = list(tu)
tu = tuple(list)
print(list)

print(list.append([50, 80]))


tu[0] = 5
print(tu)

