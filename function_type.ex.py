#write a program to calculate digits count in number using function 
def digitcount(num):
    count = 0
    while(num > 0):
        count += 1
        num = num //10
    return count

number = int(input("Enter number to check count of digits:"))
print("Digits:",digitcount(number))



