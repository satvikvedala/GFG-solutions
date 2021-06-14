#using dp
class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        dp = [0]
        res = [1]*n
        for i in range(1,n):
            while len(dp)!=0 and a[i]>=a[dp[-1]]:
                res[i] += res[dp[-1]]
                dp.pop()
            dp.append(i)
        return res
