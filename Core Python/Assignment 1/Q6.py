# Write a Program to input two angles from user and find third angle of the triangle.
a1 = int(input("Enter the first angle of the triangle: "))
a2 = int(input("Enter the second angle of the triangle: "))
#  Calculate third angle 
a3 = 180 - (a1 + a2)
# Display result
print(f'The third angle of the triangle is {a3} degress')
