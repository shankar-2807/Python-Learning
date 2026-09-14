# Q.10  Explain pass / break / continue / else keyword in python looping 

'''
⭐ pass / break / continue / else in Python Looping (5 Marks Answer)

Python provides several control statements in loops to change the normal flow of execution. 
These include pass, break, continue, and the else clause in loops.'''

## pass

''' It is a null statement that does nothing.

Used when a statement is required syntactically but you don't want to write code yet.
Example:

for i in range(5):
    pass  # placeholder '''


## break

''' Immediately terminates the loop.

Control moves to the statement after the loop.
Example:

for i in range(10):
    if i == 5:
        break '''


## continue

''' Skips the current iteration and moves to the next one.

Remaining statements in the loop body are ignored for that iteration.
Example:

for i in range(5):
    if i == 2:
        continue '''


## else with loops

''' Executes only when the loop finishes normally (without break).

Commonly used in searching logic.
Example:

for i in range(3):
    print(i)
else:
    print("Loop completed")


These statements help control loop flow efficiently and are widely used to manage complex looping logic.

'''


for i in range(1,11):
    if i == 3:
        pass
    print(i)
else:
    print("Loop completed")


