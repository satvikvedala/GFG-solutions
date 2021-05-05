class Solution:
    def numberOfConsecutiveOnes (ob,N):
        # code here 
        end_with_one = [0]*(N+1)
        end_with_zero = [0]*(N+1)
        end_with_one[1] = 1
        end_with_zero[1] = 1
        dp = [0]*(N+1)
        for i in range(2,N+1):
            l = 2**i
            end_with_zero[i] = end_with_one[i-1]+end_with_zero[i-1]
            end_with_one[i] = end_with_zero[i-1]
            dp[i] = l - (end_with_zero[i]+end_with_one[i])
        return dp[N]
