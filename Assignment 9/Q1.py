#Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!

# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Function to calculate sum of factorial series using recursion
def sum_factorial(n):
    if n == 1:
        return 1
    return factorial(n) + sum_factorial(n - 1)

# Main program
n = int(input("Enter value of n: "))
print("Sum of series =", sum_factorial(n))
