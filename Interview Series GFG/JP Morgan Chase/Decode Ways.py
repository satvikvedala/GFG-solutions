class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        if s[0] == '0':
            return 0
        else:
            dp[0] = 1
            if len(s) == 1:
                return dp[0]
        if s[1] == '0':
            if int(s[0])*10+int(s[1])<=26:
                dp[1] = dp[0]
            else:
                dp[1] = 0
        else:
            if int(s[0])*10+int(s[1])<=26:
                dp[1] = dp[0]+1
            else:
                dp[1] = dp[0]
        for i in range(2,len(s)):
            if s[i]=='0' and (s[i-1]=='1' or s[i-1]=='2'):
                dp[i] = dp[i-2]
            elif s[i]!='0' and s[i-1] == '0':
                dp[i] = dp[i-1]
            elif s[i]!='0' and s[i-1]!='0':
                if int(s[i-1])*10+int(s[i])<=26:
                    dp[i] = dp[i-1]+dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                dp[i] = 0
        return dp[-1]
