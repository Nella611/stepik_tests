a = int(input())
sum = 0
q = 0
while True:
    sum += a
    q += a ** 2
    if sum == 0:
        print(q)
        break
    a = int(input())