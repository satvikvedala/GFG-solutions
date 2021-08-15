class Solution:
    def distributeCandies(self, N, K):
        # code here 
        i = 1
        j = 0
        temp = N
        cumm = 0
        res = [0]*(K)
        while(N>0):
            cumm+=i
            if cumm<temp:
                res[j%K] += i
            else:
                res[j%K] += N
            N = N-i
            i+=1
            j+=1
            j = j%K
        return res
