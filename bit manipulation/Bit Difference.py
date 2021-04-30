class Solution:
    def countBits(self, N, A):
        # code here
        su = 0
        for i in range(0,32):
            count = 0
            for j in range(N):
                if (A[j]&(1<<i)):
                    count+=1
            su += count*(N-count)*2
        return su%1000000007
