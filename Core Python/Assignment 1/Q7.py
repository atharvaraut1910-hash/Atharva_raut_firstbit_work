# Program to Find the Roots of a Quadratic Equation
# input the values of a, b, c
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of C: "))

# Perform operation to find roots 
sq_rt_des = (b * b) - (4 * a * c)
sq_rt = sq_rt_des ** 0.5

root1 = (-b + sq_rt) / (2 * a) 
root2 = (-b - sq_rt) / (2 * a) 

print(root1)
print(root2)