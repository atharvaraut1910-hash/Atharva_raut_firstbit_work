# WAP to perform days into year, weeks, and days

# Take input from user
days = int(input("Enter number of days: "))
# calculate years
years = days // 365

# calculate remaining days 
rem_days = days % 365

# calculate weeks
weeks = rem_days // 7

# calculate remaining days
days_left = rem_days % 7
# Display result
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days_left)
