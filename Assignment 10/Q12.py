#Write a program to create three lists of numbers, their squares and cubes

# Function to create square and cube lists
def create_square_cube_lists(lst):
    square_list = []
    cube_list = []

    for i in lst:
        square_list.append(i * i)
        cube_list.append(i * i * i)

    return square_list, cube_list

# Main program
n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

squares, cubes = create_square_cube_lists(numbers)

print("Numbers list =", numbers)
print("Squares list =", squares)
print("Cubes list =", cubes)
