#Write a program to reverse a given number using recursive function.

# Recursive function to reverse number
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

# Main program
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)

print("Reversed number =", reversed_num)
