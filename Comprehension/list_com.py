li = []
for i in range(1, 11):
    li.append(i)

even = []
odd = []

for num in li:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Original List:", li)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


li = []
for i in range(1, 11):
    li.append(i)

square = []
for num in li:
    square.append(num ** 2)

print("Original List:", li)
print("Squares:", square)
