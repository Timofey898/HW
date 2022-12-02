str1 = input('введите строку ')
s = len(str1)
p = 0
i = 0
let = ''
if str1.isdigit() == 1:
    for s in range (1,s+1):
        def ans(str1):
            return str1[s-1:s]
        print(ans(str1) + '0')
elif str1.isalpha():
    for let in (str1):
        if let == 'q':
            i = 1 + i
    print(i)
elif str1.isalnum() == 0:
    for let in str1:
        p = p + 1
        if let.isalnum() == 0:
            print(p-1)
        
    
            
            
