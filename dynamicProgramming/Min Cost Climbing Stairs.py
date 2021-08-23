class Solution:
    def minCostClimbingStairs(self, cost, N):
        #Write your code here
        dp = [0]*(N)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,N):
            dp[i] = cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
