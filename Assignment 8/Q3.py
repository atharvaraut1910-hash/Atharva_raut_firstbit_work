# a) 1 + 2 + 3 + ... + n
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# factorial function
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


# b) 1! + 2! + 3! + ... + n!
def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total


# c) 1^1 + 2^2 + 3^3 + ... + n^n
def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total


# main program
n = int(input("Enter value of n: "))

print("Sum of 1 + 2 + ... + n =", sum_n(n))
print("Sum of 1! + 2! + ... + n! =", sum_factorial(n))
print("Sum of 1^1 + 2^2 + ... + n^n =", sum_power(n))
