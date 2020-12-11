a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('  ', end='  ') #отдельно для первой строчки
for f in range(c, d + 1): #отдельно для первой строчки
    if len(str(f)) < 2:
        f = (' ' + str(f)) #для выравнивания строк по вертикали
    print(f, end='  ')
print()
for i in range(a, b + 1):#вертикаль 
    if len(str(i)) < 2:
        i = ' ' + str(i)# выравнивание
    print(i, end='  ') #отдельно для первого числа по вертикали
    i = int(i)
    for j in range(c, d + 1): #горизонталь 
        x = j * i
        if len(str(x)) < 2:
            x = ' ' + str(x)#выравнивание
        print(x, end='  ')        
    print()