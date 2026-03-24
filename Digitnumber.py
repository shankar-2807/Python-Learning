#WAp to seperate digits from Three digitnumber
num = int(input("Enter Number:"))
num = 789

d1 = num % 10
# print(d1)
num = num // 10
# print(num)
d2 = num % 10
print(d2)
num = num // 10
# print(num)
d3 = num % 10
# print(d3)

reversed_digit = (d1 * 100) + (d2 * 10) +(d3)
print(f'reversed digit: {reversed_digit}')


