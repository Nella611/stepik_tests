way = input()
base = []
with open (way) as inf:
    for line in inf:
        base.append(line.strip())
counter = 0
math_all = 0
phys_all = 0
rus_lan_all = 0
sum = 0
for i in base:
    counter += 1
    student = i.split(';')
    for j in range(1, len(student)):
        if j == 1:
            math_all += float(student[j])
        elif j == 2:
            phys_all += float(student[j])
        else:
            rus_lan_all += float(student[j])
        sum += float(student[j])
    print(sum / 3)
    sum = 0
print(math_all / counter, end=' ')
print(phys_all / counter, end=' ')
print(rus_lan_all / counter, end='')
print()