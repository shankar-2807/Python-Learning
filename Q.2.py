number = int(input("Enter a 3-digit number: "))

if 100 <= number <= 999:
    first = number // 100
    second = (number // 10) % 10
    third = number % 10

    if first == 2 * second and first * 2 == third :
        print("Yes, you have done it")
    else:
        print("Please try next time")
else:
    print("Invalid input. Please enter a 3-digit number.")

    
    