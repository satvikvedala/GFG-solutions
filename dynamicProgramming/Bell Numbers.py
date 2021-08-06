class Solution:
    def bellNumber (self, N):
        # code here
        arr = [[0 for j in range(N+1)] for i in range(N+1)]
        arr[0][0] = 1
        k = 10**9+7
        for i in range(1,N+1):
            arr[i][0] = arr[i-1][i-1]
            for j in range(1,i+1):
                arr[i][j] = (arr[i-1][j-1]+arr[i][j-1])%k
        return arr[N][0]
