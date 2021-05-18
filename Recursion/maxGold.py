class Solution:
    def maxGold(self, n, m, M):
        # code here
        def func(n,m,M,i,j):
            if i<0:
                return 0
            if i>=n:
                return 0
            if j<0:
                return 0
            if j>=m:
                return 0
            su = M[i][j]
            su = su+max(func(n,m,M,i-1,j+1),max(func(n,m,M,i,j+1),func(n,m,M,i+1,j+1)))
            return su
        ma = 0
        for i in range(n):
            ma = max(ma,func(n,m,M,i,0))
        return ma
