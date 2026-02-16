#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter n: "))
fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i
    total += fact

print("Sum of series =", total)

#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

N = int(input("Enter N: "))
total = 0

for i in range(1, N + 1):
    total += N ** i

print("Sum of series =", total)


#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter n: "))
term = 1
total = 0

for i in range(1, n + 1):
    total += term
    term *= 2

print("Sum of geometric series =", total)

#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter value of a: "))
total = 0

for i in range(1, 11):
    total += (a ** i) / i

print("Sum of series =", total)

#e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

total = 0
sign = 1
den = 1

for i in range(1, n + 1):
    total += sign * (x ** i) / den
    sign *= -1
    den += 2

print("Sum of series =", total)
