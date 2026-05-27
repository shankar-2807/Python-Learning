#Calculator Project 

num1 = int(input("Enter num 1: "))
select_choice = (input("Enter Choice : +, -, /, *, %, ** : "))
num2 = int(input("Enter num 2: "))



if select_choice== '+' :
    print(num1 + num2)

elif select_choice== "-":
    print(num1 - num2)

elif select_choice=='/':
    print(num1 / num2)

elif select_choice== '*':
    print(num1 * num2)

elif select_choice== '%':
    print(num1 % num2)

elif select_choice== '**':
    print(num1 ** num2)
    
else:
    print("Enter Correct Choice..")

