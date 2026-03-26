print('''
please choose operation from below:
      1.Addition
      2.Subtraction
      3.Multiplication
      4.Division
      5.Floor Division
      6.Modules
      7.Exponential
      8.Exit''')

ch = int (input("Enter choice:"))
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
if (ch == 1):
 print("Addition is:", num1 + num2)
elif(ch == 2):
 print(f'{num1} - {num2} = {num1 - num2}')

elif(ch == 3):
 print(f'{num1} * {num2} =  {num1 * num2}')

elif(ch == 4):
 print(f'{num1} / {num2} =  {num1 / num2}')

elif(ch == 5):
 print(f'{num1} // {num2} =  {num1 // num2}')

elif(ch == 6):
 print(f'{num1} % {num2} =  {num1 % num2}')

elif(ch == 7):
 print(f'{num1} ** {num2} =  {num1 ** num2}')


elif(ch == 8):
 print("Thank you for choosing us.")
else:
 print("Invalid input.")



