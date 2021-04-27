class Solution:
    #Complete this function
    # Function for finding maximum AND value.
    def maxAND(self, arr,N):
        #Your code here
        def func(pattern,arr,N):
            count = 0
            for item in arr:
                if(pattern&item == pattern):
                    count+=1
            return count
        res = 0
        for i in range(31,-1,-1):
            count = func(res|(1<<i),arr,N)
            if count>=2:
                res = res|(1<<i)
        return res
