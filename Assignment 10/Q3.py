# Function to find second largest element
def second_largest(lst):
    if len(lst) < 2:
        return None

    largest = lst[0]
    second = lst[0]

    for i in lst:
        if i > largest:
            second = largest
            largest = i
        elif i != largest and i > second:
            second = i

    return second

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

result = second_largest(lst)

if result is None:
    print("Second largest element not possible")
else:
    print("Second largest element =", result)
