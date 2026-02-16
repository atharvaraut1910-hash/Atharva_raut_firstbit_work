class Emp:
    def __init__(self,name,address,sal):
        self.name = name        #Public
        self._address = address  #Protected
        self.__sal = sal         #Private

e1 = Emp('Atharva','Pune',100000)
print(e1.name)
print(e1._address)      #not working
#print(e1.__sal)        #raise error
print(e1._Emp__sal)
print(e1.__dict__)
#print(e1)

