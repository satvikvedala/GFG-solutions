class Solution:
    def numberSequence(self, m, n):
        # code here
        arr = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j == 0:
                    arr[i][j] = 0
                elif j == 1:
                    arr[i][j] = i
                elif i<j:
                    arr[i][j] = 0
                else:
                    arr[i][j] = arr[i-1][j]+arr[i//2][j-1]
        return arr[m][n]
