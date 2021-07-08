class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr = sorted(arr)
        dep = sorted(dep)
        stack = [arr[0]]
        i = 1
        j = 0
        ma = 0
        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                stack.append(arr[i])
                ma = max(ma,len(stack))
                i+=1
            else:
                stack.pop()
                j+=1
        return ma
