#WAP to check if a given number is prime number or not.

n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a Prime Number")
    else:
        print(n, "is NOT a Prime Number")
