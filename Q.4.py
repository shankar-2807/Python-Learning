# Q.4 what is Decision Making in Python

'''
Decision making in Python allows a program to choose different actions based on conditions.
It is used when you want to perform certain code only if a specific condition is true.
Python provides decision-making statements like if, if-else, and if-elif-else.
These statements evaluate expressions and execute code based on True/False results.
Decision making helps programs behave logically, based on user input or program conditions.  '''

# age = 18

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")


marks = int(input("Enter marks(0 to 100): "))

if marks < 0:
    print("Student failed with minus marks")
elif marks<35 and marks>=0:
    print("Student Falied")
elif marks>=90 and marks<=100:
    print("Student pass with A+ grade")
elif marks > 100 :
    print("Enter valid marks less than 100")
elif marks >=35:
    print("Student Pass")
else:
    print("invalid choice")



