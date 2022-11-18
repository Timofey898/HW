import math
com = 0
while not (com == ('конец')):
    com = input('введите команду >>>')
    if com == ('лого'):
        logo = input('сторка')
        print (math.log(len(logo)))
    if com == ('триго'):
        grad = float(input('введите градусы '))
        rad = math.radians(grad)
        print (math.sin(rad),math.cos(rad),math.tan(rad),math.cos(rad)/math.sin(rad),sep = '\n')
        
        
    
