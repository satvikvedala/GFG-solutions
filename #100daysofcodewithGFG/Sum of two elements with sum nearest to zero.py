class Solution:
    def closestToZero (self,arr, n):
        # your code here
        arr = sorted(arr)
        l = 0
        r = n-1
        su = 0
        mi = 9999999999
        while(l<r):
            su = arr[l]+arr[r]
            if abs(0-su) == abs(mi-0):
                mi = max(su,mi)
            elif abs(0-su)<abs(mi-0):
                mi = su
            if su == 0:
                return su
            elif su<0:
                l+=1
            else:
                r-=1
        return mi
