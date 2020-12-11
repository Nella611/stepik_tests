steps = int(input())
result = [0, 0]
for i in range(steps):
    step = input().split(' ')
    if step[0] == 'север':
        result[1] += int(step[1])
    elif step[0] == 'юг':
        result[1] -= int(step[1])
    elif step[0] == 'восток':
        result[0] += int(step[1])
    else:
        result[0] -= int(step[1])
print(*result)