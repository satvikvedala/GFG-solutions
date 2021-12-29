class Solution:
	def minCoins(self, coins, M, V):
		# code here
		dp = [float("inf") for i in range(V+1)]
		for i in range(M):
		    if coins[i]<=V:
		        dp[coins[i]] = 1
	    for i in range(1,V+1):
	        temp = dp[i]
	        for j in range(M):
	            if coins[j]<=i:
	                temp = min(temp,1+dp[i-coins[j]])
	        dp[i] = temp
	    if dp[-1] == float('inf'):
	        return -1
	    return dp[-1]
