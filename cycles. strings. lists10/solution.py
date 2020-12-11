a = [int(i) for i in input().split()]
if len(a) > 1:
    a.sort()
    b = []
    i = 0
    for num in a:
        if num == a[i - 1]:
            if num not in b:
                print(num, end=' ')
                b += [num]
        i += 1
print() 