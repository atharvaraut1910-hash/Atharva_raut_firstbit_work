#Write a program to print all numbers which are divisible by m and n in the list.

# Function to print numbers divisible by m and n
def divisible_by_m_and_n(lst, m, n):
    for i in lst:
        if i % m == 0 and i % n == 0:
            print(i, end=" ")

# Main program
size = int(input("Enter number of elements: "))
lst = []

for i in range(size):
    value = int(input("Enter element: "))
    lst.append(value)

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Numbers divisible by", m, "and", n, "are:")
divisible_by_m_and_n(lst, m, n)
