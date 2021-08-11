class Solution:
    def maxLength(self, S):
        # code here
        stack = []
        res = 0
        stack.append(-1)
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                if len(stack)!=0:
                    stack.pop()
                if len(stack)!=0:
                    res = max(res,i-stack[-1])
                else:
                    stack.append(i)
        return res
