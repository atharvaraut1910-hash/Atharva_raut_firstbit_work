#Write a program to check if given number is Armstrong or not using recursive function.

# Recursive function to calculate power
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Recursive function to calculate Armstrong sum
def armstrong_sum(num, digits):
    if num == 0:
        return 0
    return power(num % 10, digits) + armstrong_sum(num // 10, digits)

# Main program
n = int(input("Enter a number: "))
digits = len(str(n))

if armstrong_sum(n, digits) == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")
