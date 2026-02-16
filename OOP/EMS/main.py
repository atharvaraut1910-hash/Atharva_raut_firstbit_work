from admin import Admin

def main():
    ch = 0
    while(ch != '2'):
        print('''Please select option from below:
              1.Login
              2.Exit
              ''')
        ch = input('Enter choise:')
        if(ch == '1'):
            uid = 'admin'
            passw = '1234'
            uname = input('Enter username:')
            password = input('Enter password:')
            if(uid == uname.lower() and passw == password):
                print('Logged in successful...')
                ad = Admin()

            else:
                print('Invalid credentials...')
        elif(ch == '2'):
            print('Thank you for choosing us!')
        else:
            print('Invalid choise...')

main()