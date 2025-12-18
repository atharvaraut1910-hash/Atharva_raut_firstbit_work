##Write a program to input angles of a triangle and check whether triangle is valid or not.

a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

# A triangle is valid if the sum of all angles is 180
if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
