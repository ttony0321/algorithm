#1427
#문자열
#실버 5

n = str(input())

word = str()
k = sorted(n, reverse=True)
for i in  range(len(k)):
    word += k[i]

print(word)