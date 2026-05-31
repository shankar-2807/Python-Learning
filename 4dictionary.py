## Dictionary 

# it is denoted by { 'key':'value' } with key & value pairs
# Order : it is maintain values in insertion order.
# Mutuable : after creation you be change allowed (index is not allowed)
# Duplicate : Key must be unique : it can be allowed duplicate values


##Syntax  


Dictionary = {'name': 'shankar', 'age':22, 'surname':'shankar'}
print(Dictionary)
Dictionary.update({'surname':'mashalkar'})
print(Dictionary)
Dictionary['age'] = 23
print(Dictionary)

##Not allowed

Dictionary.append('sagar')
Dictionary.remove('mashalkar')


