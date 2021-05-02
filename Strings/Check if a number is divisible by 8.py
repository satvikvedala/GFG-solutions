class Solution:
    def DivisibleByEight(self,S):
        #code here
        if len(S)>3:
            S = S[len(S)-3:]
        if int(S)%8 == 0:
            return 1
        return -1
