#Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user):

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

area_of_rectangle = length * breadth
perimeter_of_rectangle = 2 * (length + breadth)

print('Rectangle: ')
print("Area =", area_of_rectangle)
print("Perimeter =", perimeter_of_rectangle)



