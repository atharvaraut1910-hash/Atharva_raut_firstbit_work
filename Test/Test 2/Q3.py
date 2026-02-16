import math

# Given values
length = 50
breadth = 40
radius = 20
cost_per_meter = 35

# Perimeter of rectangle + semicircle
perimeter = 2 * length + breadth + (math.pi * radius)

# Fencing 5 times
total_length = perimeter * 5

# Total cost
total_cost = total_length * cost_per_meter

print("Total fencing length (in meters):", total_length)
print("Total cost of fencing: ₹", total_cost)
