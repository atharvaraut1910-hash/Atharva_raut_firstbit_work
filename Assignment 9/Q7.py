#Write a program to find sum of digits using recursion.

# Recursive function to find sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# Main program
num = int(input("Enter a number: "))
print("Sum of digits =", sum_of_digits(num))
