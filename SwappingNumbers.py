#Using 3rd varialbe
num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
num3 = 0
print(f'Before Swapping- num1:{num1} & num2:{num2}')
num3 = num2
num2 = num1
num1 = num3
print(f'After Swapping- num1:{num1} & num2:{num2}')

num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
print(f'Before Swapping- num1:{num1} & num2:{num2}')

num1, num2 = num2, num1
print(f'After Swapping- num1:{num1} & num2:{num2}')

#WAp to seperate digits from Three digitnumber
num = int(input("Enter Number:"))
num = 534
d1 = num % 10
print(d1)
num = num


