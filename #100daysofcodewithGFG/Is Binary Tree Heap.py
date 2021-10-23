class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        def height(root):
            if root == None:
                return 0
            else:
                return 1+max(height(root.left),height(root.right))
        def leftlen(root):
            if root == None:
                return 0
            else:
                return 1+leftlen(root.left)
        from collections import deque
        h = height(root)
        h1 = leftlen(root)
        if h != h1:
            return False
        dq = deque()
        dq.append(root)
        while dq:
            temp = dq.popleft()
            if temp.left:
                if temp.left.data<temp.data:
                    dq.append(temp.left)
                else:
                    return False
            if temp.right:
                if temp.right.data<temp.data:
                    dq.append(temp.right)
                else:
                    return False
        return True
