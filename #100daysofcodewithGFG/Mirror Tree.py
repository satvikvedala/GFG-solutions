class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        def func(root):
            if root == None:
                return
            temp = root.right
            root.right = root.left
            root.left = temp
            func(root.left)
            func(root.right)
        head = root
        func(root)
        return head
