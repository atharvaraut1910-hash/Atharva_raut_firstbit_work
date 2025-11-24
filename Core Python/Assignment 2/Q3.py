# Convert distance from feet & inches to meters & centimeters

feet = int(input("Enter feet: "))
inch = int(input("Enter inches: "))

# Convert feet to inches
total_inches = feet * 12 + inch

# Convert inches to cm
cm = total_inches * 2.54

# Convert cm to meters and remaining cm
meters = int(cm // 100)
remaining_cm = cm % 100

print("Distance in meters and centimeters:")
print("Meters:", meters)
print("Centimeters:", remaining_cm)