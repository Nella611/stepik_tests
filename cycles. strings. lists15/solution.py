num = int(input())
q = [[0] * num for i in range(1, num + 1)]
q[num//2][num//2] = num * num #окончание витка
counter = 1 #занчение в клетке
conv = 0 #виток спирали
for i in range(num // 2): #отрисовка в цикле будет полого витка, потому делим пополам
    #верхняя завитушка:
    for j in range(num - conv):
        q[i][j + i] = counter
        counter += 1
    #правая стеночка:
    for j in range(i + 1, num - i):
        q[j][- i - 1] = counter
        counter += 1
    #низ:
    for j in range(i + 1, num - i):
        q[-i - 1][-j - 1] = counter
        counter += 1
    #левая стеночка:
    for j in range(i + 1, num - (i + 1)):
        q[- j - 1][i] = counter
        counter += 1
    conv += 2
for i in range(num):
    for j in range(num):
        print(q[i][j], end=' ')
    print()