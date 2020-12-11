info = input()
register = {}
for i in range(1, 12):
    register[i] = []

with open(info) as inf:
    for line in inf:
        line = line.split()
        register[int(line[0])].append(line[2])

for i in range(1, 12):
    print(i, end=' ')
    if len(register[i]) == 0:
        print('-', end='')
    else:
        summ = 0
        for j in range(len(register[i])):
            summ += int(register[i][j])
        average = summ / len(register[i])
        print(average, end='')
    print()