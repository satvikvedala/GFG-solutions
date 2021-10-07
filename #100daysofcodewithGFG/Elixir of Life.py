class Solution:
    def maxFrequency(self, S):
        # code here
        i = 0
        j = len(S)-1
        isum = 0
        jsum = 0
        sti = ''
        stj = ''
        count = 1
        while i<len(S) and j>-1:
            isum+=ord(S[i])
            jsum+=ord(S[j])
            sti+=S[i]
            stj+=S[j]
            if isum == jsum and sti == stj[::-1]:
                ss = sti
                break
            i+=1
            j-=1
        x = len(ss)
        y = x+len(ss)-1
        while x<=len(S)-len(ss):
            if S[x:y+1] == ss:
                count+=1
            x+=1
            y+=1
        return count
