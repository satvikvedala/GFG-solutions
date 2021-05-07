class Solution:

	def countStrings(self,n):
    	# code here
    	if n == 1:
    	    return 2
    	dp = [0]*(n+1)
    	dp[1] = 2
    	dp[2] = 3
    	for i in range(3,n+1):
    	    dp[i] = (dp[i-1]+dp[i-2])%1000000007
    	return dp[n]
