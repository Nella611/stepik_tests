# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())
nums = []
sum_num = {}
for i in range(1, n + 1):
    x = int(input())
    if x not in sum_num:
        sum_num[x] = f(x)
    print(sum_num[x])