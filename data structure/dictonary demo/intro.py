#1. denote by {}, pair of key & value
di = {1:'python',2:'Java',3:'C'}

#2. Hetrogenous
di = {'name':'Atharva','Age':22,'Modules':['Python','Data analysis','Data science']}

#3.Orderd

#4.Dict:Mutable,key:Immutable,value:Mutable,
print(type(di))
print(id(di))
di['name'] = 'Atharva Raut'
di['Salary'] = 20000
print(di)
print(id(di))
