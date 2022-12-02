n = int(input('кол строк '))
str2 = ('')
for n in range (0,n):
    str1 = input('введите строку')
    def first1(str1):
        return str1.title()[:1]
    str2 = (str2 + first1(str1))
print(str2)
