# Program to calculate total painting cost for 4 equal sized walls

# accept height and width of wall
height = float(input("Enter height of wall (in meters): "))
width = float(input("Enter width of wall (in meters): "))

# accept painting rate per square meter
rate = float(input("Enter painting rate per sq. meter: "))

# area of one wall
area_one_wall = height * width

# total area of four walls
total_area = 4 * area_one_wall

# calculate total painting cost
total_cost = total_area * rate

print("\nTotal painting area:", total_area, "sq.m")
print("Total painting cost: ₹", total_cost)
