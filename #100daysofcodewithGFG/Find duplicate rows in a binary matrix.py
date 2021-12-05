class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        from collections import defaultdict
        dd = defaultdict(list)
        for i in range(m):
            su = 0
            k = 0
            for j in range(n):
                su+=(10**k)*arr[i][j]
                k+=1
            dd[su].append(i)
        ans = []
        for k,v in dd.items():
            if (len(v)>1):
                for i in range(1,len(v)):
                    ans.append(v[i])
                
        return sorted(ans)
