# WAP to calculate percentagee based on best of 5
# Take inputs from user
m1= int(input("Enter marks for sub1: "))
m2= int(input("Enter marks for sub2: "))
m3= int(input("Enter marks for sub3: "))
m4= int(input("Enter marks for sub4: "))
m5= int(input("Enter marks for sub5: "))

# perform addition
total = m1 + m2 + m3 + m4 + m5


# calculate percentage
percentage = (total / 500) * 100 
print("percentage = ",percentage) 