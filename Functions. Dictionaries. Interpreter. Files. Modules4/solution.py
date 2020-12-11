text = input().split()
s = {}
for word in text:
    if word.lower() in s:
        s[word.lower()] += 1
    else:
        s[word.lower()] = 1
for key, value in s.items():
    print(key, value)