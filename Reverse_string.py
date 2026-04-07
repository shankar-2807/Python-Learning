def rev_str1(str):
    str = "Hello World!"
    rev_str = ' '
    for i in range(len(str)-1 , -1 ,-1):
        rev_str = rev_str + str[i]
    return rev_str

str = 'Hello World!'
print("Reversed string: ", rev_str1(str))






# For example 

str = "Hello  World!"
str2 = str[::-1]
print(str2)

