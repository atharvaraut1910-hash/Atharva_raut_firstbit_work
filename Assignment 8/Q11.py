def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        d = temp % 10
        total += d ** digits
        temp //= 10

    return total == num


n = int(input("Enter number: "))

if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
