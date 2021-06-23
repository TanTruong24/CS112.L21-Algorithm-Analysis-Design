def crush(s):
        n = len(s)
        cut, dp = [-1] + [n] * n, [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (j+1>=i or dp[j+1][i-1]):
                    dp[j][i] = True
                    cut[i+1] = min(cut[i+1], cut[j]+1)
        return cut[-1]
 
s = input()
print(crush(s))
 