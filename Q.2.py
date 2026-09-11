# Q.2 Explain Data types in python

# several types of data types in python like (numeric,string,list , tuple, dictionary)

###Python has different types of data types used to store various types of values.
###The main data types are: Numeric, String, List, Tuple, Dictionary, Boolean.

# numeric:
'''
int = whole numbers(1,88,3285)
float = decimal number (2.87)
complex = real + imagary no (5+2j)  '''

num1 = 20
num2 = 88.56
num3 = 5+8j
print(type(num1),type(num2),type(num3))

###### Sequence Types
# string
'''
### A sequence of characters written inside single or double quotes.
character written in ('shankar',"shankar")'''

name = 'shankar'
surname = "mashalkar"
print(type(name),type(surname))

# list

'''
### 
# 1.Ordered
# 2.Mutable (changeable)
# 3.Allows duplicate values
# 4.Written in square brackets [ ]

li = ['shankar',99,2.87,{name:'shakar'}]'''

li = ['shankar',99,{'name':'shankar'}]
print(type(li))

# tuple

'''
###
#1. Ordered
#2. Immutable (cannot be changed)
#3. Written in parentheses ( )

list = ('shankar',99,2.87,{'name':'shakar'})'''

list = ('shankar',"mashalkar",{'name':'shakar'})
print(type(list))

# Dictionary (combination of key:value)

'''
###
#1. Stores data in key: value pairs
#2.Written in curly braces { }
#3. Keys must be unique

fullname = {'name':'shankar', 'surname':'mashalkar'}'''

fullname = {'name':'shankar', 'surname':'mashalkar','age':21}
print(type(fullname))
print(fullname)
fullname['sirname'] = 'mashalkarrrrrr'
print(fullname)


#################################################################################################
'''
Corrections in Your Notes
Your Writing	                               Correction
{name:'shakar'}	                        {'name': 'shakar'} (strings must be in quotes)
tuple written as list = ([...])	        correct name should be tuple = (...)
dictionary spelling "sirname"	        correct spelling: "surname"
string example (('shankar'))	        use "shankar" or 'shankar'

'''


