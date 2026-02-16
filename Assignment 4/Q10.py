#WAP to check if given number is Perfect Number.

n = int(input("Enter a number: "))

sum_div = 0

# Find proper divisors
for i in range(1, n):
    if i % 2 == 0 and i % 7:
        print(i, end=" ")
