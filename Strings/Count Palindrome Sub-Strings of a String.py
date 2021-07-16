class Solution:

    def CountPS(self, S, N):
        # code here
        count = 0
        for i in range(N):
            st = ''
            st+=S[i]
            for j in range(i+1,N):
                st+=S[j]
                if st == st[::-1]:
                    count+=1
        return count
                
