#save memory
#generating values acccording to user requirement
#Mainting state of function
#using yield keyword to return value


def fun():
    for i in range(1,11):
        yield i

res = fun()

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))