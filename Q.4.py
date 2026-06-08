#Write a program to calculate the total cost of painting. The interior of building with four equal sized walls.
height = int(input("Enter a height of wall in meter: "))
width = int(input("Enter a width of wall in meter : "))

area_of_wall = (height * width)
print("area_of_wall: ",area_of_wall)

interior_of_building_size = (area_of_wall * 4)
print("interior_of_building_size: ",interior_of_building_size)

per_meter_cost = 20
Total_cost_of_painting_is = (interior_of_building_size * per_meter_cost)

print("Total cost of painting is: ",Total_cost_of_painting_is)


