n, m = map(int,input().split())
coin = list(map(int,input().split()))

dp = [0] * (n + 1)
dp[0] = 1
for i in range(m): 
    for j in range(coin[i], n+1): 
        dp[j] = dp[j] + dp[j - coin[i]]

print(dp[n])