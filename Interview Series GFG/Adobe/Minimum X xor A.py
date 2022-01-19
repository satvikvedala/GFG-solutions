class Solution:
    def minVal(self, a, b):
        #code here
        def func(b):
            x = 1
            count = 0
            for i in range(32):
                if b&(x<<i) != 0:
                    count+=1
            return count
        no_of_bits = func(b)
        num = 0
        j = 31
        while(j>-1):
            if ((a&(1<<j)) and no_of_bits>0):
                num|=1<<j
                no_of_bits-=1
            j-=1
        k = 0
        while(no_of_bits>0):
            if num&(1<<k) == 0:
                num|=(1<<k)
                no_of_bits-=1
            k+=1
        return num
