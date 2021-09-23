class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        import math
        count = 0
        while n>0:
            temp = math.log(n)/math.log(2)
            temp = math.floor(temp)
            count += ((2**(temp-1))*temp)+(n-(2**temp)+1)
            n = n-2**temp
        return int(count)
