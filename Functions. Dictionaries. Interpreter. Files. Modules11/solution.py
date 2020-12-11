n = int(input())
i = 0
matches = {}
while i < n:
    match = input().split(';')
    #print(match)
    first_team = match[0]
    second_team = match[2]
    score_first_team = int(match[1])
    score_second_team = int(match[3])
    if first_team not in matches:
        matches[first_team] = [1, 0, 0, 0, 0]
    else:
        matches[first_team][0] += 1
    if second_team not in matches:
        matches[second_team] = [1, 0, 0, 0, 0]
    else:
        matches[second_team][0] += 1
    if score_first_team > score_second_team:
        matches[first_team][1] += 1
        matches[first_team][4] += 3
        matches[second_team][3] += 1
    elif score_first_team < score_second_team:
        matches[second_team][1] += 1
        matches[second_team][4] += 3
        matches[first_team][3] += 1
    else:
        matches[first_team][2] += 1
        matches[first_team][4] += 1
        matches[second_team][2] += 1
        matches[second_team][4] += 1
    i += 1
for j in matches:
    print(j, end=':')
    for k in matches[j]:
        print(k, end=' ')
    print()