#11048
#다이나믹 프로그래밍

a, b = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(a)]

dp = [[0]*(b+1) for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        dp[i][j] = lst[i-1][j-1] + max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
print(dp[i][j])