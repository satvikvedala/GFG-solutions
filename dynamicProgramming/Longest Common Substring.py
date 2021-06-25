class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        res = 0
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif S1[i-1] == S2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    res = max(res,dp[i][j])
        return res
