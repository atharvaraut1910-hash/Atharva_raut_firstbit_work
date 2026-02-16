#Method 1: importing file
import functions
res = functions.chkEven(10)
print(res)


#Method 2: importing functions from file
from functions import *
res = chkEven(10)
print(res)

#Method 3: import specific functions from file
from functions import chkEven,chkPos
res = chkPos(7)
print(res)

#Method 4: Alias 
import functions as fun 
res = fun.chkEven(10)
print(res)

