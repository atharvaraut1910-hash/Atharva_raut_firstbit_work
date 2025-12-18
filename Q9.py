# Program to calculate grade from 5 subject marks

# Input marks
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

# Display result
print("Total Marks =", total)
print("Percentage =", percentage)

# Decide grade
if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 40:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")
