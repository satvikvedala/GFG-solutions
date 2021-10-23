class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self, root):
        '''
        :param root: root of the binary tree
        :return: None, newline is provided by driver code
        '''
        # code here
        def fillMap(root, d, l, m):
            if(root == None):
                return
             
            if d not in m:
                m[d] = [root.data,l]
            elif(m[d][1] > l):
                m[d] = [root.data,l]
            fillMap(root.left, d - 1, l + 1, m)
            fillMap(root.right, d + 1, l + 1, m)
        m = {}
        res = []
        fillMap(root, 0, 0, m)
        for it in sorted (m.keys()):
            res.append(m[it][0])
        return res
