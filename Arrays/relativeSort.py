    def relativeSort (self,A1, N, A2, M):
        # Your Code Here
        res = {}
        for item in A1:
            if item in res:
                res[item]+=1
            else:
               res[item] = 1
        ans = []
        for item in A2:
            while item in res and res[item]>0:
                ans.append(item)
                res[item]-=1
        ma = -1
        for k,v in res.items():
            if k>ma:
                ma = k
        for item in range(ma+1):
            while item in res and res[item]>0:
                ans.append(item)
                res[item]-=1
        return ans
