n = int(input()) 
w = [list(map(int, input().split())) for _ in range(n)]
dp = [0]* (n+1)


for i in range(n-1, -1, -1):
    t = w[i][0]
    if i + t <= n:
        p = w[i][1]
        dp[i] = max(dp[i+1], dp[i+t]+p)
    
    else:
        dp[i] = dp[i+1]
        
print(dp[0])