# Write a program to enter P, T, R and calculate Compound Interest.
#  Take Inputs of P, T, R from user.
p = float(input("Enter the principal amount (P): "))
t = float(input("Enter the time in years (T): "))
r = float(input("Enter the rate of interest (R) in percentage: "))
# Calculate Compound Interest
CI = p * (1 + r/100) **t - p
# Display the result
print(f'The Compound Interest is: {CI}')