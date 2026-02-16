#Write a program to create a duplicate of an existing list. It should not point to same list.

# Function to duplicate a list
def duplicate_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
    return new_list

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

dup_list = duplicate_list(lst)

print("Original list =", lst)
print("Duplicate list =", dup_list)

# Proof they are different lists
if id(lst) != id(dup_list):
    print("Both lists are different (not pointing to same list)")
