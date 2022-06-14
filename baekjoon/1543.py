#1543
#그리디 알고리즘, 문자열, 브루트포스 알고리즘
#실버 4

pdf = input()
word = input()
cnt = 0
n = 0
while n <= len(pdf) - len(word):
    if pdf[n:n+len(word)] == word:
        cnt += 1
        n += len(word)
    else:
        n += 1
print(cnt)