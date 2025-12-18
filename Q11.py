# Program to calculate total ticket amount for 5 people

total_amount = 0

ticket_price = float(input("Enter ticket price per person: "))

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))

    if age < 12:
        discount = 0.30 * ticket_price     # 30% discount
        final_amount = ticket_price - discount
    elif age > 59:
        discount = 0.50 * ticket_price     # 50% discount
        final_amount = ticket_price - discount
    else:
        final_amount = ticket_price        # No discount

    total_amount += final_amount

print("\nTotal ticket amount for all 5 people =", total_amount)
