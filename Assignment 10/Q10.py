#Write a program to remove all occurrences of a given element in the list.

# Function to remove all occurrences of an element
def remove_element(lst, key):
    new_list = []
    for i in lst:
        if i != key:
            new_list.append(i)
    return new_list

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

key = int(input("Enter element to remove: "))

result = remove_element(lst, key)

print("List after removing", key, "=", result)
