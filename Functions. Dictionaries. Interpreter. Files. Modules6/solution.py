str = input()
leter = str[0]
a = []
num = ""
q = 0
for i in range(1, len(str)):
    if (i + q) >= len(str):
        break
    if str[i + q].isdigit():
        num += str[i + q]
        for j in range(i + q + 1, len(str)):
            if str[j].isdigit():
                qq += 1
                q += 1
                num += str[j]
            else:
                break
        a.append(str[i + q - qq - 1] * int(num))
        num = ''
        qq = 0
for i in a:
    print(i, end='')
print()