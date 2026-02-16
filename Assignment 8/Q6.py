def fibonacci(n):
    a = 1
    b = 1

    if n >= 1:
        print(a, end=" ")
    if n >= 2:
        print(b, end=" ")

    for i in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


n = int(input("Enter number of terms: "))
fibonacci(n)
