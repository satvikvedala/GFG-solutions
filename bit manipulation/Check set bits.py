class Solution:
    def isBitSet (self, N):
        # code here 
        import math
        b = math.log(N)/math.log(2)
        b = math.ceil(b)
        if N  == (2**b)-1:
            return 1
        return 0
