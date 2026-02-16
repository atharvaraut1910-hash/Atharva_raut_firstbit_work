#1. Structure:[]
li = [10,20,30,40]
print(type(li))

#2.Type of data:Heterogeneous
li = [10,3,14,'abc',[10,20]]
print(type(li))
print(li)

#3.Sequence:Ordered
print(li)

#4.Changable:Mutable
print(id(li))
li[1] = 6.18
print(id(li))
print(li)

