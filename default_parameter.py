#1. Assign value to parameter in the defination OF FUNCTION
#2. Assign default argument from right to left 
#3. we can achieve option parameter concept

def sum(num1, num2, num3 = 0, num4 = 0):
    return num1 + num2 + num3 + num4

print(sum(1, 2, 3, 4,))
print(sum(10, 20, 30))
print(sum(45, 85))



