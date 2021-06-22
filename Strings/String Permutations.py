class Solution:
    def permutation(self,s):
        def func(a,res,l,r):
            if l == r:
                res.append(''.join(a))
                return
            else:
                for i in range(l,r):
                    a[l],a[i] = a[i],a[l]
                    func(a,res,l+1,r)
                    a[l],a[i] = a[i],a[l]
        n = len(s)
        res = []
        func(list(s),res,0,n)
        return sorted(res)
