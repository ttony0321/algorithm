#11047
#그리디 알고리즘
#실버 4

n, k = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

cnt = 0
for j in range(len(money)-1, -1, -1):
    if k%money[j] != k:
        cnt += int(k / money[j])
        k = k%money[j]


print(cnt)