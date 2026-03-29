num = int(input("ENTER A NUMBER: "))

if(num > 0):
    if(num > 50):
       if(num > 100):
          print("Number greater than 100.")
       else:
          print("Number greater than 50 but less than 100.")
    else:
        print("Number greater then 0 but less than 50.")
else:
    print("number less than 0.") 


    