#Even Number
n = int(input("Enter Number: "))
even = [i for i in range(1,n+1) if i % 2 == 0]
print(even)


#Odd Number
n = int(input("Enter Number: "))
odd = [i for i in range(1,n+1) if i % 2 != 0]
print(odd)
