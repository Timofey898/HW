rast = int(input('введите растояние : '))
vrem = int(input('введите время : '))
if (rast // vrem) < 30 :
    print('медленно')
elif (rast // vrem) < 60 :
    print('средне')
elif (rast // vrem) > 90 :
    print('быстро')
