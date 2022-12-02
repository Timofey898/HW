import random
import array
n = int(input('Задайте размер списка:'))
i = int(input('Задайте начало диапазона:'))
c = int(input('Задайте онец диапазона:'))
mylist = []
for n in range (0,n):
    o = random.randrange(i,c)
    mylist.append(o)
print(mylist)
print(len(mylist))
print(max(mylist))
print(min(mylist))
print(sorted (mylist))
mylist.sort(reverse = True)
print(mylist)
    
       
