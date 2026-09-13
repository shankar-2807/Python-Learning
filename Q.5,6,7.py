# Q.5.6.7  Explain difference between while loop and for loop 

'''
What is a While Loop?

A while loop repeats a block of code as long as the condition is TRUE.
It is used when we don't know how many times the loop should run.

Example:
i = 1
while i <= 5:
    print(i)
    i += 1

⭐ What is a For Loop?

A for loop is used to iterate over a sequence (list, string, range).
It is used when we know how many times the loop should run.

Example:
for i in range(1, 6):
    print(i)

    


⭐ Difference Between While Loop and For Loop

(Write this table in notebook)

Feature	                      While Loop                                           	For Loop
Use Case	        When number of iterations is unknown	                   When iterations are known

Condition	           Runs based on a condition	                   Runs using a sequence (range, list, string)

Increment/
Decrement	           Must be written manually (i += 1)                    	Automatically handled by range()

Chances of 
infinite loop	        High if condition not updated	                               Very low

Syntax Style	           More flexible                                     	More structured & readable    

'''


i = 1

while i <= 5:
    print(i)

    i += 1


for i in range(1,6):
    print(i)