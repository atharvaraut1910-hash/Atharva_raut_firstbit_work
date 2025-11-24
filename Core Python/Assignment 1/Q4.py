# Write a program to enter P, T, R and calculate simple Interest.
# Take inputs from user
P = float(input("Enter Principal amount (P): "))
T = float(input("Enter Time period in years (T): "))
R = float(input("Enter Rate of interest (R) in percentage: "))

# Calculate Simple Interest
SI = (P * T * R) / 100
# Display result
print("Simple Interest is:", SI)
