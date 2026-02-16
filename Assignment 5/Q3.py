n = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0

for i in range(1, n + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        amount = ticket_cost * 0.70   # 30% discount
    elif age > 59:
        amount = ticket_cost * 0.50   # 50% discount
    else:
        amount = ticket_cost          # full payment

    total_amount += amount

print(f"\nTotal ticket amount to be paid: ₹{total_amount}")
