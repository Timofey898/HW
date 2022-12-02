import random
import array
mylist = []
list1 = []
q =0
n = int(input('Задайте размер списка:'))
for n in range (0,n):
    o = random.randrange(0,2)
    mylist.append(o)
print(mylist)
col = mylist.count(0)
print(col)
col1 = mylist.count(1)
print(col1)
for n in range (0,n):
    if 0 in mylist :
        q = mylist.index(0)
        mylist.pop(q)
        mylist.insert(q, 1)
        list1.append(q)
print(list1)
