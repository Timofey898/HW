import random 
my_file = open("BabyFile.txt", "r+")
n = int(input('n'))
for n in range (0,n+1):
    s = str(random.randrange(1000,10000))
    my_file.write(s)
    my_file.write(' ')

