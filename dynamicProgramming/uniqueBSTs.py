#Unique BST's 
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
  for j in range(i):
    dp[i] += dp[i]*dp[i-j-1]
return dp[n]%1000000007
 
