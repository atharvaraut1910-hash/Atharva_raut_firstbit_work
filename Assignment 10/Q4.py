#Write a program to reverse the list.

# Function to reverse a list
def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        temp = lst[i]
        lst[i] = lst[n - i - 1]
        lst[n - i - 1] = temp
    return lst

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

print("Reversed list =", reverse_list(lst))
