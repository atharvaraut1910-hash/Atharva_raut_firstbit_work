import random

# Correct credentials
correct_userid = "admin"
correct_password = "12345"

# Step 1: Get input
userid = input("Enter UserID: ")
password = input("Enter Password: ")

# Step 2: Verify credentials
if userid == correct_userid and password == correct_password:
    # Step 3: Generate 4-digit random number
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    # Step 4: Ask user to re-enter captcha
    user_captcha = int(input("Enter the above number: "))

    # Step 5: Check captcha
    if user_captcha == captcha:
        print("Login Successful! ✔")
    else:
        print("Captcha Failed! ❌")
else:
    print("Invalid UserID or Password! ❌")
