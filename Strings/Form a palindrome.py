    def findMinInsertions(self, S):
        # code here
        s = S[::-1]
        dp = [[0 for j in range(len(s)+1)] for i in range(len(S)+1)]
        for i in range(len(S)+1):
            dp[i][0] = 0
        for j in range(len(s)+1):
            dp[0][j] = 0
        for i in range(1,len(S)+1):
            for j in range(1,len(s)+1):
                if S[i-1] == s[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return len(S) - dp[len(S)][len(s)]
