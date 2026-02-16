# Program to calculate Profit or Loss

cost_price = float(input("Enter Cost Price (CP): "))
selling_price = float(input("Enter Selling Price (SP): "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)
else:
    print("No Profit No Loss")
