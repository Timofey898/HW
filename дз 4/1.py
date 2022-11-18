n = int(input('введит натуральное число '))
a = int(input('введит натуральное число '))
b = int(input('введит натуральное число '))
i = 0
x = 0
for x in range (n,0,-1):
    p = 0
    for i in range ((a+1),b):
        c = b - a - 1
        if (not (i == x)) and (x % 2 >0):
            p = p +1
            if p == c:
                print(x)
    
