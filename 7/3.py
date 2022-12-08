import random 
my_file = open("vvs.txt", "r")
a = my_file.readline()
line1 = random.choice(open('vvs.txt').readlines())
line2 = random.choice(open('vvs.txt').readlines())
if not(line1 == line2):
    print('I recieve ',line1)
    print('You receive ',line2)
else :
    line1 = random.choice(open('vvs.txt').readlines())
    line2 = random.choice(open('vvs.txt').readlines())
    print('I recieve ',line1)
    print('You receive ',line2)
