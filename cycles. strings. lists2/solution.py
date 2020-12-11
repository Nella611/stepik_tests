biol = int(input())
inf = int(input())
i = 1
while i <= biol * inf:
    if i % biol == 0 and i % inf == 0:
        print(i)
        break #как сделать без остановки и без дополнительных циклов не понимаю
    i += 1    
