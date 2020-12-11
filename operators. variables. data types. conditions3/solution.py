a = float(input())
b = float(input())
calk = input()
if calk == '/':
    if b == 0.0:
        print('Деление на 0!')
    else:
        print(a / b)
elif calk == '+':
    print(a + b)
elif calk == '-':
    print(a - b)
elif calk == '*':
    print(a * b)
elif calk == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif calk == "pow":
    print(a ** b)
elif calk == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)