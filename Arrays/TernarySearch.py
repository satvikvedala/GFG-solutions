    def ternarySearch(self,arr,N,K):
        #Your code here
        def func(arr,N,K,l,r):
            while l<=r:
                mid1 = l+(r-l)//3
                mid2 = r - (r-l)//3
                if arr[mid1] == K:
                    return 1
                elif arr[mid2] == K:
                    return 1
                elif K<arr[mid1]:
                    r = mid1-1
                elif K>arr[mid2]:
                    l = mid2+1
                else:
                    l = mid1+1
                    r = mid2-1
        ans = func(arr,N,K,0,N-1)
        if ans == None:
            return -1
        return ans
