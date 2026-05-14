##1. Operators are universal
#2. perform operation on object.
#3. We add new functionality to the operator.
 #+ : __add__   , __sub__  ,  __mul__  , __truediv__  ,  __eq__ = == ,  __ne__ = != 
 #  __it__ = <  ,  __gt__ = .  , __le__ = <=  , __ge__  = >=  ,  _-str__ = str()


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self, other):
        s = self.s + other.s
        m = s // 60
        s = s % 60
        m = m + self.m + other.m
        h = m // 60
        m = m % 60
        h = h + self.h + other.h

        return f'{h}:{m}:{s}'

t1 = Time(10, 20, 30)
t2=  Time(12, 45, 35)

res = t1 + t2
print(res)  


