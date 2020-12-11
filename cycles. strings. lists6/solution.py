seq = input()
counter = seq.upper().count('C') + seq.upper().count('G')
print((counter / len(seq)) * 100)