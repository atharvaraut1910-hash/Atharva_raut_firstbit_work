#  Write a program to check if given number is Armstrong number or not.
#  (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
#  4*4*4*4)

# Program to check Armstrong Number

n = int(input("Enter a number: "))
original = n

# Count digits
digits = len(str(n))

sum_power = 0

# Calculate sum of digits raised to powers
while n > 0:
    digit = n % 10
    sum_power += digit ** digits
    n //= 10

# Check Armstrong condition
if sum_power == original:
    print(original, "is an Armstrong Number")
else:
    print(original, "is NOT an Armstrong Number")
