# Q.9. Explain function and types of function

'''
⭐ What is a Function?

A block of reusable code that performs a specific task.
It runs only when called and helps reduce repetition.

Syntax:

def function_name():
    statements

⭐ Types of Functions in Python
1️⃣ Built-in Functions

Already provided by Python.
Examples: print(), len(), sum(), type()

2️⃣ User-defined Functions

Created by the programmer.

def greet():
    print("Hello!")

3️⃣ Functions with Parameters
def add(a, b):
    return a + b

4️⃣ Functions with Default Arguments
def greet(name="User"):
    print("Hello", name)

5️⃣ Return Type Functions
def square(x):
    return x*x

6️⃣ Lambda (Anonymous) Function

Small one-line functions.

square = lambda x: x*x


'''
# ###User Defined
# def greet():
#     print("Hello..!")

# greet()


# ###Function With Parameter
# def sum(a,b):
#     return a + b

# a=5
# b=3
# result = sum(a,b)
# print(result)

# ###Function with default Parameter
# def add(a=5,b=7):
#     c = a + b
#     print(c)

# add(3,8)

# ###Return Type Function

# def square(x):
#     return x * x

# squaree = square(3) 
# print(squaree)



################  Practice  ################


# def name ():    ##User defined
#     print('My Name is Shankar')
# name()

# def age(a,b):    # with parameter 
#     c = a+b
#     print(f'My age is {c}')
# age(20,2)

# def address(city='Pune',state='Maharashtra'):   ##Default parameter
#     print(f'i am leaving in {city},{state}')
# address('tuljapur','maharashtra')

# def pincode(x):   # with return
#     return x

# pincodeeee =pincode(413601)
# print(pincodeeee)





def shankar ():
    print('my name is shankar')

shankar()

def shanakr(age,salary):
    print(f'my age is {age } & salary is {salary}' )

shanakr(23,30000)


def address(city='tuljapur',state = 'maharashtra'):
    print(f'i am living in {city} state is {state}')

address(city='pune',state='maharashtra')




