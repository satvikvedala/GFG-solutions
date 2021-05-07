class Solution:
	def minCoins(self, coins, M, V):
		# code here
		dp = [0]*(V+1)
		dp[0] = 0
		res = float("inf")
		for i in range(1,V+1):
		    temp = float("inf")
		    for j in range(M):
		        if coins[j]<=i:
		            temp = min(temp,1+dp[i-coins[j]])
		    dp[i] = temp
		if dp[V]<res:
		    return dp[V]
		return -1
