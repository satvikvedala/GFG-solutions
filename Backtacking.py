#Rat in a Maze Problem - I
class Solution:
    def findPath(self, m, n):
        # code here
        res = []
        st = ''
        visited = [[False for i in range(n)] for j in range(n)]
        def func(mat,n,res,st,visited,i,j):
            if i<0 or j<0 or i>=n or j>=n or mat[i][j] == 0:
                return
            if i == n-1 and j == n-1:
                visited[i][j] = True
                res.append(st)
                return
            mat[i][j] = 0
            func(mat,n,res,st+'D',visited,i+1,j)
            func(mat,n,res,st+'U',visited,i-1,j)
            func(mat,n,res,st+'L',visited,i,j-1)
            func(mat,n,res,st+'R',visited,i,j+1)
            mat[i][j] = 1
            
        func(m,n,res,st,visited,0,0)
        res = sorted(res)
        return res
