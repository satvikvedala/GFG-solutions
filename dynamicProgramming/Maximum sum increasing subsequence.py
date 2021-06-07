class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		dp = [0]*n
		for i in range(n):
		    dp[i] = Arr[i]
		for i in range(1,n):
		    for j in range(i):
		        if Arr[i]>Arr[j] and dp[i]<Arr[i]+dp[j]:
		            dp[i] = Arr[i]+dp[j]
		return max(dp)
