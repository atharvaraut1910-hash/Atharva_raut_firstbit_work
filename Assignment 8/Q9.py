def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return temp == rev

n = int(input("Enter number: "))
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")
