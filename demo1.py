#1. Structure: set(), {10,20,30}
s = set()
s = {10, 20, 30}
print(type(s))


#2. Type of data: Heterogenous , unique(value)
s1 = {10, 'a', 3.14, 10}
print(s1)

#3. Sequence :  (Unordered)
s = {10, 20, 'a', 3.14, 30, 'b'}
print(s)

#4. Changable : (Mutable) , not editable
# s[0]  # gives TypeError: set notb subscriptable

print(id(s))
s.add(88)
print(id(s))
print(s)
