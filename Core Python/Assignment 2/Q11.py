# Minimum number of notes for a given amount

amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("\nMinimum notes:")

count = 0
for note in notes:
    if amount >= note:
        n = amount // note
        amount = amount % note
        count += n
        print(note, "x", n)

print("\nTotal number of notes:", count)

