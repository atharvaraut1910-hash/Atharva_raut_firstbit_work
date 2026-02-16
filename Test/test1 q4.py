#Q4. calculate the cost of painting the following buildings walls (both interior and exterior) you need to accept area (one wall) and cost of both interior and exterior wall.


# Program to calculate painting cost of building walls

# Inputs from user
area = float(input("Enter area of one wall (in sq.ft or sq.m): "))
cost_interior = float(input("Enter cost of painting per area for interior walls: "))
cost_exterior = float(input("Enter cost of painting per area for exterior walls: "))
num_interior = int(input("Enter number of interior walls: "))
num_exterior = int(input("Enter number of exterior walls: "))

# Calculations
total_interior_cost = num_interior * area * cost_interior
total_exterior_cost = num_exterior * area * cost_exterior
total_cost = total_interior_cost + total_exterior_cost

# Output
print("Total cost of interior wall painting is:", total_interior_cost)
print("Total cost of exterior wall painting is:", total_exterior_cost)
print("Overall painting cost:", total_cost)

