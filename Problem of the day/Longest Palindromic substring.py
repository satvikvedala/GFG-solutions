class Solution:
    def longestPalindrome(self, S):
        # code here
        ma = 0
        res = ''
        for i in range(len(S)):
            for j in range(i+1,len(S)+1):
                if S[i:j] == S[i:j][::-1]:
                    if len(S[i:j])>ma:
                        ma = len(S[i:j])
                        res = S[i:j]
                    
                
        return res
