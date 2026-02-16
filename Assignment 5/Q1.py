#Write a program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_userid = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_userid and password == correct_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid credentials. Attempts left: {attempts}")
        else:
            print("Too many wrong attempts. Program terminated.")
