n = int(input())
a = [[i] * i for i in range(1,n + 1)]
counter = []
for i in range(n):
    for j in range(len(a[i])):
        counter.append(a[i][j]) 
        print(a[i][j], end= ' ')
        if len(counter) == n:
            break
    if len(counter) == n:
        break
print()