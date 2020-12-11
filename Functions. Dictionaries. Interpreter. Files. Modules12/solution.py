wors = input()
cipher = input()
conformity = {}
for i in range(len(wors)):
    conformity[wors[i]] = cipher[i]
#print(conformity)
to_cipher = input()
un_cipher = input()
result = ''
for i in range(len(to_cipher)):
    result += conformity[to_cipher[i]]
print(result)
result2 = ''
for i in range(len(un_cipher)):
    for j in conformity:
        if conformity[j] == un_cipher[i]:
            result2 += j
            break
print(result2)