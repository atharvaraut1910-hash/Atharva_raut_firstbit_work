# Sum of digits of a 3-digit number

num = int(input("Enter a three-digit number: "))

# Extract digits
a = num // 100            # hundreds place
b = (num // 10) % 10      # tens place
c = num % 10              # units place

digit_sum = a + b + c

print("Sum of digits:", digit_sum)