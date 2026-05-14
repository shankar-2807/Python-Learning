### function / method overloding ( compile time polymorphism).
# same name of functon but different no. of parameter for multiple functon.
# Time of function call, automatically decided which function will execute(basis on numbers of parameter).
#### NOT WORKING IN PYTHON
# override recent function to previous function (interpreter).

#Solution (variable length of parameter/ args).

def sum(n1, n2):
    return n1 + n2

def sum(n1, n2, n3):
    return n1 + n2 + n3

print(sum(10, 20, 30))

# print(sum(10, 20))  # gives error