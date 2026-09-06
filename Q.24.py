### Q.24  Explain abstraction / encapsulation / inheritance / polymorphism.

class student():
    def __init__(self,id,name,branch):
        self.i = id
        self.n = name
        self.b = branch

    def __str__(self):
        return f"the student {self.n} is take the admission of {self.b}"
    

s1 = student(1,'shankar','python')
print(s1)



# class SStudent():
#     def __init__(self,id,name,branch):
#         self.i = id
#         self.n = name
#         self.b = branch

#         print(f'the student {name} is take the admission of {branch}')
    

# s2 =SStudent(1,'shankar','python')




