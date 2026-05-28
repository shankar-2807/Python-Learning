num = int(input('Enter the age: '))

if num <= 0:
    print("Enter correct age..")
elif num >= 18 and num <=100:
    print("You can Vote..")
elif num > 100:
    print('Age is greater than 100..')
else:
    print('You cannot vote..')

