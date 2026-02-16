# li = [[j for j in range(i, i+10)] for i in range(1, 101, 10)]
# print(li)


li = [[j for j in range(i * 10 + 1,(i+1) * 10 + 1)] for i in range(10)]
print(li)
