class Solution:
    preindex = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def func2(ino,i,j,x):
            for k in range(i,j+1):
                if ino[k] == x:
                    return k
        def func(pre,ino,l,r):
            if l>r:
                return None
            else:
                root = TreeNode(pre[self.preindex])
                self.preindex+=1
                if l == r:
                    return root
                ind = func2(inorder,l,r,root.val)
                root.left = func(pre,ino,l,ind-1)
                root.right = func(pre,ino,ind+1,r)
                return root
        return func(preorder,inorder,0,len(preorder)-1)
