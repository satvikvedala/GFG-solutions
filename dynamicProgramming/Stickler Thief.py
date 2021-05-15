class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        if n == 1:
            return a[0]
        if n == 2:
            return a[1]
        else:
            dp = [0]*(n+1)
            dp[1] = a[0]
            dp[2] = max(a[1],a[0])
            for i in range(3,n+1):
                dp[i] = max(dp[i-1],dp[i-2]+a[i-1])
            return dp[n]
