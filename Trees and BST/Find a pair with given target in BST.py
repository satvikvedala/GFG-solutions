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

    
    
#Using Stack and Revstack
class Solution:
    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self,root, target): 
        # code here.
        def addleftele(stack,root):
            while root:
                stack.append(root)
                root = root.left
        def addrightele(stack,root):
            while root:
                stack.append(root)
                root = root.right
        def nextele(stack):
            s = stack.pop()
            addleftele(stack,s.right)
            return s.data
        def prevele(stack):
            s = stack.pop()
            addrightele(stack,s.left)
            return s.data
        from collections import deque
        stack = deque()
        addleftele(stack,root)
        
        revstack = deque()
        addrightele(revstack,root)
        
        x = nextele(stack)
        y = prevele(revstack)
        
        while x<y:
            if x+y == target:
                return 1
            if x+y>target:
                if len(revstack):
                    y = prevele(revstack)
                else:
                    return 0
            else:
                if len(stack):
                    x = nextele(stack)
                else:
                    return 0
        return 0
