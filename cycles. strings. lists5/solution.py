a = int(input())
b = int(input())
counter = 0
s = 0
for i in range (a, b + 1):
    if i % 3 == 0:
        s += i
        counter +=1
print(float(s / counter))