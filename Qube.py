def Cube(n):
    cube = {}
    for i in range(1, n+1):
        cube[i] = i ** 3
    return cube


n = int(input("Enter a number : "))
Cubes = Cube(n)
print(Cubes)




