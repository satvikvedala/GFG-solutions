def constructTree(pre, preLN, n):
    # code here
    def func(pre,preLN,n,index):
        if index[0]>=n:
            return None
        if preLN[index[0]] == 'L':
            return Node(pre[index[0]])
        else:
            node = Node(pre[index[0]])
            index[0]+=1
            node.left = func(pre,preLN,n,index)
            index[0]+=1
            node.right = func(pre,preLN,n,index)
            return node
    index = [0]
    #print(func(pre,preLN,n,index).left.left.data)
    return func(pre,preLN,n,index)
