#Write a program to remove duplicates from the list.

# Function to remove duplicates from list
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        found = False
        for j in new_list:
            if i == j:
                found = True
                break
        if not found:
            new_list.append(i)
    return new_list

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

result = remove_duplicates(lst)

print("List after removing duplicates =", result)
