x = float(input('введите x'))
y = float(input('введите y'))
if x == 0 or y == 0:
    print ('x и y > 0')
else :
    if x > 0 and y > 0:
        print ('точка в первой четверти ')
        strok1 = str(input('введите первую сторчку'))
        strok2 = str(input('введите вторую строчку'))
        if len(strok1) > len(strok2):
            print (strok2)
        elif len(strok1) == len(strok2):
            print ('сторки равны')
        else :
            print(strok1)
    if x < 0 and y > 0:
        print ('вторая четверть ')
        f = (2 * abs(x) - y)
        f = f / (y**2)
        print(f)
    if x < 0 and y < 0:
        print('третья четверть')
        strok = (input('введите строку'))
        print('(',int(len(strok)*x),',',len(strok)*y,')')
    if x > 0 and y < 0:
        print ('четверая четверть')
        if abs(x) > abs(y):
            print('Координата x – наибольшая по модулю')
        elif abs(x) < abs(y):
            print('Координата x – наибольшая по модулю')
        else:
            print('Координаты равны по модулю')

            
            
        







