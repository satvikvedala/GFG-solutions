class Solution:
    def count(self, S, m, n): 
        # code here 
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 1
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = dp[i][j-1]
                if S[j-1]<=i:
                    dp[i][j]+=dp[i-S[j-1]][j]
        return dp[n][m]
