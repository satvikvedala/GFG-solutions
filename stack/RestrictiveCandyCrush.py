class Solution:
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        stack = []
        if k == 1:
            return ''
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append([s[i],1])
            elif stack[-1][0]!=s[i]:
                stack.append([s[i],1])
            else:
                if stack[-1][1]==k-1:
                    stack.pop(-1)
                else:
                    stack[-1][1]+=1
        return ''.join(x[0]*x[1] for x in stack)
