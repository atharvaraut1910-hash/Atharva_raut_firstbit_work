#(Do all questions without using inbuilt functions)

#1. Write a program to find sum of all elements of list

# Function to find sum of list elements
def list_sum(lst):
    total = 0
    for i in lst:
        total = total + i
    return total

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

print("Sum of all elements =", list_sum(lst))
