##Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Triangle is valid if sum of any two sides is greater than the third side
if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")
else:
    print("Sides must be positive numbers!")
