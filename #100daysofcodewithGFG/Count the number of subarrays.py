class Solution:
    def countSubarray(self, N, A, L, R):
        # code here
        def func(A,X):
            l = 0
            sm = 0
            size = 0
            for r in range(len(A)):
                sm+=A[r]
                while sm>X:
                    sm-=A[l]
                    l+=1
                size += r-l+1
            return size
        return func(A,R) - func(A,L-1)
