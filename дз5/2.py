str1 = input('введите строку ')
print(len(str1))
def first1(str1):
    return str1[:1]
print(first1(str1))
n = len(str1)
i = n
p = 0
str2 = ''
str3 = ''
str4 = ''
def firstL(str1):
    return str1[n-1:n]
print(firstL(str1))
for n in range (0,n):
    p = i -n
    def firstO(str1):
        return str1[p-1:p]
    str2 = str2 + (firstO(str1))
print(str2)
for n in range(0,n+2):
    if n % 2 == 0:
        def firstH(str1):
            return str1[n-1:n]
        str3 = str3 +firstH(str1)
    else:
        def firstH(str1):
            return str1[n-1:n]
        str4 = str4 +firstH(str1)
print(str3)
print(str4)

            
    
