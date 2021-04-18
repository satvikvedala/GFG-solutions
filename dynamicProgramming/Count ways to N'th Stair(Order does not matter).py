    def countWays(self,m):
        
        mod = 1000000007
        # code here
        dp = [0]*(m+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,m+1):
            dp[i] = (dp[i-2]+1)%mod
        return dp[m]
