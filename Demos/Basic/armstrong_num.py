num = int(input("Enter number "))
temp = num


count = 0
while(temp > 0):
    #temp % 10
    temp = temp // 10
    count += 1

temp = num
sum = 0
while(temp > 0):
        digit = temp % 10
        temp = temp // 10
        mult = 1
        for i in range(count):
            mult = mult* digit
        sum = sum + mult

if (sum == num):
    print(f'{num}is an armstrong number.')
else:
     print(f'{num} is not an armstrong number.')
