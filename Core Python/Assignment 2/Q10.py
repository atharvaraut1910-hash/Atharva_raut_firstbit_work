# Reverse a three-digit number

num = int(input("Enter a three-digit number: "))

a = num // 100        # hundreds digit
b = (num // 10) % 10  # tens digit
c = num % 10          # units digit

rev = c * 100 + b * 10 + a

print("Reversed number:", rev)