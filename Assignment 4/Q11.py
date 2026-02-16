# Program to check Strong Number

n = int(input("Enter a number: "))
original = n
sum_fact = 0

# Function to calculate factorial of a digit
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Calculate sum of factorials of digits
while n > 0:
    digit = n % 10
    sum_fact += factorial(digit)
    n //= 10

# Check if Strong Number
if sum_fact == original:
    print(original, "is a Strong Number")
else:
    print(original, "is NOT a Strong Number")
