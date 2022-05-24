n = int(input())
words = []
for i in range(n):
    words.append(input())

set_words = set(words)
words = list(set_words)
words.sort()
words.sort(key=len)

for i in words:
    print(i)