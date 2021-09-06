class Solution:
    def printNearNodes(self, root, low, high):
        #code here.
        def func(root,low,high,res):
            if root:
                func(root.left,low,high,res)
                if root.data>=low and root.data<=high:
                    res.append(root.data)
                func(root.right,low,high,res)
        res = []
        func(root,low,high,res)
        return res
