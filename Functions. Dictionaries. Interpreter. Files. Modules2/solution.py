def modify_list(l):
    x = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            x.append(l[i] // 2)
    l[:] = x