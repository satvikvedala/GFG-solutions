class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def func(root,arr):
            if root:
                func(root.left,arr)
                arr.append(root.data)
                func(root.right,arr)
        arr = []
        func(root,arr)
        for i in range(1,len(arr)):
            if arr[i]<=arr[i-1]:
                return False
        return True
