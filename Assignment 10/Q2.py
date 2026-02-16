# Function to find maximum and minimum
def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]

    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i

    return max_val, min_val

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

max_element, min_element = find_max_min(lst)

print("Maximum element =", max_element)
print("Minimum element =", min_element)
