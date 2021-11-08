def countSubtreesWithSumX(root, x):
    
    # code here
    def func(root,x,count):
        if root == None:
            return 0
        left = func(root.left,x,count)
        right = func(root.right,x,count)
        if (left+right+root.data) == x:
            count[0]+=1
        return left+right+root.data
            
    count = [0]
    ans = func(root,x,count)
    return count[0]
