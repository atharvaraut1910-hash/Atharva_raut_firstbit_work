#Write a program to print list after removing even numbers.

# Function to remove even numbers from list
def remove_even_numbers(lst):
    new_list = []
    for i in lst:
        if i % 2 != 0:
            new_list.append(i)
    return new_list

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

result = remove_even_numbers(lst)

print("List after removing even numbers =", result)
