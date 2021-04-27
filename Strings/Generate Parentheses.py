class Solution:
    def AllParenthesis(self,n):
        #code here
        res = []
        st = ['']*(2*n)
        def func(res,n,open,pos,close,st):
            if open == close == n:
                res.append(''.join(item for item in st))
                return
            if open>close:
                st[pos] = ')'
                func(res,n,open,pos+1,close+1,st)
            if open<n:
                st[pos] = '('
                func(res,n,open+1,pos+1,close,st)
                
                
        func(res,n,0,0,0,st)
        return res
