import random
import array
mylist = []
n = int(input('Задайте размер списка:'))
s = int (input('удалить из списка'))
for n in range (0,n):
    o = random.randrange(0,10)
    mylist.append(o)
print(mylist)
for n in range (0,n):
    if s in mylist :
        mylist.remove(s)
print(mylist)
