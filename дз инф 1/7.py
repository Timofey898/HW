num = int(input('трехзачное число'))
a = num // 100
b = num // 10 % 10
c = num % 10
if  a > b:
    if a > c:
        print(a)
elif b > c:
    print(b)
else :
    print(c)
    
