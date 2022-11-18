first = int(input('введите первое число :'))
sec = int(input('введите второе число :'))
if first > sec :
    print (first,'наибольшее число')
    print (sec,'наименьшее число')
elif first < sec :
    print (sec,'наибольшее число')
    print (first,'наименьшее число')
elif first == sec :
    print ('числа равны ')
