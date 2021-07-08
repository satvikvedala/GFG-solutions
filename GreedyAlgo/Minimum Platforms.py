class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr = sorted(arr)
        dep = sorted(dep)
        i = 1
        j = 0
        ma = 1
        res = 1
        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                ma+=1
                i+=1
                res = max(res,ma)
            else:
                ma-=1
                j+=1
        return res
