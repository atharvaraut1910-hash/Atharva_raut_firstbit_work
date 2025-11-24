# Convert hh:mm:ss to seconds

h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

total_seconds = h * 3600 + m * 60 + s
print("Total time in seconds:", total_seconds)
