class Solution:
    def reversedBits(self, X):
        # code here 
        res = 0
        for i in range(0,32):
            if X&(1<<i)>0:
                res = res|(1<<(31-i))
        return res
