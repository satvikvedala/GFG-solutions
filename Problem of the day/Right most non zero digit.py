class Solution:
    def rightmostNonZeroDigit (self, N, A):
        # code here 
        c5 = 0
        c2 = 0
        for i in range(N):
            temp = A[i]
            while temp>0 and temp%5 == 0:
                temp = temp//5
                c5+=1
        for i in range(N):
            temp = A[i]
            while temp>0 and temp%2 == 0:
                temp = temp//2
                c2+=1
        prod = 1
        for i in range(N):
            prod = prod*A[i]
        res = 10**min(c2,c5)
        prod = prod//res
        if prod%10!=0:
            return prod%10
        return -1
