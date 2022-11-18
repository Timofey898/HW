import random
a = random.randint(0, 1000)
b = random.randint(0, 1000)
x = 0

n = int(input('введите число '))
i = 0
for i in range (min(a,b),max(a,b)):
    if i == n :
        x = 1
    else :
        x = x
if x == 1:
    print ('Lucky!')
else :
    print('Try again!')
