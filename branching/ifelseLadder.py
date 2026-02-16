num = int(input('Enter number to check pos or neg:'))

if(num == 0):
    print(f'{num} is a neutral number.')
elif(num > 0):
    print(f'{num} is a positive number.')
else:
    print(f'{num} is a negative number.')
    