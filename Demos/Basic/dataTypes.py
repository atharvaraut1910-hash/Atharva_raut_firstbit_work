#1.int
x=10
print(type(x))

#2.float
x=3.14
print(type(x))

#3.complex
x=10+5j #10 is real,5j is imaginary
print(type(x))



###Text
#1.str
x='abc'
print(type(x))

x="abc"
print(type(x))

x='''this is first line.this is second line'''
print(type(x))

x="""this is first line.this is second line"""
print(type(x))


####Sequential
#1.list
x=[10,20,30,40]
print(type(x))

#2.tuple
x=(10,20,30,40)
print(type(x))

#3.range
x=range(1,11)
print(type(x))


###Settype
#1.Set
x={10,20,30,40}
print(type(x))

#2.frozenset
x=frozenset({10,20,30,40,})
print(type(x))


###Mapping
x={'id':101,'name':'atharva','sal':25000}
print(type(x))



###Nonetype
x=None
print(type(x))



###Boolean
#1.True
x=True
print(type(x))

#2.False
x=False
print(type(x))
