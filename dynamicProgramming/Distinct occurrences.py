class Solution:
    def sequenceCount(self,arr1, arr2):
        # Code here
        dp = [[0 for j in range(len(arr2)+1)]for i in range(len(arr1)+1)]
        for i in range(len(arr1)):
            dp[i][0] = 1
        for i in range(1,len(arr1)+1):
            for j in range(1,len(arr2)+1):
                dp[i][j] = dp[i-1][j]
                if (arr2[j-1] == arr1[i-1]):
                    dp[i][j]+=dp[i-1][j-1]
        return dp[len(arr1)][len(arr2)]%1000000007
