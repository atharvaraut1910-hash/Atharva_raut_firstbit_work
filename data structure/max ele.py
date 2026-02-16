li =[40,30,60,20,80,10,70]
max = li[0]
for i in range(1,len(li)):
    if(li[i] > max):
        max =  li[i]
print('Maximum element is:',max)
