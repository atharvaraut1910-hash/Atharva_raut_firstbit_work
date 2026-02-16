# Program to check if a 3-digit number is a palindrome

num = int(input("Enter a 3-digit number: "))

# Extract digits
hundreds = num // 100
ones = num % 10

# Check palindrome
if hundreds == ones:
    print(num, "is a Palindrome ✔")
else:
    print(num, "is NOT a Palindrome ❌")
