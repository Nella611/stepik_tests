a = int(input())
b = int(input())
c = int(input())
m = a
if m <= b:
    m = b
if m <= c:
    m = c
print(m)
s = a
if s >= b:
    s = b
if s >= c:
    s = c
print(s)
#если есть два одинаковых числа, то сравнение с m & s не работает
"""варианты середины:
число действиетльно всередине false
число минимальное (повторяющееся) false
число максимальное(повторяющееся) true
"""
#добавить еще одно if?
if s < a < m:
    print(a)
elif s < b < m:
    print(b)
elif s < c < m:
    print(c)
    
elif a == m and (b == m or c == m):
    print(a)            
elif a == s and (b == s or c == s):
    print(a)
elif b == m and (a == m or c == m):
    print(b)            
elif b == s and (a == s or c == s):
    print(b)
elif c == m and (a == m or b == m):
    print(c)            
elif c == s and (a == s or b == s):
    print(c)