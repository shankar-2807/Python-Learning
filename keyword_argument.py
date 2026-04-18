#1. Assign value to parameter in function calling
#2. keyword using for assigning must be from the defination
#3. Assign value from right to left 
#4. we can ignore positional parameter concept

def emp(eid, ename, esal, edept):
    print("EID:", eid)
    print("ENAME:", ename)
    print("SALARY:", esal)
    print("DEPT:", edept)

emp(ename = "Shankar", eid = 101, esal= 400000, edept = "Trainer")



