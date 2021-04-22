class Solution:
    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self,root, target): 
        # code here.
        li = []
        se = set()
        def inorder(root):
            if root:
                inorder(root.left)
                li.append(root.data)
                inorder(root.right)
        inorder(root)
        for i in range(len(li)):
            if (target - li[i]) not in se:
                se.add(li[i])
            else:
                return 1
        return 0
