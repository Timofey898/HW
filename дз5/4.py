
stop = ''
while not(stop == ('stop')):
    str1 = input('введите строку ')
    if str1.isdigit():
        print('цифровая строка ')
    elif str1.isalpha():
        print('Буквенная строка')
    elif str1.isalnum():
        print('Смешаная сторка ')
    stop = input('Продолжим???')
