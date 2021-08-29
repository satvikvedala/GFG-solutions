class Solution:
    def bottomView(self, root):
        # code here
        def func(root,li,y,x):
            if root == None:
                return
            if x not in li:
                li[x] = (root.data,y)
            else:
                if y>= li[x][1]:
                    li[x] = (root.data,y)
            func(root.left,li,y+1,x-1)
            func(root.right,li,y+1,x+1)
        li = dict()
        func(root,li,0,0)
        res = []
        for k,v in sorted(li.items()):
            res.append(v[0])
            
        return res
