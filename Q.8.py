#Q.8  Explain range() in python 
## range() is a built-in function used to generate a sequence of numbers.
## Mostly used in for loops.

'''
Syntax:
range(start, stop, step)

Meaning:

start → beginning number (default 0)
stop → end number (exclusive)
step → how much to increase each time (default 1)

Use to find (Odd/Even numbers )
'''

#### imp 
for i in range(1,10,0):
    print(i)

"Values Error : (step = 0) must not be zero "

## Print no 1 to 10..
for i in range(1,11,1):
    if i % 2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')


























