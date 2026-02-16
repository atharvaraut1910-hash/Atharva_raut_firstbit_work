# Program to check correct UserID and Password

correct_userid = "admin"
correct_password = "12345"

userid = input("Enter UserID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    print("Login Successful!")
else:
    print("Invalid UserID or Password!")
