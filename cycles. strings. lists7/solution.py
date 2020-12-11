dnc = input()
dnccod = ''
counter = 1
sym = dnc[0]
for c in dnc[1:]:
    if c == sym:
        counter += 1
        
    else:
        if counter == 0:
            counter = 1
        dnccod += sym
        dnccod += str(counter)
        sym = c
        counter = 1
if counter >= 1:
    dnccod += sym
    dnccod += str(counter)
print(dnccod)