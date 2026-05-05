#Syntax:
#try:
    #Wghere we feel exception will occur

#except:
    #Will execute when exception occured in try block

try:
    num = int(input("Enter number: "))
    print("Number is:", num)
except:
    print("Invalid input.")

print("Program executed.")