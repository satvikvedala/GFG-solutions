class Solution:
    def printMinNumberForPattern(ob,S):
        # code here 
        curr = 1
        prev = 0
        st = ''
        for i in range(len(S)+1):
            if i == len(S):
                for i in range(curr,prev,-1):
                    st+=str(i)
            elif S[i] == 'I':
                for i in range(curr,prev,-1):
                    st+=str(i)
                prev = curr
                curr+=1
            elif S[i] == 'D':
                curr+=1
        return st
