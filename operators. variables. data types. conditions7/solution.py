# put your python code here
a = int(input())
# с учетом того, что нам циклы и манипуляции со сроками не даны:
sum1 = a % 10 + (a % 100) // 10 + (a % 1000) // 100
sum2 = (a % 10000) // 1000 + (a % 100000) // 10000 + (a % 1000000) // 100000
if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')