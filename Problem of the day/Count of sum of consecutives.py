class Solution:
    def getCount(self, N):
        # code here 
        count = 0
        L = 1
        while (L*(L+1))<2*N:
            a = ((N - (L*(L+1))/2))/(L+1)
            if a - int(a) == 0:
                count+=1
            L+=1
        return count
