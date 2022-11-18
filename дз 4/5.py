import math
n = int(input('введите чило '))
for n in range (1,n):
    if (n % 5)>0:
        print ('Длина окружности с радиусом ',n,':',n * 2 * math.pi)
        print ('Площадь круга с радиусом ',n,':',n**2 * math.pi)
        print ('')
        
        
        
