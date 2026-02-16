#Write a program to create a new list from existing list which contains cube of each number of list.

# Function to create list of cubes
def cube_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i * i * i)
    return new_list

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

result = cube_list(lst)

print("Original list =", lst)
print("Cube list =", result)
