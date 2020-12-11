lst = input().split()
num = input()
i = 0
if num not in lst:
    print('Отсутствует')
else:
    while i < len(lst):
        if num == lst[i]:
            print(i, end=' ')
        i += 1
    print()