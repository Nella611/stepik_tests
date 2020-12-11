way = input()
text = ''
with open (way) as inf:
    for line in inf:
        line = line.strip() #склеивает строчки, но нет пробела между строками
        text += line
        text += ' '
q = []
word = ''
for letter in text:
    if letter != ' ':
        word += letter
    else:
        q.append(word)
        word = ''
if len(word) > 0:
    q.append(word)
        
s = {}
for word in q:
    if word.lower() in s:
        s[word.lower()] += 1
    else:
        s[word.lower()] = 1
value = 0
for key in s:
    if s[key] > value:
        keys.clear()
        value = s[key]
        keys.append(key)
    elif s[key] == value:
        keys.append(key)
    else:
        continue
            
imax = keys[0]
for i in range(len(keys)):
    if keys[i] > imax:
        imax = keys[i]

print(imax , value)