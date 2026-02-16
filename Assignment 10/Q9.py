# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

# Function to separate even and odd elements
def separate_even_odd(lst):
    even_list = []
    odd_list = []

    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

even_list, odd_list = separate_even_odd(lst)

print("Even elements list =", even_list)
print("Odd elements list =", odd_list)
