class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        t = word1
        s = word2
        dp = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
        dp[0][0] = 0
        for j in range(1,len(t)+1):
            dp[0][j] = j
        for i in range(1,len(s)+1):
            dp[i][0] = i
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if t[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1]))
        return dp[len(s)][len(t)]
