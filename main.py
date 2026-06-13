from admin import Admin

def main():
    ch = 0
    while(ch != '2'):
        print('''---EMPLOYEE MANAGEMENT SYSTEM---
        1. Login
        2. Exit''')
        ch = input('Enter choice:')
        if(ch == '1'):
            uname = input('Enter username:')
            passw = input('Enter password:')
            if(uname == 'admin' and passw == '1234'):
                print('Logged in successful')
                Admin()
            else:
                print('Invalid credentials....')
        elif(ch == '2'):
            print('Thank you!')
        else:
            print('Invalid choice...')

if(__name__ == '__main__'):
    main()


