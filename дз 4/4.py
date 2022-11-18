import math
import random
i = 0
com = 0

while not(com ==('N')):
    a = int(input('введите натуральное число'))
    b = int(input('введите натуральное число'))
    ran = random.randrange(a, b)
    for i in range (1,ran):
        print(math.log(i,10))
    com = input('Желаете продолжить? Y/N >>>')
