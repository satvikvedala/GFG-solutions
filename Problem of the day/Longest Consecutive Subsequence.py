    def findLongestConseqSubseq(self,arr, N):
        #code here
        mi = float("inf")
        ma = float("-inf")
        for i in range(N):
            mi = min(mi,arr[i])
        for i in range(N):
            ma = max(ma,arr[i])
        num = mi
        max_len = 1
        se = set()
        for i in range(N):
            se.add(arr[i])
        count = 1
        for i in range(mi+1,ma+1):
            if i in se:
                count+=1
            else:
                count = 0
            max_len  = max(max_len,count)
        return max_len
