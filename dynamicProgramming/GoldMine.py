class Solution:
    def maxGold(self, n, m, M):
        # code here
        dp = [[0 for j in range(m)] for i in range(n)]
        ma = 0
        for j in range(m-1,-1,-1):
            for i in range(n):
                if i == 0 or j == m-1:
                    diag_up = 0
                else:
                    diag_up = dp[i-1][j+1]
                
                if j == m-1:
                    right = 0
                else:
                    right = dp[i][j+1]
                
                if i == n-1 or j == m-1:
                    diag_down = 0
                else:
                    diag_down = dp[i+1][j+1]
                    
                dp[i][j] = M[i][j]+max(diag_up,max(diag_down,right))
        res = 0
        for i in range(n):
            res = max(res,dp[i][0])
        return res
