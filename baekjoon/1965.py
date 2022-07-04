#1965
#다이나믹 프로그래밍

n = int(input())

lst = list(map(int, input().split()))

c = len(lst)
dp = [1 for _ in range(c)]

for i in range(c):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))