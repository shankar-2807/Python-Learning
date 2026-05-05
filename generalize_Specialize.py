li = [10, 20, 30, 40]

try:
    val = int(input("Enter value:"))
    print(li.index(val))

#Specialized exception handling
except ValueError:
    print("Value error occured.")


except IndexError as e:
    print("Index error:", e)

#Generalized exception handling
except Exception as e:
    print("Error:", e)

print('Program excuted successfully.')

#Handle all specilized exception of list methods