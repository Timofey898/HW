num = int(input('введите трехзанчное число :'))
n = num // 100
u = (num // 10 ) % 10
m = num % 10
if max(n,u,m) - min(n,u,m) == n+u+m-min(n,u,m)-max(n,u,m):
    print ('интересное число ')
else :
    print('не интересное ')
