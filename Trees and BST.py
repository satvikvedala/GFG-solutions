Range Sum of BST
	def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        if root.val<low:
            return self.rangeSumBST(root.right,low,high)
        if root.val>high:
            return self.rangeSumBST(root.left,low,high)
        return root.val+self.rangeSumBST(root.right,low,high)+self.rangeSumBST(root.left,low,high)

Binary Tree Paths
    def func(self,root,st,arr):
        if root.left == None and root.right == None:
            arr.append(st+str(root.val))
            return
        st = st+str(root.val)+'->'
        if root.left!=None:
            self.func(root.left,st,arr)
        if root.right!=None:
            self.func(root.right,st,arr)
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        arr = []
        if root == None:
            return arr
        self.func(root,'',arr)
        return arr
Merge Two Binary Trees
	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return
        if t1 == None:
            return t2
        if t2 == None:
            return  t1
        t1.val = t1.val+t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1

Search in a Binary Search Tree
iterative
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        res = None
        while root!=None:
            if root.val == val:
                return root
            elif root.val>val:
                root = root.left
            else:
                root = root.right
        return res
recursive
	def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        if root.val == val:
            return root
        elif root.val>val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)

N-ary Tree Postorder Traversal
	def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        temp = []
        while stack:
            curr = stack.pop()
            if curr:
                temp.append(curr.val)
                for child in curr.children:
                    stack.append(child)
        return temp[::-1]


Sum of Root To Leaf Binary Numbers
	def func(self,root,value):
        if root == None:
            return 0
        value = 2*value+root.val
        if root.left == None and root.right == None:
            return value
        return self.func(root.left,value)+ self.func(root.right,value)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.func(root,0)

Univalued Binary Tree
    def func(self,root,arr):
        if root!=None:
            self.func(root.left,arr)
            arr.append(root.val)
            self.func(root.right,arr)
        return arr
    def isUnivalTree(self, root: TreeNode) -> bool:
        arr = []
        arr = self.func(root,arr)
        if len(set(arr)) == 1:
            return True
        return False

 
Maximum Depth of Binary Tree

    def maxDepth(self, root: TreeNode) -> int:
        from collections import deque
        q = deque()
        if root == None:
            return 0
        count = 0
        q.append(root)
        while q:
            size = len(q)
            count+=1
            for i in range(size):
                curr = q.popleft()
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
        return count


Invert Binary Tree
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return 
        if root.left!=None:
            self.invertTree(root.left)
        if root.right!=None:
            self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root


Leaf-Similar Trees
    def leafsimilar(self,root,arr):
        if root == None:
            return
        if root.left == None and root.right == None:
            arr.append(root.val)
        self.leafsimilar(root.left,arr)
        self.leafsimilar(root.right,arr)
        return arr
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr1 = []
        arr2 = []
        arr1 = self.leafsimilar(root1,arr1)
        arr2 = self.leafsimilar(root2,arr2)
        if arr1 == arr2:
            return True
        return False

Average of Levels in Binary Tree
    from collections import deque
        q = deque()
        temp = []
        q.append(root)
        while q:
            size = len(q)
            su = 0
            for i in range(size):
                curr = q.popleft()
                su = su+curr.val
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
            temp.append(su/size)
        return temp


Trim a Binary Search Tree
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root == None:
            return
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        if root.val<low or root.val>high:
            if root.val<low:
                return root.right
            elif root.val>high:
                return root.left
        
        return root



Two Sum IV - Input is a BST
    def func(self,root,arr):
        if root!=None:
            self.func(root.left,arr)
            arr.append(root.val)
            self.func(root.right,arr)
        return arr
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []
        arr = self.func(root,arr)
        temp = []
        for item in arr:
            if k-item in temp:
                return True
            temp.append(item)
        return False


Convert Sorted Array to Binary Search Tree
    def func(self,nums,l,h):
        if l>h:
            return None
        mid = (l+h)//2
        root = TreeNode(nums[mid])
        root.left = self.func(nums,l,mid-1)
        root.right = self.func(nums,mid+1,h)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = 0
        h = len(nums)-1
        return self.func(nums,l,h)

Binary Tree Level Order Traversal II
def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        q = deque()
        dq = []
        if root == None:
            return dq
        q.append(root)
        while q:
            temp = []
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
            dq.append(temp)
        return dq[::-1]


Minimum Distance Between BST Nodes
    def func(self,root,arr):
        if root!=None:
            self.func(root.left,arr)
            arr.append(root.val)
            self.func(root.right,arr)
        return arr
    def minDiffInBST(self, root: TreeNode) -> int:
        arr = []
        arr = self.func(root,arr)
        mi = 999999999
        for i in range(1,len(arr)):
            mi = min(mi,arr[i]-arr[i-1])
        return mi


Lowest Common Ancestor of a Binary Search Tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root

path sum:
    def func(self,root,sum,su):
        if root == None:
            return False
        su = su+root.val
        print(su,root.val)
        if su == sum and root.left == None and root.right == None:
            return True
        return self.func(root.left,sum,su) or self.func(root.right,sum,su)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        su = 0
        flag = False
        flag =  self.func(root,sum,su)
        return flag

Find Mode in Binary Search Tree
    def func(self,root,arr):
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if curr.val not in arr:
                    arr[curr.val] = 1
                else:
                    arr[curr.val]+=1
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
        return arr
    def findMode(self, root: TreeNode) -> List[int]:
        arr = {}
        res = []
        if root == None:
            return res
        arr = self.func(root,arr)
        ma = 0
        for k,v in arr.items():
            if v>ma:
                ma = v
        
        for k,v in arr.items():
            if v == ma:
                res.append(k)
        return res
-----------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------
Medium level
Find a Corresponding Node of a Binary Tree in a Clone of That Tree
    def func(self,root1,root2,x):
        if root1 is None or root2 is None:
            return None
        if root1 is x and root1.val == root2.val:
            return root2
        left = self.func(root1.left,root2.left,x)
        right =  self.func(root1.right,root2.right,x)
        if left!=None:
            return left
        return right
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.func(original,cloned,target)
Deepest Leaves Sum
    def func(self,root,h):
        from collections import deque
        q = deque()
        q.append(root)
        level = 0
        su = 0
        while q:
            size = len(q)
            level+=1
            for i in range(size):
                curr = q.popleft()
                if level == h:
                    su = su+curr.val
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
        return su
    def height(self,root):
        if root == None:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def deepestLeavesSum(self, root: TreeNode) -> int:
        h = self.height(root)
        return self.func(root,h)

Maximum Binary Tree
    def max_index(self,nums):
        index = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[index]:
                index = i
        return index
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        mi = self.max_index(nums)
        root = TreeNode(nums[mi])
        if mi!=0:
            root.left = self.constructMaximumBinaryTree(nums[:mi])
        else:
            root.left = None
        if mi!=len(nums)-1:
            root.right = self.constructMaximumBinaryTree(nums[mi+1:])
        else:
            root.right = None
        return root

Delete Leaves With a Given Value
    def getleaves(self,root,target,arr):
        if root!=None:
            self.getleaves(root.left,target,arr)
            if root.left == None and root.right == None:
                arr.append(root.val)
            self.getleaves(root.right,target,arr)
        return arr
    def deletenode(self,root,x):
        if root == None:
            return None
        root.left = self.deletenode(root.left,x)
        root.right = self.deletenode(root.right,x)
        if (root.val == x) and (root.left == None and root.right == None):
            return None
        return root
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        leaves = []
        leaves = self.getleaves(root,target,leaves)
        print(leaves)
        while target in leaves:
            root = self.deletenode(root,target)
            leaves.remove(target)
            leaves = self.getleaves(root,target,leaves)
        return root

    def getleaves(self,root,target,arr):
        if root!=None:
            self.getleaves(root.left,target,arr)
            if root.left == None and root.right == None:
                arr.append(root.val)
            self.getleaves(root.right,target,arr)
        return arr

Binary Tree Pruning
    def getleaves(self,root,target,arr):
        if root!=None:
            self.getleaves(root.left,target,arr)
            if root.left == None and root.right == None:
                arr.append(root.val)
            self.getleaves(root.right,target,arr)
        return arr
    def deletenode(self,root,x):
        if root == None:
            return None
        root.left = self.deletenode(root.left,x)
        root.right = self.deletenode(root.right,x)
        if (root.val == x) and (root.left == None and root.right == None):
            return None
        return root
    def pruneTree(self, root: TreeNode) -> TreeNode:
        leaves = []
        leaves = self.getleaves(root,0,leaves)
        print(leaves)
        while 0 in leaves:
            root = self.deletenode(root,0)
            leaves.remove(0)
            leaves = self.getleaves(root,0,leaves)
        return root

Maximum Level Sum of a Binary Tree
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import deque
        q = deque()
        q.append(root)
        res = 9999999999
        level = 0
        bsu = -99999999999
        while q:
            size = len(q)
            csu = 0
            level +=1
            for i in range(size):
                curr = q.popleft()
                csu = csu+curr.val
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
            if csu>bsu:
                res = level
                bsu = csu
            elif csu == bsu:
                res = min(res,level)
        return res

Validate Binary Search Tree
    def func(self,root,ma,mi):
        if root == None:
            return True
        if (root.val>mi and root.val<ma) and (self.func(root.left,root.val,mi) and self.func(root.right,ma,root.val)):
            return True
        else:
            return False
    def isValidBST(self, root: TreeNode) -> bool:
        ma = float('inf')
        mi = float('-inf')
        return self.func(root,ma,mi)

Maximum Width of Binary Tree
    def func(self,root,q,x,y):
        if root!=None:
            q[x].append(y)
            self.func(root.left,q,x+1,2*y)
            self.func(root.right,q,x+1,2*y+1)
        return q
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = collections.defaultdict(list)
        q = self.func(root,q,0,0)
        res = 0
        print(q)
        for level in q:
            count = q[level][-1] - q[level][0]
            res = max(res,count+1)
        return res

Maximum Difference Between Node and Ancestor
    def func2(self,item):
        temp = list(map(int,item.split(" ")))
        a = max(temp)
        b = min(temp)
        return abs(a-b)
    def func(self,root,arr,st):
        if root.left == None and root.right == None:
            st = st+str(root.val)
            arr.append(st)
            return
        st = st+str(root.val)+" "
        if root.left!=None:
            self.func(root.left,arr,st)
        if root.right!=None:
            self.func(root.right,arr,st)
    def maxAncestorDiff(self, root: TreeNode) -> int:
        arr = []
        self.func(root,arr,'')
        res = 0
	#find paths from node to leaves and store them in arr
	#func2 is about max difference in each path
        for item in arr:
            res = max(res,self.func2(item))
        return res	


Binary Tree Maximum Path Sum
    def func2(self,root):
        if root == None:
            return float('-inf')
        return max(root.val,max(self.func2(root.left),self.func2(root.right)))
    def func(self,root,res):
        if root == None:
            return 0
        l = self.func(root.left,res)
        r = self.func(root.right,res)
        res[0] = max(res[0],max(root.val+l+r,max(root.val,max(root.val+r,root.val+l))))
        return max(root.val,max(root.val+l,root.val+r))
    def maxPathSum(self, root: TreeNode) -> int:
        res = [float('-inf')]
        su = self.func(root,res)
        return max(self.func2(root),res[0])


Binary Search Tree Iterator
    q = []
    index = 0
    def func(self,root,q):
        if root:
            self.func(root.left,q)
            q.append(root.val)
            self.func(root.right,q)
        return q
    def __init__(self, root: TreeNode):
        self.q = self.func(root,self.q)
        print(self.q)
    def next(self) -> int:
        if self.index<len(self.q):
            temp = self.index
            self.index = self.index+1
            return self.q[temp]

    def hasNext(self) -> bool:
        if self.index<len(self.q):
            return True
        else:
            self.q.clear()
            return False
	    
Sum Tree	    
 def isSumTree(self,root):
        # Code here
        def func(root):
            if root == None:
                return 0
            return root.data+func(root.left)+func(root.right)
        if root == None or (root.left == None and root.right == None):
            return True
        ls = func(root.left)
        rs = func(root.right)
        
        if ls+rs == root.data and self.isSumTree(root.left) and self.isSumTree(root.right):
            return True
        return False
	
Increasing Order Search Tree
	class Solution:
    def func(self,root,arr):
        if root!=None:
            self.func(root.left,arr)
            arr.append(root.val)
            self.func(root.right,arr)
        return arr
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        arr = self.func(root,arr)
        print(arr)
        temp = None
        curr = None
        for item in arr:
            if temp == None:
                temp = TreeNode(item)
                curr = temp
            else:
                okay = TreeNode(item)
                curr.right = okay
                curr = curr.right
        return temp

Boundary Traversal of binary tree
def printBoundaryView(root):
    # Code here
    res = []
    res.append(root.data)
    def func1(root,left):
        if root:
            if root.left:
                left.append(root.data)
                func1(root.left,left)
            elif root.right:
                left.append(root.data)
                func1(root.right,left)
    func1(root.left,res)
    def func2(root,leaves):
        if root:
            func2(root.left,leaves)
            if root.left == None and root.right == None:
                leaves.append(root.data)
            func2(root.right,leaves)
    func2(root.left,res)
    func2(root.right,res)
    def func3(root,right):
        if root:
            if root.right:
                func3(root.right,right)
                right.append(root.data)
            elif root.left:
                func3(root.left,right)
                right.append(root.data)
    func3(root.right,res)
    return res

Bottom View of Binary Tree
def bottomView(root):
    '''
    :param root: root of the binary tree
    :return: list containing the bottom view from left to right
    '''
    # code here
    from collections import defaultdict
    dic = defaultdict(list)
    def func(root,dic,x,y):
        if root:
            if y not in dic:
                dic[y] = (root.data,x)
            else:
                if x>=dic.get(y)[1]:
                    dic[y] = (root.data,x)
            func(root.left,dic,x+1,y-1)
            func(root.right,dic,x+1,y+1)
    func(root,dic,0,0)
    dic = sorted(dic.items())
    res = []
    for item in dic:
        res.append(item[1][0])
    return res

Maximum Path Sum between 2 Leaf Nodes
def maxPathSum(root):
    # code here 
    res = [float("-inf")]
    def func(root,res):
        if root == None:
            return 0
        l = func(root.left,res)
        r = func(root.right,res)
        
        if root.left != None and root.right !=None:
            res[0] = max(res[0],l+r+root.data)
            return max(l,r)+root.data
        elif root.left == None:
            return r+root.data
        else:
            return l+root.data
    su = func(root,res)
    return res[0]
