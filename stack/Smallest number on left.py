class Solution:
    def leftSmaller(self, n, a):
        # code here
        stack = []
        ans = []
        for i in range(n):
            while len(stack)!=0 and a[i]<=stack[-1]:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(a[i])
        return ans
