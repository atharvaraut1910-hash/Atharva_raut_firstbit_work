num = int(input("Enter a 3-digit number: "))

#extract digit
First = num // 100
second = (num // 10) % 10
third = num % 10

#condition
#first = 2 * second
#first = third / 2  third = 2 * first

if First== 2 * second and First * 2 == third:
    print("yes,you have done it")
else:
    print("please try next time")
    