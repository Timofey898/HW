num = int(input('трехзачное число'))
a = num // 100
b = num // 10 % 10
c = num % 10
print (a,b,c)
print (a,c,b)
print (b,a,c)
print (b,c,a)
print (c,a,b)
print (c,b,a)

