#append, clear, copy, count, extend, index, insert, pop
#remove, reverse, sort

li=[10,30,60,20,50]

###Add element
#single element
li.append(80)    #add single element at the end
li.append([90,100])

##Multiple
li.extend([90,100])   #ass multiple elements at end

li.insert(3,'abc')   #add element at given index

###Remove element
li.clear()   #remove all element/ empty list

#using index 
#li.pop()  #last element will be removed
#li.pop(15) #remove elemnt of given index

###Other methods
print(li.index(70))  #return the index of given element
                        #if ele not present,gives valueerror

li2=li.copy()
li3=li
li.pop()
print(li2)
print(li3)

print(li.count(70))  #return occurances

li.reverse()
li.sort(reverse=True)   #sorted list - reverse = True, used to sort in descending order
