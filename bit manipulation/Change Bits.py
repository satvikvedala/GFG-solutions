class Solution:
    def changeBits(self, N):
        # code here 
        import math
        b = math.log(N)/math.log(2)
        b = math.floor(b)
        temp = N
        for i in range(b+1):
            N = N|(1<<i)
        return [N - temp,N]
