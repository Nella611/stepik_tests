a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    b = []
    i = 0
    while i < len(a):
        if i == len(a) - 1:
            print(int(a[i - 1]) + int(a[0]), end='')
        else:
            print(int(a[i - 1]) + int(a[i + 1]), end=' ')
        i += 1        
print()