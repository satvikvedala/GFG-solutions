    def BinarySearch(self,arr,N,K):
        #Your code here
        def func(arr,N,K,l,r):
            while l<=r:
                mid = (l+r)//2
                if arr[mid] == K:
                    return 1
                elif arr[mid]<K:
                    l = mid+1
                else:
                    r = mid-1
        ans = func(arr,N,K,0,N-1)
        if ans == None:
            return -1
        return ans
