num = 0
while num >= 0:
    num = int(input())
    if num > 100:
        break
    elif num < 10:
        continue
    else:
        print(num)  