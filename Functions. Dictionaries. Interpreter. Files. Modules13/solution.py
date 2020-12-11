n = int(input())
vocabulary = set()
for i in range(n):
    word = input().lower()
    vocabulary.add(word)
n = int(input())
mistakes = set()
for i in range(n):
    str = input().split(' ')
    for wrd in str:
        if wrd.lower() not in vocabulary:
            mistakes.add(wrd.lower())
for mistake in mistakes:
    print(mistake)