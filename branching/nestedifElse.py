gender = input("Enter gender(M/F):")
age = int(input("Enter age:"))

if(gender == "M"):
    if(age >= 21):
        print("Eligible for marriage.")
    else:
        print("Pehle Padh Le Bhai.")
else:
    if(age >= 18):
        print("Eligible for mrraige.")
    else:
        print("pahle padh le bahan.")
        